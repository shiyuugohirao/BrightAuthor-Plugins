# Blank Plugin Template

> [日本語版はこちら](README_ja.md)

## Overview

A starter template for writing a new BrightAuthor plugin. The script demonstrates the basic plugin structure: initialization, event handling, and Plugin Message reception.

## Requirements

- Minimum firmware: 1.0.0

## Plugin Name

```
blank
```

## Installation

1. Download `blankPlugin.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `blankPlugin.brs`.
4. Set the plugin **Name** to `blank`.

## Usage

### Getting Started

1. Copy `blankPlugin.brs` and rename it for your plugin.
2. Do a find-replace on the string `blank` throughout the file (function names, plugin name, object name).
3. Implement your logic in the `ProcessEvent` handler.

### Plugin Messages

The template listens for Plugin Messages sent to `blank`. When received, it returns `true` to prevent other handlers from processing the event.

To send messages to other plugins, uncomment and modify the `PostMessage` block in the script.

## Related Files

| File | Description |
|------|-------------|
| `blankPlugin.brs` | Template plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
