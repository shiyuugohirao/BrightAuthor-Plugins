# Player Rename (Local File Networking)

> [日本語版はこちら](README_ja.md)

## Overview

Renames the player in Local File Networking (LFN) environments by writing to the networking registry. The new name can be set via a User Variable at startup or via Plugin Message / UDP at runtime.

## Plugin Name

```
lfnrename
```

## Installation

1. Download `LFNRename` from this folder (no file extension).
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `LFNRename`.
4. Set the plugin **Name** to `lfnrename`.

## Usage

### User Variable (at startup)

Create a User Variable named `lname` in **File > Presentation Properties > Variables**. On plugin initialization, if `lname` differs from the current registry name, the player renames itself and reboots.

### Plugin Message / UDP (port 555)

```
lfnrename!<new_name>
```

| Command | Description |
|---------|-------------|
| `lfnrename!<name>` | Set player name to `<name>` and reboot |
| `lfnrename!debug` | Enable debug logging |
| `lfnrename!reboot` | Reboot the player |

## Notes

- Writes to the `networking` registry section, key `un`.
- Player reboots automatically when the name changes.
- If the new name matches the current name, no change is made.

## Related Files

| File | Description |
|------|-------------|
| `LFNRename` | Main plugin script (no extension) |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
