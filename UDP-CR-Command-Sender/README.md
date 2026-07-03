# UDP CR Command Sender

> [日本語版はこちら](README_ja.md)

## Overview

Sends a UDP string with a carriage return (CR, ASCII 13) appended to the end. Uses the UDP destination address and port configured in BrightAuthor presentation properties.

## Plugin Name

```
udpcr
```

## Installation

1. Download `udpcr.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `udpcr.brs`.
4. Set the plugin **Name** to `udpcr`.
5. Configure the UDP destination in **File > Presentation Properties > I/O** (UDP send address and port).

## Usage

Send a Plugin Message or UDP command in the following format:

```
Udp!<string>
```

The string is sent over UDP with a CR character (`chr(13)`) appended.

### Examples

```
Udp!POWER ON
```

## Notes

- UDP destination is read from `bsp.udpAddress$` and `bsp.udpSendPort` (BrightAuthor I/O settings).
- Commands starting with `udp` received via UDP are also processed.

## Related Files

| File | Description |
|------|-------------|
| `udpcr.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
