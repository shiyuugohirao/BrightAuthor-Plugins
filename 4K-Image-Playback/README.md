# 4K Image Playback

> [日本語版はこちら](README_ja.md)

## Overview

Displays 4K still images in a slideshow from a folder on the SD card. Images are played alphabetically. Designed for 4K242, 4K1042, and 4K1142 players using Standalone publishing.

Download [this sample presentation](http://brightsignnetwork.com/download/Romeo/Play4KImagesFrom4KimagesFolder.zip) for a working example.

## Requirements

- 4K242, 4K1042, or 4K1142 player
- Standalone publishing method (images are added to SD card after publishing)
- Video Only or Video or Images zone occupying the full screen
- Interactive playlist

## Plugin Name

```
PlayImagesFromFolder
```

## Installation

1. Download `4K-Image-Plugin.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `4K-Image-Plugin.brs`.
4. Set the plugin **Name** to `PlayImagesFromFolder`.

## Usage

### Plugin Messages

| Message | Description |
|---------|-------------|
| `FolderPlay` | Start playing 4K images from the `4KImages` folder |
| `BAPlay` | Sent by the plugin when the image playlist finishes; use as a Plugin Message event trigger |

### Creating a 4K Image Playlist

1. Create an Event Handler state for 4K images (cannot be the Home State). Use a short Timeout (.1s) between Home State and Event Handler if needed.
2. Add an event transitioning to the Event Handler state.
3. In the event **Advanced** tab, add **Send - Send Plugin Message** to `PlayImagesFromFolder` with message `FolderPlay`.
4. Add a Plugin Message event to leave the Event Handler state.
5. Set the Plugin Message field to `BAPlay` to transition when playback completes.

For continuous loop, add the `FolderPlay` command to the `BAPlay` Plugin Message event and set it to **Remain on current state**.

## User Variables

| Variable | Description |
|----------|-------------|
| `ImageTimeOUTinSeconds` | Seconds each 4K image is displayed |

Create in **File > Presentation Properties > Variables**.

## Configuration

After publishing with Standalone method:

1. Navigate to the SD card root (`SD:/`).
2. Create a folder named `4KImages`.
3. Add 4K images to the folder (played alphabetically).

## Notes

- Uses the 4K video decoder; cannot display 4K image and 4K video simultaneously. 4K image + HD video is supported.
- The zone displays as 1920x1080 in **Edit > Layout** even though 4K images are shown.

## Related Files

| File | Description |
|------|-------------|
| `4K-Image-Plugin.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
