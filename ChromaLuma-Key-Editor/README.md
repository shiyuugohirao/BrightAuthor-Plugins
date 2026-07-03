# Chroma Luma Key Editor

> [日本語版はこちら](README_ja.md)

## Overview

Applies Chroma or Luma keying to a Video Only or Video or Images zone, making a selected color transparent. Useful for green-screen style overlays and picture-in-picture effects.

## Plugin Name

```
chromaLuma
```

## Installation

1. Download `chromaLuma.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `chromaLuma.brs`.
4. Set the plugin **Name** to `chromaLuma`.

## Usage

Send a Plugin Message in the following format:

```
chromaLuma!<zone_name>!<luma>!<cr>!<cb>
```

| Field | Description |
|-------|-------------|
| `zone_name` | Name of the video zone to key |
| `luma` | Luma value as 6-character hex (e.g. `FF0000`) |
| `cr` | Cr chroma value as hex |
| `cb` | Cb chroma value as hex |

The plugin calls `SetKeyingValue` on the zone's video player with the specified luma, cr, and cb values.

### Example

```
chromaLuma!main!00FF00!008000!008000
```

## Notes

- Zone name must match exactly (case-sensitive).
- The zone must have an active `videoPlayer` object.
- Color values are parsed from 6-character hex strings.

## Related Files

| File | Description |
|------|-------------|
| `chromaLuma.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
