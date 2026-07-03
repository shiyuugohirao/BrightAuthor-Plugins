# Setup with Publish

> [日本語版はこちら](README_ja.md)

## Overview

Performs device setup by publishing a presentation to the player. Normally, device setup requires physically inserting a storage device; for Local File Networking (LFN) and Simple File Networking (SFN) players, this plugin enables remote configuration by publishing setup files.

## Plugin Name

```
setup
```

## Creating the Device Setup Package

1. Go to **Tools > Setup BrightSign Unit**.
2. Configure device settings as desired.
3. Click **Create Setup Files**.
4. Save setup files to a folder on your PC.
5. Zip the setup files into a file named `autorun.zip`.

**Important:** Setup files (`autoplugins.brs`, `brightsign-dumps`, etc.) must be at the **root** of the zip, not in a subdirectory.

**Note:** Empty folders may disappear when zipping; the plugin recreates necessary folders on the player.

## Installation

1. Download `setup_plugin.brs` from this folder.
2. Open a presentation to publish to the target player(s).
3. Go to **File > Presentation Properties > Autorun**.
4. Click **Add Script Plugin** and select `setup_plugin.brs`.
5. Set the plugin **Name** to `setup`.
6. Go to **File > Presentation Properties > Files** and add `autorun.zip`.
7. Publish the presentation normally.

## Usage

When the player receives the presentation, it performs device setup using the files in `autorun.zip`, reboots, and begins playing the published presentation.

Works with all publishing methods.

## Notes

- Prior pool folder is preserved if `pool` is not included inside `autorun.zip`.
- The `uservariables.db` file is deleted before reboot.

## Related Files

| File | Description |
|------|-------------|
| `setup_plugin.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
