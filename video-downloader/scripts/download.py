#!/usr/bin/env python3
"""
Universal video downloader using yt-dlp.

Supports 1000+ websites including YouTube, Bilibili, Twitter/X, TikTok, and more.
Default output directory: ~/Downloads/Videos/

Requirements:
    - yt-dlp: Install via `brew install yt-dlp` (macOS) or `pip install yt-dlp`

Usage:
    python3 download.py "VIDEO_URL"
    python3 download.py "VIDEO_URL" -o ~/Desktop
    python3 download.py "VIDEO_URL" -f 1080
    python3 download.py "VIDEO_URL" -a
    python3 download.py "VIDEO_URL" -F
"""

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_OUTPUT_DIR = "~/Downloads/Videos"


def check_yt_dlp() -> bool:
    """Check if yt-dlp is installed."""
    result = subprocess.run(
        ["which", "yt-dlp"], capture_output=True, text=True
    )
    return result.returncode == 0


def get_yt_dlp_version() -> str:
    """Get yt-dlp version."""
    result = subprocess.run(
        ["yt-dlp", "--version"], capture_output=True, text=True
    )
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def download(
    url: str,
    output_dir: str = DEFAULT_OUTPUT_DIR,
    max_height: int = None,
    audio_only: bool = False,
    list_formats: bool = False,
    with_subs: bool = False,
    use_cookies: str = None,
) -> int:
    """
    Download video from URL using yt-dlp.

    Args:
        url: Video URL
        output_dir: Output directory
        max_height: Maximum video height (e.g., 1080, 720)
        audio_only: Extract audio only (as MP3)
        list_formats: List available formats instead of downloading
        with_subs: Download subtitles
        use_cookies: Browser to extract cookies from (chrome, firefox, etc.)

    Returns:
        Exit code (0 for success)
    """
    if not check_yt_dlp():
        print("Error: yt-dlp is not installed")
        print("Install via: brew install yt-dlp  # or: pip install yt-dlp")
        return 1

    print(f"yt-dlp version: {get_yt_dlp_version()}")

    cmd = ["yt-dlp"]

    # List formats only
    if list_formats:
        cmd.extend(["-F", url])
        return subprocess.run(cmd).returncode

    # Output directory
    output_path = Path(output_dir).expanduser().resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    cmd.extend(["-P", str(output_path)])

    # Browser cookies for authentication
    if use_cookies:
        cmd.extend(["--cookies-from-browser", use_cookies])

    # Audio only
    if audio_only:
        cmd.extend(["-x", "--audio-format", "mp3"])
    elif max_height:
        cmd.extend(["-f", f"bestvideo[height<={max_height}]+bestaudio/best"])
    else:
        cmd.extend(["-f", "bestvideo+bestaudio/best"])

    # Subtitles
    if with_subs:
        cmd.extend(["--write-subs", "--sub-lang", "zh,en,ja"])

    # Progress display
    cmd.append("--progress")

    # Add URL
    cmd.append(url)

    print(f"\nCommand: {' '.join(cmd)}\n")
    result = subprocess.run(cmd)

    if result.returncode == 0:
        print(f"\nDownload completed!")
        print(f"Location: {output_path}")
    else:
        print(f"\nDownload failed (exit code: {result.returncode})")
        print("\nTroubleshooting tips:")
        print("  1. Update yt-dlp: brew upgrade yt-dlp")
        print("  2. Try with cookies: python3 download.py URL --cookies chrome")
        print("  3. Check formats: python3 download.py URL -F")

    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Download videos from 1000+ websites using yt-dlp",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://youtu.be/VIDEO_ID"
  %(prog)s "https://www.bilibili.com/video/BV..." --cookies chrome
  %(prog)s "https://twitter.com/user/status/123" -f 720
  %(prog)s "VIDEO_URL" -a                        # Audio only
  %(prog)s "VIDEO_URL" -F                        # List formats
        """,
    )
    parser.add_argument("url", help="Video URL to download")
    parser.add_argument(
        "-o", "--output",
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "-f", "--format",
        type=int,
        metavar="HEIGHT",
        help="Max video height (e.g., 1080, 720, 480)",
    )
    parser.add_argument(
        "-a", "--audio",
        action="store_true",
        help="Download audio only (as MP3)",
    )
    parser.add_argument(
        "-F", "--list-formats",
        action="store_true",
        help="List available formats",
    )
    parser.add_argument(
        "--subs",
        action="store_true",
        help="Download subtitles (zh, en, ja)",
    )
    parser.add_argument(
        "--cookies",
        metavar="BROWSER",
        help="Browser to extract cookies from (chrome, firefox, safari, edge)",
    )

    args = parser.parse_args()

    exit_code = download(
        url=args.url,
        output_dir=args.output,
        max_height=args.format,
        audio_only=args.audio,
        list_formats=args.list_formats,
        with_subs=args.subs,
        use_cookies=args.cookies,
    )

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
