# Set Video Mode

> [日本語版はこちら](README_ja.md)

## Overview

Dynamically changes the video output mode on Series 4 players via Plugin Message. Supports setting resolution, frame rate, color space, and color depth.

## Requirements

- Series 4 players

## Plugin Name

```
videomode
```

## Installation

1. Download `videomode_plugin.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `videomode_plugin.brs`.
4. Set the plugin **Name** to `videomode`.

## Usage

Send a Plugin Message using `!!` as the field separator:

```
brightsign!!videomode!!<resolution>!!<color_space>!!<color_depth>
```

| Field | Description | Required |
|-------|-------------|----------|
| `resolution` | e.g. `1920x1080x60i` | Yes |
| `color_space` | e.g. `444` | Optional |
| `color_depth` | e.g. `10bit` | Optional |

### Examples

Resolution only:

```
brightsign!!videomode!!1920x1080x60i
```

Resolution and color space:

```
brightsign!!videomode!!1920x1080x60i!!444
```

Full specification:

```
brightsign!!videomode!!1920x1080x60i!!444!!10bit
```

## Notes

- Invalid video modes are logged to the serial console.
- Uses `roVideoMode.SetMode()` internally.

## Related Files

| File | Description |
|------|-------------|
| `videomode_plugin.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
