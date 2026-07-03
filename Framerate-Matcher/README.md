# Framerate Matcher

> [日本語版はこちら](README_ja.md)

## Overview

By default, a BrightAuthor presentation maintains a fixed framerate set by the presentation screen resolution, ignoring the framerate of the playing video. This plugin dynamically matches the video output framerate to the currently playing video file whenever a new video begins.

## Requirements

- Firmware 6.1.76 or later (minimum FW in script: 6.1.58)
- Presentation must contain **one video zone only**

## Plugin Name

```
matchFrameRate
```

## Installation

1. Download `matchFrameRate.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `matchFrameRate.brs`.
4. Set the plugin **Name** to `matchFrameRate`.

## Video Format Restrictions

The plugin probes framerate at runtime via `roVideoPlayer.GetStreamInfo()`. Supported containers:

- MP4 with framerate defined in MP4 encapsulation (any video codec)
- MPEG2-TS
- H.265 Elementary Stream (ES)

If a video does not meet these criteria, it plays normally without framerate change.

## Notes

- Uses probe data from the video file to call `roVideoMode.SetMode()` on the fly.
- Only one video zone is supported per presentation.

## Related Files

| File | Description |
|------|-------------|
| `matchFrameRate.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
