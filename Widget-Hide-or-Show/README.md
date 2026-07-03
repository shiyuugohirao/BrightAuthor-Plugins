# Widget Hide or Show

> [日本語版はこちら](README_ja.md)

## Overview

Dynamically shows or hides Ticker and Clock widget zones at runtime via Plugin Message or UDP commands.

## Plugin Name

```
custom
```

## Installation

1. Download ` Widget hide or show.brs` from this folder (note the leading space in the filename).
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select the plugin file.
4. Set the plugin **Name** to `custom`.

## Usage

Commands can be sent via **Send Plugin Message** or UDP on port **555**.

### Clock Widget

| Command | Description |
|---------|-------------|
| `clock!hide` | Hide the first Clock widget found |
| `clock!show` | Show the first Clock widget found |
| `clock!hide!<zone_name>` | Hide a specific Clock zone |
| `clock!show!<zone_name>` | Show a specific Clock zone |

### Ticker Widget

| Command | Description |
|---------|-------------|
| `ticker!hide` | Hide the first Ticker (Text) widget found |
| `ticker!show` | Show the first Ticker widget found |
| `ticker!hide!<zone_name>` | Hide a specific Ticker zone |
| `ticker!show!<zone_name>` | Show a specific Ticker zone |

### Examples

```
clock!hide
ticker!show!MyTicker
```

## Notes

- Zone names are matched case-insensitively.
- When multiple zones exist, use the three-field format with the zone name.

## Related Files

| File | Description |
|------|-------------|
| ` Widget hide or show.brs` | Main plugin script (filename has a leading space) |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
