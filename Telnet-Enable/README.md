# Telnet Enable

> [日本語版はこちら](README_ja.md)

## Overview

Enables or disables Telnet on the player by writing to the networking registry. Telnet is useful for remote debugging and log access.

## Plugin Name

```
telnet
```

## Installation

1. Download `telnet_enable.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `telnet_enable.brs`.
4. Set the plugin **Name** to `telnet`.

## Usage

Commands can be sent via **Send Plugin Message** or UDP on port **555**.

| Command | Description |
|---------|-------------|
| `telnet!on` | Enable Telnet on port 23 |
| `telnet!off` | Disable Telnet |
| `telnet!reboot` | Reboot the player |
| `telnet!debug` | Enable debug logging |

## Notes

- Registry changes may require a manual reboot to take effect (automatic reboot is commented out in the script).
- Telnet writes to the `networking` registry section (`telnet` key set to `23` or blank).

## Related Files

| File | Description |
|------|-------------|
| `telnet_enable.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
