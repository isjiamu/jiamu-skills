# Platform-Specific Tips

## YouTube

### High-Quality Downloads (1080p+)

YouTube restricts high-quality formats for non-authenticated requests. Solutions:

#### Option 1: Browser Cookies (Recommended)

```bash
yt-dlp --cookies-from-browser chrome "VIDEO_URL"
```

Supported browsers: `chrome`, `firefox`, `safari`, `edge`, `opera`, `brave`

#### Option 2: PO Token Provider

For persistent high-quality access without browser dependency:

```bash
# Find yt-dlp's Python path
head -1 $(which yt-dlp)

# Install the plugin
/path/to/python -m pip install bgutil-ytdlp-pot-provider
```

### Age-Restricted Content

Requires authentication via cookies:

```bash
yt-dlp --cookies-from-browser chrome "VIDEO_URL"
```

## Bilibili

### Best Quality

```bash
# With authentication for high quality
yt-dlp --cookies-from-browser chrome "https://www.bilibili.com/video/BV..."

# Specify quality
yt-dlp -f "bestvideo+bestaudio" "https://www.bilibili.com/video/BV..."
```

### Download Entire Series

```bash
yt-dlp -P ~/Downloads/Videos "https://www.bilibili.com/video/BV..." --playlist-items 1-10
```

## Twitter/X

Usually works without authentication:

```bash
yt-dlp "https://twitter.com/user/status/123456789"
yt-dlp "https://x.com/user/status/123456789"
```

For protected tweets, use cookies:

```bash
yt-dlp --cookies-from-browser chrome "https://twitter.com/user/status/123456789"
```

## TikTok

```bash
# Download single video
yt-dlp "https://www.tiktok.com/@user/video/123456789"

# Without watermark (if available)
yt-dlp -f "download_addr-0" "https://www.tiktok.com/@user/video/123456789"
```

## Instagram

Requires authentication for most content:

```bash
yt-dlp --cookies-from-browser chrome "https://www.instagram.com/p/ABC123/"
yt-dlp --cookies-from-browser chrome "https://www.instagram.com/reel/ABC123/"
```

## Twitch

### VODs

```bash
yt-dlp "https://www.twitch.tv/videos/123456789"
```

### Clips

```bash
yt-dlp "https://clips.twitch.tv/ClipName"
```

## Vimeo

```bash
# Public videos
yt-dlp "https://vimeo.com/123456789"

# Password-protected
yt-dlp --video-password "PASSWORD" "https://vimeo.com/123456789"
```

## Common Issues

### "Sign in to confirm your age"

```bash
yt-dlp --cookies-from-browser chrome "VIDEO_URL"
```

### "Video is unavailable"

1. Check if video exists in browser
2. Try with cookies
3. Check if region-restricted (use VPN/proxy)

### Slow Downloads

```bash
# Limit concurrent downloads
yt-dlp --concurrent-fragments 3 "VIDEO_URL"

# Use external downloader
yt-dlp --downloader aria2c "VIDEO_URL"
```

### Network Issues (China)

```bash
# Use proxy
yt-dlp --proxy socks5://127.0.0.1:1080 "VIDEO_URL"

# Or environment variable
export ALL_PROXY=socks5://127.0.0.1:1080
```

## Useful Options Reference

| Option | Description |
|--------|-------------|
| `-F` | List all formats |
| `-f FORMAT` | Select format |
| `-P DIR` | Output directory |
| `-o TEMPLATE` | Output filename template |
| `-x` | Extract audio |
| `--audio-format mp3` | Convert to MP3 |
| `--write-subs` | Download subtitles |
| `--sub-lang LANGS` | Subtitle languages |
| `--cookies-from-browser BROWSER` | Use browser cookies |
| `--proxy URL` | Use proxy |
| `--limit-rate RATE` | Limit download speed |
