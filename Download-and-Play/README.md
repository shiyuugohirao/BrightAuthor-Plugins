# Download and Play

> [日本語版はこちら](README_ja.md)

## Overview

Downloads an image from a URL and displays it full screen on the player. Useful for dynamically updating signage content from a network source.

## Plugin Name

```
downplay
```

## Installation

1. Download `downplay.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `downplay.brs`.
4. Set the plugin **Name** to `downplay`.

## Usage

Send a Plugin Message or UDP command (port **5000**) in the following format:

```
downplay!<URL>
```

The plugin downloads the image asynchronously and displays it scaled to fill the screen.

| Command | Description |
|---------|-------------|
| `downplay!<URL>` | Download and display image from URL |
| `downplay!stop` | Stop image display |
| `downplay!debug` | Enable debug logging |
| `downplay!reboot` | Reboot the player |

### Example

```
downplay!http://example.com/images/banner.jpg
```

## Notes

- Only image files are supported (displayed via `roImagePlayer`).
- Downloaded file is saved locally using the filename extracted from the URL.
- UDP commands must start with `downplay`.

## Related Files

| File | Description |
|------|-------------|
| `downplay.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
