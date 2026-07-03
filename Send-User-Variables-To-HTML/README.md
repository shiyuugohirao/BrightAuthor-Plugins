# Send User Variables to HTML

> [日本語版はこちら](README_ja.md)

## Overview

Listens for `USER_VARIABLE_UPDATED` events and sends all User Variables to an HTML widget via `PostJSMessage`. Variables can be updated through the local web server on port 8008 or the BrightSign iPad app.

## Requirements

- Minimum firmware: 6.2.*

## Plugin Name

```
sendUserVars
```

## Installation

1. Download `sendUserVars.brs` from this folder.
2. Open `sendUserVariablesToHtml.bpf` in BrightAuthor and import missing files.
3. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
4. Click **Add Script Plugin** and select `sendUserVars.brs`.
5. Set the plugin **Name** to `sendUserVars`.
6. Publish the presentation.

## Usage

1. Publish the presentation to the player.
2. On the BrightSign iPad app, visit the local web server, or in a browser go to `http://<player_ip>:8008/`.
3. Change User Variables on the web interface.
4. Updated values are sent to the HTML widget and displayed on screen.

## Related Files

| File | Description |
|------|-------------|
| `sendUserVars.brs` | Main plugin script |
| `sendUserVariablesToHtml.bpf` | Sample presentation |
| `index.html` | Sample HTML page |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
