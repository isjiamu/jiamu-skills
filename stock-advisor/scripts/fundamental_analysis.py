#!/usr/bin/env python3
"""
A股基本面分析模块
使用AKShare获取财务数据，计算核心基本面指标并生成评分
"""

import argparse
from typing import Optional

import akshare as ak
import pandas as pd


def fetch_financial_indicators(symbol: str) -> Optional[pd.DataFrame]:
    """获取财务分析指标"""
    try:
        df = ak.stock_financial_analysis_indicator(symbol=symbol)
        return df
    except Exception as e:
        print(f"[警告] 获取财务指标失败: {e}")
        return None


def fetch_stock_info(symbol: str) -> Optional[pd.DataFrame]:
    """获取股票基本信息"""
    try:
        df = ak.stock_individual_info_em(symbol=symbol)
        return df
    except Exception as e:
        print(f"[警告] 获取基本信息失败: {e}")
        return None


def fetch_realtime_quote(symbol: str) -> Optional[pd.Series]:
    """获取实时行情数据（含PE/PB等估值指标）"""
    try:
        df = ak.stock_zh_a_spot_em()
        row = df[df["代码"] == symbol]
        if row.empty:
            print(f"[警告] 未找到股票 {symbol} 的实时行情")
            return None
        return row.iloc[0]
    except Exception as e:
        print(f"[警告] 获取实时行情失败: {e}")
        return None


def safe_float(value, default: float = 0.0) -> float:
    """安全转换为浮点数"""
    try:
        v = float(value)
        return v if pd.notna(v) else default
    except (ValueError, TypeError):
        return default


def calc_growth_metrics(fin_df: pd.DataFrame) -> dict:
    """计算成长性指标（营收增长率、净利润增长率）"""
    result = {"revenue_growth": None, "net_profit_growth": None}
    if fin_df is None or len(fin_df) < 2:
        return result

    try:
        result["revenue_growth"] = safe_float(fin_df.iloc[0].get("主营业务收入增长率(%)", None))
        result["net_profit_growth"] = safe_float(fin_df.iloc[0].get("净利润增长率(%)", None))
    except (IndexError, KeyError):
        pass
    return result


def calc_profitability_metrics(fin_df: pd.DataFrame) -> dict:
    """计算盈利能力指标（ROE、毛利率）"""
    result = {"roe": None, "gross_margin": None}
    if fin_df is None or fin_df.empty:
        return result

    try:
        row = fin_df.iloc[0]
        result["roe"] = safe_float(row.get("净资产收益率(%)", None))
        result["gross_margin"] = safe_float(row.get("销售毛利率(%)", None))
    except (IndexError, KeyError):
        pass
    return result


def calc_valuation_metrics(quote: Optional[pd.Series]) -> dict:
    """从实时行情中提取估值指标（PE/PB/PS）"""
    result = {"pe_ttm": None, "pb": None, "ps": None}
    if quote is None:
        return result

    result["pe_ttm"] = safe_float(quote.get("市盈率-动态", None))
    result["pb"] = safe_float(quote.get("市净率", None))
    # PS = 总市值 / 营业收入，部分接口直接提供
    total_mv = safe_float(quote.get("总市值", 0))
    if total_mv > 0:
        result["ps"] = None  # 需要营收数据才能计算，留给下方补充
    return result


def calc_risk_metrics(fin_df: pd.DataFrame) -> dict:
    """计算风险指标（资产负债率）"""
    result = {"debt_to_asset": None}
    if fin_df is None or fin_df.empty:
        return result

    try:
        result["debt_to_asset"] = safe_float(fin_df.iloc[0].get("资产负债率(%)", None))
    except (IndexError, KeyError):
        pass
    return result


