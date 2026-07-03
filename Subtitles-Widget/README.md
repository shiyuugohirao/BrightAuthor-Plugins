# Subtitles Widget

> [日本語版はこちら](README_ja.md)

## Overview

Displays subtitles for video files using an attached `.txt` file with timecodes. Supports multiple subtitled videos per presentation. Subtitle text files must be **UTF-8** encoded.

## Plugin Name

```
custom
```

## Installation

1. Download `subtitles_widget.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `subtitles_widget.brs`.
4. Set the plugin **Name** to `custom`.
5. Go to **File > Presentation Properties > Files** and add a `.txt` subtitle file for each video.

## Creating Subtitle Files

Use the same base filename as the video (different extension). Example: `Information_Clip.mov` → `Information_Clip.txt`.

Format: timecode on one line, subtitle text on the next line. Separate with carriage return (`\r\n`).

```
00:00:00:00
This is the first line of text.
00:00:04:23
This is the second line of text.
00:00:08:23
This is the third line of text.
```

Timecode format: `hours:minutes:seconds:frames`

To show no subtitle at a point, use a timecode followed by a blank line.

## Usage

Subtitles display automatically when a matching video plays. No commands or text widget setup required.

## Configuration

### Resizing the Subtitle Widget

Edit line 45 in `subtitles_widget.brs`:

```brightscript
s.rect=CreateObject("roRectangle", x, y, width, height)
```

Example for bottom strip on 1920x1080:

```brightscript
s.rect=CreateObject("roRectangle", 0, 900, 1920, 180)
```

By default, an "action safe" area is used.

## Related Files

| File | Description |
|------|-------------|
| `subtitles_widget.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
