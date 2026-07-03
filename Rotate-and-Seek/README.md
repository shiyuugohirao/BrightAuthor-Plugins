# Rotate and Seek

> [日本語版はこちら](README_ja.md)

## Overview

Rotate video, seek to positions, change playback speed, fade video, and create scrolling Ticker zones. All actions are triggered via Plugin Message or UDP commands on port **555**.

## Plugin Name

```
custom
```

## Installation

1. Download `rotate_and_seek.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `rotate_and_seek.brs`.
4. Set the plugin **Name** to `custom`.

## Usage

### Rotate

```
rotate!<zone_name>!<rotate_type>
```

| rotate_type | Description |
|-------------|-------------|
| r90 | 90° clockwise |
| r180 | 180° rotation |
| r270 | 270° clockwise |
| mirror | Horizontal mirror |
| m90 | Mirrored 90° clockwise |
| m180 | Mirrored 180° |
| m270 | Mirrored 270° clockwise |

Example: `rotate!main!r90`

### Seek

```
seek!<zone_name>!<video_position_ms>
```

Seeks to position in milliseconds. Does not seek past end of file.

Example: `seek!main!2500`

### Speed

```
speed!<playback_speed>
speed!<zone_name>!<playback_speed>
```

| Range | Behavior |
|-------|----------|
| 0 < speed < 1.0 | Slow forward |
| 1.0 | Normal forward |
| > 1.0 | Fast forward |
| -1.0 < speed < 0 | Slow reverse |
| -1.0 | Normal reverse |
| < -1.0 | Fast reverse |

Example: `speed!0.5` (half speed), `speed!-2.0` (2x rewind)

### Fade

```
fade!<fade_duration_ms>
fade!<zone_name>!<fade_duration_ms>
```

### Scrolling Ticker

Initialize zone:

```
ticker!scroll!<x>!<y>!<w>!<h>
```

| Command | Description |
|---------|-------------|
| `ticker!show` | Display the Ticker zone |
| `ticker!hide` | Hide the Ticker zone |
| `ticker!add!<text>` | Add text to the scrolling list |
| `ticker!message.txt` | Scroll contents of `message.txt` file (clears other strings) |
| `ticker!clear` | Clear all strings (takes effect after current string finishes) |
| `ticker!solid` | Black background (default) |
| `ticker!transparent` | Transparent background |

The Ticker zone is created by the plugin; no layout editing required.

## Related Files

| File | Description |
|------|-------------|
| `rotate_and_seek.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
