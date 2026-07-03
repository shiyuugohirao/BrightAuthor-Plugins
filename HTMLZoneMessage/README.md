# HTML Zone Message

> [日本語版はこちら](README_ja.md)

## Overview

This plugin enables bidirectional communication between an HTML widget and BrightAuthor zone messages. Zone messages sent from BrightAuthor are forwarded to the HTML widget via `PostJSMessage`, and messages from the HTML page can trigger zone messages back into the presentation.

## Requirements

- Minimum firmware: 1.0.0
- A presentation with an HTML widget zone

## Plugin Name

When adding this plugin in **File > Presentation Properties > Autorun**, set the plugin **Name** to:

```
htmlZoneMessage
```

## Installation

1. Download `htmlZoneMessage.brs` from this folder (right-click **Raw** and **Save Link As...**).
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `htmlZoneMessage.brs`.
4. Set the plugin **Name** to `htmlZoneMessage`.
5. Include the sample HTML and BPF files in your presentation as needed.

## Usage

### BrightAuthor to HTML

When a **Send Zone Message** event occurs, the plugin forwards the message parameter to the HTML widget:

```
PostJSMessage({ zoneMessage: <event parameter> })
```

Your HTML page should listen for this message in JavaScript.

### HTML to BrightAuthor

When the HTML widget sends a message with a `button` field, the plugin posts a zone message back to the presentation:

```javascript
// Example: HTML sends a message that triggers a zone message
{ button: "myParameter" }
```

This results in a `SEND_ZONE_MESSAGE` event with `eventParameter` set to `myParameter`.

### Plugin Messages

The plugin accepts Plugin Messages directed to `htmlZoneMessage`. Extend the handler in the script to process custom messages as needed.

## Configuration

The plugin automatically finds the first HTML widget in the presentation (`loadingHtmlWidget` in the zone HSM). Only one HTML widget is supported per plugin instance.

## Related Files

| File | Description |
|------|-------------|
| `htmlZoneMessage.brs` | Main plugin script |
| `SendAndReceiveZoneMessagesInHTML.bpf` | Sample BrightAuthor presentation |
| `HTMLSite.html` | Sample HTML page |
| `html/` | Duplicate copies of sample files |

## Notes

- Debug output is printed to the serial console when events are received.
- Ensure your HTML page handles `PostJSMessage` callbacks and sends widget events in the expected format.

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
