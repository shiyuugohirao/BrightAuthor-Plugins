# Screenshot and Playback

> [日本語版はこちら](README_ja.md)

## Overview

Two features: (1) captures a screenshot of the player display every 10 seconds (overwriting the previous file), and (2) plays image or video files on demand via Plugin Message or UDP commands.

## Plugin Name

```
play
```

## Installation

1. Download `Screenshot_and_Playback.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `Screenshot_and_Playback.brs`.
4. Set the plugin **Name** to `play`.

## Screenshot Configuration

Edit parameters around line 380 in `Screenshot_and_Playback.brs`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `width` / `height` | 1280 x 720 | Screenshot resolution |
| `filename` | `screen.jpg` (SD root) | Output file path |
| `filetype` | JPEG | Image format (or BMP) |

## Playback Commands

| Command | Description |
|---------|-------------|
| `play!<filename>` | Play specified image or video file |
| `play!folder!<foldername>` | Play all files in the folder on SD card |
| `play!transition!<number>` | Set image transition type (0–29) |

### Transition Types

| Number | Effect |
|--------|--------|
| 0 | No transition (immediate) |
| 1–4 | Wipes (top, bottom, left, right) |
| 5–8 | Explode from center/corners |
| 10–11 | Venetian blinds (vertical/horizontal) |
| 12–13 | Combs (vertical/horizontal) |
| 14 | Fade out to background, fade in |
| 15 | Crossfade between images |
| 16–19 | Slide from edges |
| 20–23 | Slide entire screen |
| 24–25 | Scale pseudo-rotation |
| 26–29 | Expand from edges |

## Related Files

| File | Description |
|------|-------------|
| `Screenshot_and_Playback.brs` | Main plugin script |

## See Also

- [Play-File](../Play-File/) for playback without screenshots
- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
