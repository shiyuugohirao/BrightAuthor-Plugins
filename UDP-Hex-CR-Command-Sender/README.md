# UDP Hex CR Command Sender

> [日本語版はこちら](README_ja.md)

## Overview

Sends UDP commands encoded as hexadecimal strings. The hex data is converted to bytes and sent to the UDP destination configured in BrightAuthor.

## Plugin Name

```
udphex
```

## Installation

1. Download `udphex.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `udphex.brs`.
4. Set the plugin **Name** to `udphex`.
5. Configure the UDP destination in **File > Presentation Properties > I/O**.

## Usage

Send a Plugin Message or UDP command in the following format:

```
Udp!<hex_command>
```

The hex string is converted to a byte array via `FromHexString` and sent over UDP.

### Examples

```
Udp!FF0102030D
```

## Notes

- Unlike [UDP-CR-Command-Sender](../UDP-CR-Command-Sender/), this plugin does not append a CR automatically; include termination bytes in the hex string if needed.
- UDP destination is read from BrightAuthor I/O settings.

## Related Files

| File | Description |
|------|-------------|
| `udphex.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
