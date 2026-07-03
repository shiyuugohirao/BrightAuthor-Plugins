# Play File

> [日本語版はこちら](README_ja.md)

## Overview

This plugin plays image or video files on demand via Plugin Message or UDP commands. It can play a single file or iterate through all files in a folder (video playlist mode).

## Requirements

- Supported image formats: PNG, JPG, BMP
- Supported video formats: MP4, WMV, MOV, VOB, MPG, TS
- Images display for 5 seconds by default before clearing

## Plugin Name

When adding this plugin in **File > Presentation Properties > Autorun**, set the plugin **Name** to:

```
play
```

## Installation

1. Download `play.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `play.brs`.
4. Set the plugin **Name** to `play`.

## Usage

Commands can be sent via **Send Plugin Message** in BrightAuthor or UDP on port **555**.

### Command Format

| Command | Description |
|---------|-------------|
| `play!<filename>` | Play the specified image or video file |
| `play!folder!<folder_path>` | Play all files in the folder sequentially (video playlist) |
| `play!debug` | Enable debug logging |
| `play!reboot` | Reboot the player |

### UDP

Send the same command strings to the player on UDP port **555**. Commands must start with `play`.

## Examples

```
play!myvideo.mp4
play!folder!/videos
```

## Configuration

The following values can be edited in `play.brs`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `s.imagetime%` | 5 | Seconds to display each image |
| `s.udpReceiverPort` | 555 | UDP listen port |
| `s.vclear` | true | Clear video player after playback ends |
| `s.loop` | false | Loop single video file |

## Related Files

| File | Description |
|------|-------------|
| `play.brs` | Main plugin script |

## Notes

- Folder playback currently supports video files only in playlist mode.
- For periodic screenshots plus playback, see [Screenshot-and-Playback](../Screenshot-and-Playback/).

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
