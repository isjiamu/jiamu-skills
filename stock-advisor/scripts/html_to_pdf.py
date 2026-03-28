#!/usr/bin/env python3
"""Convert an HTML file to PDF using Playwright (async API)."""

import argparse
import asyncio
import os
import sys

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Error: playwright is not installed.", file=sys.stderr)
    print("Install it with:", file=sys.stderr)
    print("  pip install playwright", file=sys.stderr)
    print("  playwright install chromium", file=sys.stderr)
    sys.exit(1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert an HTML file to PDF using Playwright."
    )
    parser.add_argument("input", help="Path to the input HTML file")
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output PDF path (default: same as input with .pdf extension)",
    )
    return parser.parse_args()


def resolve_output_path(input_path: str, output_arg: str | None) -> str:
    if output_arg:
        return os.path.abspath(output_arg)
    base, _ = os.path.splitext(input_path)
    return os.path.abspath(base + ".pdf")


async def html_to_pdf(input_path: str, output_path: str) -> None:
    file_url = "file://" + os.path.abspath(input_path)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(file_url, wait_until="networkidle")

        # Wait for fonts and styles to fully load
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(1000)

        await page.pdf(
            path=output_path,
            format="A4",
            margin={
                "top": "20mm",
                "bottom": "20mm",
                "left": "15mm",
                "right": "15mm",
            },
            print_background=True,
        )

        await browser.close()


def main() -> None:
    args = parse_args()
    input_path = os.path.abspath(args.input)

    if not os.path.isfile(input_path):
        print(f"Error: file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    output_path = resolve_output_path(input_path, args.output)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        asyncio.run(html_to_pdf(input_path, output_path))
    except Exception as e:
        print(f"Error generating PDF: {e}", file=sys.stderr)
        if "Executable doesn't exist" in str(e):
            print("Run: playwright install chromium", file=sys.stderr)
        sys.exit(1)

    print(output_path)


if __name__ == "__main__":
    main()
