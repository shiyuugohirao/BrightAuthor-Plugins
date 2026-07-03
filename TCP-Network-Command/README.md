# TCP Network Command

> [日本語版はこちら](README_ja.md)

## Overview

Sends a hexadecimal command over TCP to a network device. The default implementation sends a PJLink power-on command to a projector, but the message and port can be customized in the script.

## Plugin Name

```
PJLinkOn
```

## Installation

1. Download `PJLinkOn.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `PJLinkOn.brs`.
4. Set the plugin **Name** to `PJLinkOn`.

## Usage

Send a **Send Plugin Message** command with the projector's IP address as the message text:

```
192.168.1.100
```

The plugin connects to the device on TCP port **4352** (PJLink default) and sends the hex message defined in the script.

### Default PJLink Command

The default hex message `2531504F575220310D0A` corresponds to `%1POWR 1` (power on).

## Configuration

Edit `PJLinkOn.brs` to customize:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `projector_port` | 4352 | TCP port |
| `projector_message$` | `2531504F575220310D0A` | Hex command to send |

## Notes

- The Plugin Message text is used directly as the target IP address.
- Connection failure is logged to the serial console.

## Related Files

| File | Description |
|------|-------------|
| `PJLinkOn.brs` | Main plugin script (PJLink example by Tweaklab) |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
