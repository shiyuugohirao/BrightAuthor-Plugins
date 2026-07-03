# Change Ticker Separator

> [日本語版はこちら](README_ja.md)

## Overview

Changes the separator symbol between items in a scrolling Ticker zone. By default, BrightAuthor uses a diamond separator; this plugin can set it to a circle, square, or other supported symbol.

## Plugin Name

```
customT
```

## Installation

1. Download `ChangeSeparator.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `ChangeSeparator.brs`.
4. Set the plugin **Name** to `customT`.

## Usage

The plugin applies the separator symbol to all Ticker (`roTextWidget`) zones when the presentation starts and on each event.

## Configuration

Edit the `s.symbol` value in `ChangeSeparator.brs`:

| Value | Symbol |
|-------|--------|
| `:diamond:` | Diamond (default in BrightAuthor) |
| `:circle:` | Circle |
| `:square:` | Square |

Example:

```brightscript
s.symbol = ":circle:"
```

## Related Files

| File | Description |
|------|-------------|
| `ChangeSeparator.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
