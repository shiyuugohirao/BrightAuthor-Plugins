# Screenshot with URL

> [日本語版はこちら](README_ja.md)

## Overview

Captures a screenshot of the player display and serves it over HTTP. Access the latest snapshot by visiting a URL on the player's local web server.

## Plugin Name

```
Custom
```

## Installation

1. Download `GenerateSnapshotViaHTTP.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `GenerateSnapshotViaHTTP.brs`.
4. Set the plugin **Name** to `Custom`.

## Usage

The plugin starts an HTTP server on port **8081**. To capture and retrieve a screenshot:

```
http://<player_ip>:8081/mySnap
```

Replace `<player_ip>` with the player's IP address (e.g. `http://192.168.1.78:8081/mySnap`).

### Behavior

1. Creates a `mySnap` folder on the SD card if it does not exist.
2. Captures a JPEG screenshot at the current video resolution.
3. Saves the image as `mySnap/LastSnapshot.jpg`.
4. Returns the JPEG image in the HTTP response.

## Configuration

Screenshot parameters in the script:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `filetype` | JPEG | Image format |
| `quality` | 25 | JPEG quality |
| `Storage` | SD: | Storage device |
| HTTP port | 8081 | Local web server port |

## Notes

- The HTTP server runs alongside the main autorun web server on a separate port.
- Screenshots use the current `roVideoMode` resolution.

## Related Files

| File | Description |
|------|-------------|
| `GenerateSnapshotViaHTTP.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
