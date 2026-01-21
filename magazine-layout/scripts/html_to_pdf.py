#!/usr/bin/env python3
"""
HTML to PDF Converter for Magazine Layouts

This script converts HTML files (especially magazine-style layouts) to PDF.
Supports multiple rendering engines with automatic fallback.

Usage:
    python html_to_pdf.py <input.html> [output.pdf] [--engine ENGINE]

Options:
    --engine    Choose rendering engine: playwright, weasyprint, or wkhtmltopdf
                Default: auto-detect best available

Requirements:
    - playwright: pip install playwright && playwright install chromium
    - weasyprint: pip install weasyprint
    - wkhtmltopdf: brew install wkhtmltopdf (macOS) or apt install wkhtmltopdf (Linux)
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path


def check_playwright():
    """Check if playwright is available."""
    try:
        from playwright.sync_api import sync_playwright
        return True
    except ImportError:
        return False


def check_weasyprint():
    """Check if weasyprint is available."""
    try:
        import weasyprint
        return True
    except ImportError:
        return False


def check_wkhtmltopdf():
    """Check if wkhtmltopdf is available."""
    try:
        result = subprocess.run(['wkhtmltopdf', '--version'],
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def convert_with_playwright(input_html: str, output_pdf: str, page_width: str = "800px", page_height: str = "1200px"):
    """Convert HTML to PDF using Playwright (best quality for Tailwind CSS)."""
    from playwright.sync_api import sync_playwright

    input_path = Path(input_html).resolve()
    output_path = Path(output_pdf).resolve()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the HTML file
        page.goto(f"file://{input_path}")

        # Wait for fonts and styles to load
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1000)  # Extra wait for web fonts

        # Generate PDF
        page.pdf(
            path=str(output_path),
            format="A4",
            print_background=True,
            margin={
                "top": "0",
                "right": "0",
                "bottom": "0",
                "left": "0"
            }
        )

        browser.close()

    print(f"✅ PDF created: {output_path}")
    return str(output_path)


def convert_with_weasyprint(input_html: str, output_pdf: str):
    """Convert HTML to PDF using WeasyPrint."""
    import weasyprint

    input_path = Path(input_html).resolve()
    output_path = Path(output_pdf).resolve()

    # Read HTML and convert
    html = weasyprint.HTML(filename=str(input_path))
    html.write_pdf(str(output_path))

    print(f"✅ PDF created: {output_path}")
    return str(output_path)


def convert_with_wkhtmltopdf(input_html: str, output_pdf: str):
    """Convert HTML to PDF using wkhtmltopdf."""
    input_path = Path(input_html).resolve()
    output_path = Path(output_pdf).resolve()

    cmd = [
        'wkhtmltopdf',
        '--enable-local-file-access',
        '--enable-javascript',
        '--javascript-delay', '2000',
        '--page-size', 'A4',
        '--margin-top', '0',
        '--margin-right', '0',
        '--margin-bottom', '0',
        '--margin-left', '0',
        '--print-media-type',
        str(input_path),
        str(output_path)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"wkhtmltopdf failed: {result.stderr}")

    print(f"✅ PDF created: {output_path}")
    return str(output_path)


def detect_best_engine():
    """Detect the best available rendering engine."""
    if check_playwright():
        return "playwright"
    elif check_weasyprint():
        return "weasyprint"
    elif check_wkhtmltopdf():
        return "wkhtmltopdf"
    else:
        return None


def convert_html_to_pdf(input_html: str, output_pdf: str = None, engine: str = "auto"):
    """
    Convert HTML file to PDF.

    Args:
        input_html: Path to input HTML file
        output_pdf: Path to output PDF file (optional, defaults to same name as HTML)
        engine: Rendering engine to use (playwright, weasyprint, wkhtmltopdf, or auto)

    Returns:
        Path to generated PDF file
    """
    # Validate input
    input_path = Path(input_html)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_html}")

    # Set default output path
    if output_pdf is None:
        output_pdf = str(input_path.with_suffix('.pdf'))

    # Auto-detect engine if needed
    if engine == "auto":
        engine = detect_best_engine()
        if engine is None:
            raise RuntimeError(
                "No PDF rendering engine available. Please install one of:\n"
                "  - playwright: pip install playwright && playwright install chromium\n"
                "  - weasyprint: pip install weasyprint\n"
                "  - wkhtmltopdf: brew install wkhtmltopdf"
            )
        print(f"📄 Using {engine} for PDF conversion")

    # Convert using selected engine
    if engine == "playwright":
        if not check_playwright():
            raise RuntimeError("Playwright not installed. Run: pip install playwright && playwright install chromium")
        return convert_with_playwright(input_html, output_pdf)

    elif engine == "weasyprint":
        if not check_weasyprint():
            raise RuntimeError("WeasyPrint not installed. Run: pip install weasyprint")
        return convert_with_weasyprint(input_html, output_pdf)

    elif engine == "wkhtmltopdf":
        if not check_wkhtmltopdf():
            raise RuntimeError("wkhtmltopdf not installed. Run: brew install wkhtmltopdf")
        return convert_with_wkhtmltopdf(input_html, output_pdf)

    else:
        raise ValueError(f"Unknown engine: {engine}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert magazine-layout HTML to PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python html_to_pdf.py magazine.html
    python html_to_pdf.py magazine.html output.pdf
    python html_to_pdf.py magazine.html --engine playwright

Available engines:
    playwright   - Best quality, handles Tailwind CSS and web fonts well (recommended)
    weasyprint   - Good quality, pure Python solution
    wkhtmltopdf  - Lightweight, requires system install
        """
    )

    parser.add_argument("input", help="Input HTML file")
    parser.add_argument("output", nargs="?", help="Output PDF file (optional)")
    parser.add_argument("--engine", choices=["auto", "playwright", "weasyprint", "wkhtmltopdf"],
                       default="auto", help="PDF rendering engine (default: auto)")
    parser.add_argument("--check", action="store_true",
                       help="Check available engines and exit")

    args = parser.parse_args()

    if args.check:
        print("Checking available PDF engines...")
        print(f"  playwright:   {'✅ Available' if check_playwright() else '❌ Not installed'}")
        print(f"  weasyprint:   {'✅ Available' if check_weasyprint() else '❌ Not installed'}")
        print(f"  wkhtmltopdf:  {'✅ Available' if check_wkhtmltopdf() else '❌ Not installed'}")
        best = detect_best_engine()
        if best:
            print(f"\nRecommended engine: {best}")
        else:
            print("\n⚠️  No engines available. Please install one.")
        return

    try:
        output_path = convert_html_to_pdf(args.input, args.output, args.engine)
        print(f"\n🎉 Successfully converted to PDF: {output_path}")
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
