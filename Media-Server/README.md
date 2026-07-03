# Media Server

> [日本語版はこちら](README_ja.md)

## Overview

Converts an XT, XD, or 4K player into a Media Server that can multicast streams or respond to client RTSP streaming requests. Supports streaming HDMI input, the presentation display, or video files.

When files are cached (not read from SD card), XDx30/XDx32 support up to four 19Mbps streams. XT, 4K, and XDx33 support up to 50 19Mbps streams of the same file or 11 streams (16Mbps average) of different files.

**Note:** Only MPEG-2 transport stream format is supported for file streaming.

## Requirements

- BrightAuthor 4.3 or newer
- XTx43, XDx33, 4Kx42, XDx32 for streaming presentation display or HDMI input

## Plugin Name

```
server
```

## Installation

1. Download `server_plugin.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `server_plugin.brs`.
4. Set the plugin **Name** to `server`.

## Server Parameters

Edit these values in `server_plugin.brs`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `s.streamdisplayenabled` | false | Set `true` to stream the presentation display |
| `s.hdmioutenabled` | true | Set `false` to disable default HDMI streaming |
| `s.hdmimultienabled` | false | Set `true` to multicast HDMI input |

**Note:** If all three are false, clients stream video files from the server.

### Encoder Settings

HDMI input streaming:

```
pipleline$="hdmi:,encoder:vformat=720p60&vbitrate=8000,"
```

Multicast HDMI:

```
pipelineaddress$ = "hdmi:,encoder:vformat=720p30&vbitrate=8000,"+m.multicast$
```

Presentation display:

```
display:mode=1&vformat=720p30&vbitrate=8000,encoder:,mem:/display
```

Adjustable parameters: `vformat` (720p30, 1080p60), `vbitrate` (8000–15000).

### Multicast Address

Edit `s.multicast$` (line 53):

```
s.multicast$ = "rtp://239.192.0.0:5004/"
```

## Streaming URLs

### File stream

```
rtsp://ServerIpAddress:8090/file:///folder/file.ts
rtsp://ServerIpAddress:8090/file:///file.ts
```

### HDMI input

```
rtsp://serverIPAddress:8090/mem:/hdmi/stream.ts
```

### Display stream

```
rtsp://serverIPAddress:8090/mem:/display/stream.ts
```

## Related Files

| File | Description |
|------|-------------|
| `server_plugin.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
