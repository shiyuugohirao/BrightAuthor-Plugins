# Variable Countdown

> [日本語版はこちら](README_ja.md)

## Overview

Decrements a User Variable by 1 each time a countdown command is received. Useful for Live Text timers and countdown displays driven by User Variables.

## Plugin Name

```
countdown
```

## Installation

1. Download `var_countdown.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `var_countdown.brs`.
4. Set the plugin **Name** to `countdown`.
5. Create a User Variable in **File > Presentation Properties > Variables** with an integer default value.

## Usage

Send a Plugin Message or UDP command (port **555**) in the following format:

```
Countdown!<variable_name>
```

Each command decrements the variable by 1 (minimum 0). The updated value is written back via `SetCurrentValue`.

### Example

If User Variable `timer` has value `60`:

```
Countdown!timer
```

Result: `timer` becomes `59`.

## Notes

- Trigger countdown commands on a timer interval (e.g. every 1 second) using BrightAuthor events.
- Variable name in the command is case-sensitive and must match the User Variable name exactly.

## Related Files

| File | Description |
|------|-------------|
| `var_countdown.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
