# Add to Cloud

> [日本語版はこちら](README_ja.md)

## Overview

Adds a BrightAuthor Classic player to BSN.cloud (control cloud, content cloud, or both). The plugin reads `cloudParams.json` and writes its values to the player registry.

## Plugin Name

Add the `addToCloud.brs` plugin to your presentation (plugin name is configured in BrightAuthor when adding the script).

## Setup Steps

1. Create a BSN setup in BrightAuthor:Connected.
2. Copy three values from `current-sync.json` in the setup into `cloudParams.json`:
   - `account` → `a`
   - `group` → `g`
   - `bsnRegistrationToken` → `bsnrt`
3. Publish a presentation with the plugin to a card.
4. Place `cloudParams.json` at the root of the card.

## Configuration

### Example Files

| File | Description |
|------|-------------|
| `ControlCloud_cloudParams.json` | Control cloud only |
| `ContentCloud_cloudParams.json` | Both control and content cloud |

To use control cloud only, set `"contentCloud": false` in `cloudParams.json` or remove the key.

If content cloud recovery is enabled, the plugin triggers recovery after writing the registry.

## Related Files

| File | Description |
|------|-------------|
| `addToCloud.brs` | Main plugin script |
| `ControlCloud_cloudParams.json` | Sample: control cloud only |
| `ContentCloud_cloudParams.json` | Sample: control + content cloud |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