def fundamental_score(growth: dict, profitability: dict,
                      valuation: dict, risk: dict) -> dict:
    """
    综合基本面评分 (0-100)

    评分维度:
      - 成长性 (25分): 营收增长 + 净利润增长
      - 盈利能力 (25分): ROE + 毛利率
      - 估值合理性 (25分): PE/PB 越低越好（相对合理范围）
      - 财务安全 (25分): 资产负债率越低越好
    """
    score = 50  # 基础分

    # --- 成长性 ---
    rev_g = growth.get("revenue_growth")
    if rev_g is not None:
        if rev_g > 30:
            score += 10
        elif rev_g > 15:
            score += 6
        elif rev_g > 0:
            score += 2
        elif rev_g > -10:
            score -= 3
        else:
            score -= 8

    np_g = growth.get("net_profit_growth")
    if np_g is not None:
        if np_g > 30:
            score += 10
        elif np_g > 15:
            score += 6
        elif np_g > 0:
            score += 2
        elif np_g > -10:
            score -= 3
        else:
            score -= 8

    # --- 盈利能力 ---
    roe = profitability.get("roe")
    if roe is not None:
        if roe > 20:
            score += 10
        elif roe > 12:
            score += 6
        elif roe > 6:
            score += 2
        elif roe > 0:
            score -= 2
        else:
            score -= 8

    gm = profitability.get("gross_margin")
    if gm is not None:
        if gm > 50:
            score += 8
        elif gm > 30:
            score += 4
        elif gm > 15:
            score += 1
        else:
            score -= 4

    # --- 估值合理性 ---
    pe = valuation.get("pe_ttm")
    if pe is not None and pe > 0:
        if pe < 15:
            score += 8
        elif pe < 25:
            score += 4
        elif pe < 40:
            score -= 2
        else:
            score -= 8

    pb = valuation.get("pb")
    if pb is not None and pb > 0:
        if pb < 1.5:
            score += 6
        elif pb < 3:
            score += 2
        elif pb < 6:
            score -= 2
        else:
            score -= 6

    # --- 财务安全 ---
    da = risk.get("debt_to_asset")
    if da is not None:
        if da < 30:
            score += 8
        elif da < 50:
            score += 4
        elif da < 70:
            score -= 3
        else:
            score -= 8

    # 归一化到 0-100
    score = min(max(score, 0), 100)

    # 评级
    if score >= 80:
        rating = "优秀"
        stars = 5
    elif score >= 65:
        rating = "良好"
        stars = 4
    elif score >= 50:
        rating = "中性"
        stars = 3
    elif score >= 35:
        rating = "较弱"
        stars = 2
    else:
        rating = "警示"
        stars = 1

    return {"score": score, "rating": rating, "stars": stars}


def analyze_fundamental(symbol: str) -> dict:
    """
    完整基本面分析

    Args:
        symbol: 股票代码，如 "000001"

    Returns:
        包含基本信息、成长性、盈利能力、估值、风险和综合评分的字典
    """
    fin_df = fetch_financial_indicators(symbol)
    info_df = fetch_stock_info(symbol)
    quote = fetch_realtime_quote(symbol)

    # 解析基本信息
    stock_name = ""
    industry = ""
    if info_df is not None:
        info_map = dict(zip(info_df.iloc[:, 0], info_df.iloc[:, 1]))
        stock_name = info_map.get("股票简称", "")
        industry = info_map.get("行业", "")

    growth = calc_growth_metrics(fin_df)
    profitability = calc_profitability_metrics(fin_df)
    valuation = calc_valuation_metrics(quote)
    risk = calc_risk_metrics(fin_df)

    score_data = fundamental_score(growth, profitability, valuation, risk)

    return {
        "basic_info": {
            "symbol": symbol,
            "name": stock_name,
            "industry": industry,
        },
        "growth": growth,
        "profitability": profitability,
        "valuation": valuation,
        "risk": risk,
        "score": score_data,
    }


def format_pct(value, suffix: str = "%") -> str:
    """格式化百分比显示"""
    if value is None:
        return "N/A"
    return f"{value:.2f}{suffix}"


def format_ratio(value) -> str:
    """格式化倍数显示"""
    if value is None or value == 0:
        return "N/A"
    return f"{value:.2f}"


def print_report(result: dict) -> None:
    """打印基本面分析报告"""
    info = result["basic_info"]
    g = result["growth"]
    p = result["profitability"]
    v = result["valuation"]
    r = result["risk"]
    s = result["score"]

    print(f"\n{'=' * 50}")
    print(f"  {info['name']}({info['symbol']}) 基本面分析报告")
    print(f"  行业: {info['industry']}")
    print(f"{'=' * 50}")

    print(f"\n【成长性】")
    print(f"  营收增长率:     {format_pct(g['revenue_growth'])}")
    print(f"  净利润增长率:   {format_pct(g['net_profit_growth'])}")

    print(f"\n【盈利能力】")
    print(f"  ROE:            {format_pct(p['roe'])}")
    print(f"  销售毛利率:     {format_pct(p['gross_margin'])}")

    print(f"\n【估值水平】")
    print(f"  PE(TTM):        {format_ratio(v['pe_ttm'])}")
    print(f"  PB:             {format_ratio(v['pb'])}")

    print(f"\n【财务安全】")
    print(f"  资产负债率:     {format_pct(r['debt_to_asset'])}")

    print(f"\n{'─' * 50}")
    print(f"  综合评分: {s['score']} - {s['rating']} ({'⭐' * s['stars']})")
    print(f"{'─' * 50}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A股基本面分析工具")
    parser.add_argument("--symbol", type=str, required=True,
                        help="股票代码，如 000001")
    args = parser.parse_args()

    result = analyze_fundamental(args.symbol)
    print_report(result)
