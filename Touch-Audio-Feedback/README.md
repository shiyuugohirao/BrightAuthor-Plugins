# Touch Audio Feedback

> [日本語版はこちら](README_ja.md)

## Overview

Plays an audio file through HDMI when a touch event is detected on the player. Provides audible feedback for interactive touch presentations.

## Plugin Name

```
touch
```

## Installation

1. Download `touch_audio_feedback.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `touch_audio_feedback.brs`.
4. Set the plugin **Name** to `touch`.
5. Add `ping.mp3` (or your preferred audio file) to the presentation asset pool.

## Usage

On any `roTouchEvent`, the plugin plays `ping.mp3` from the presentation pool via HDMI audio output.

Plugin Messages are also supported:

| Command | Description |
|---------|-------------|
| `touch!debug` | Enable debug logging |
| `touch!reboot` | Reboot the player |

## Configuration

Edit `touch_audio_feedback.brs` to change the default audio file:

```brightscript
s.file$ = "ping.mp3"
```

Audio is routed to HDMI via `roAudioOutput("HDMI")`.

## Related Files

| File | Description |
|------|-------------|
| `touch_audio_feedback.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
