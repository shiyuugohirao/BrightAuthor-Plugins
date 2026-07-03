# Pronto Hex Transmitter

> [日本語版はこちら](README_ja.md)

## Overview

Sends IR commands using the [Pronto Hex Code](http://www.remotecentral.com/features/irdisp2.htm) (PHC) protocol. Trigger commands via Plugin Message or UDP from a BrightAuthor presentation.

**Note:** As of BrightAuthor version 3.8.0.27, PHC IR commands are supported natively via the **Send IR Remote (Pronto)** command. If you are using 3.8.0.27 or later, this plugin may be unnecessary.

## Requirements

- Firmware 4.7.96 or later (IR send/receive support)
- Player with IR output capability

## Plugin Name

```
sendir
```

## Installation

1. Edit `sendir.brs` with your device's PHC codes (see Configuration below).
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `sendir.brs`.
4. Set the plugin **Name** to `sendir`.

## Usage

### Plugin Messages

Send a **Send Plugin Message** to the `sendir` plugin with one of the predefined command names:

| Command | Default Action |
|---------|----------------|
| `tvon` | TV power on |
| `tvoff` | TV power off |
| `prjon` | Projector power on |
| `prjoff` | Projector power off |

### UDP Commands

Send UDP messages to port **21000** in the format:

```
sendir!<command>
```

Examples:

```
sendir!tvon
sendir!mute
```

## Configuration

### Editing PHC Codes

1. Visit [Remote Central IR Database](http://www.remotecentral.com/cgi-bin/codes/) and find your device's PHC codes.
2. Open `sendir.brs` in a text editor.
3. Replace the `s.tvoff`, `s.tvon`, `s.prjoff`, and `s.prjon` values in the `newSendIR` function.
4. Change the last four hex digits of each code to `0000`.

**Example:** Panasonic codes often end with `0ac2`; change to `0000` when adding to the plugin.

### Adding Custom Commands

Add new lines in the form:

```brightscript
s.mute = "0000 0071 ..."
```

Then trigger with Plugin Message `mute` or UDP `sendir!mute`.

## Notes

- The player must support IR output (`roIRRemote` object).
- UDP commands starting with `sendir` are processed on port 21000.

## Related Files

| File | Description |
|------|-------------|
| `sendir.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
