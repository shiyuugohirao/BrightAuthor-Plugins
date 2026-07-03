# Media Server RTSP

> [日本語版はこちら](README_ja.md)

## Overview

Converts an XD or 4K player into an RTSP Media Server that waits for client connections before streaming. Supports MPEG-2 transport stream files only.

When files are cached, XD players support up to four 19Mbps streams. 4K players support up to 50 19Mbps streams of the same file or 11 streams (16Mbps average) of different files.

## Plugin Name

```
server
```

## Installation

1. Download `Media_Server_RTSP.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `Media_Server_RTSP.brs`.
4. Set the plugin **Name** to `server`.

## Streaming URLs

RTSP server runs on port **8090** (configurable):

```
rtsp://ServerIpAddress:8090/file:///folder/file.ts
rtsp://ServerIpAddress:8090/file:///file.ts
```

## Server Parameters

### Maxbitrate

Sets the maximum instantaneous RTP bitrate in Kbps. Value `80000` (80Mbps) works well for XD players. Default (zero) means no limit.

Example: `rtsp:port=554&trace&maxbitrate=80000`

### Threads

Each thread handles one client. Default is `5`.

Example: `http:port=8080&threads=10`

## Related Files

| File | Description |
|------|-------------|
| `Media_Server_RTSP.brs` | Main plugin script |

## See Also

- [Media Server](../Media-Server/) for HDMI and display streaming
- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
