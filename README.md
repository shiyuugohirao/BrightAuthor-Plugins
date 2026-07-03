# BrightAuthor-Plugins

> [日本語版はこちら](README_ja.md)

## About This Repository

This repository is a **fork of the official [BrightSign/BrightAuthor-Plugins](https://github.com/brightsign/BrightAuthor-Plugins)** on GitHub. The plugin source code (`.brs` / `.bpf` files) is based on BrightSign's official samples and is intended to be used as-is for learning and reference.

**What was added in this fork:**

- Expanded **README** documentation for each plugin (requirements, plugin name, commands, configuration)
- Japanese documentation (**README_ja.md**) for every plugin and the root index
- A categorized plugin index with brief descriptions and links

**Purpose:** This fork is maintained for **learning and study**. It helps you understand what each official sample plugin does, how to install it in BrightAuthor, and how to use Plugin Messages, UDP commands, and User Variables. It is not an official BrightSign product.

For the latest official plugin code, refer to the [upstream repository](https://github.com/brightsign/BrightAuthor-Plugins). For authoritative documentation, see the [BrightSign Plugins and Parsers docs](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers).

## About the Plugins

Each folder contains a self-contained plugin (`.brs` or `.bpf` file) that extends [BrightAuthor](https://www.brightsign.biz/products/brightauthor). Plugins are added to a presentation via **File > Presentation Properties > Autorun** and run on the player at runtime.

## How to Use a Plugin

1. Open the plugin folder and read its [README](Blank-Plugin-Template/README.md) for requirements, plugin name, and commands.
2. Download the plugin file from GitHub: right-click the **Raw** link on the `.brs` file and choose **Save Link As...**
3. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
4. Click **Add Script Plugin** and select the downloaded `.brs` file.
5. Set the plugin **Name** exactly as documented in the plugin README (incorrect names will prevent the plugin from working).
6. Publish the presentation to your player.

To learn more about plugins, visit the [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers).

## Plugin Index

### Development

| Plugin | Description |
|--------|-------------|
| [Blank-Plugin-Template](Blank-Plugin-Template/README.md) | Starter template for writing a new plugin |

### Media Playback

| Plugin | Description |
|--------|-------------|
| [4K-Image-Playback](4K-Image-Playback/README.md) | Slideshow of 4K still images from an SD card folder |
| [Download-and-Play](Download-and-Play/README.md) | Download an image from a URL and display it full screen |
| [Framerate-Matcher](Framerate-Matcher/README.md) | Dynamically match video output framerate to the playing video |
| [Play-File](Play-File/README.md) | Play images or videos via Plugin Message commands |
| [Rotate-and-Seek](Rotate-and-Seek/README.md) | Rotate, seek, change speed, fade video; create scrolling Ticker zones |
| [Screenshot-and-Playback](Screenshot-and-Playback/README.md) | Periodic screenshots plus media playback commands |
| [Subtitles-Widget](Subtitles-Widget/README.md) | Overlay timed subtitles on video from `.txt` files |

### Streaming

| Plugin | Description |
|--------|-------------|
| [Media-Server](Media-Server/README.md) | Stream HDMI input, presentation display, or files via RTSP/multicast |
| [Media-Server-RTSP](Media-Server-RTSP/README.md) | RTSP file streaming server on port 8090 |

### Network Control

| Plugin | Description |
|--------|-------------|
| [TCP-Network-Command](TCP-Network-Command/README.md) | Send hex commands over TCP (e.g. PJLink projector control) |
| [UDP-CR-Command-Sender](UDP-CR-Command-Sender/README.md) | Send UDP strings with carriage return appended |
| [UDP-Hex-CR-Command-Sender](UDP-Hex-CR-Command-Sender/README.md) | Send UDP hex commands with carriage return appended |
| [Telnet-Enable](Telnet-Enable/README.md) | Enable, disable, or reboot Telnet on the player |
| [Pronto-Hex-Transmitter](Pronto-Hex-Transmitter/README.md) | Transmit IR commands using Pronto Hex Codes |

### UI and Widgets

| Plugin | Description |
|--------|-------------|
| [Widget-Hide-or-Show](Widget-Hide-or-Show/README.md) | Show or hide Ticker and Clock zones at runtime |
| [Change-Ticker-Separator](Change-Ticker-Separator/README.md) | Customize the separator symbol in scrolling Ticker zones |
| [Touch-Audio-Feedback](Touch-Audio-Feedback/README.md) | Play audio feedback on touch events via HDMI |
| [Send-User-Variables-To-HTML](Send-User-Variables-To-HTML/README.md) | Push User Variable updates to an HTML widget |
| [HTMLZoneMessage](HTMLZoneMessage/README.md) | Send and receive zone messages between HTML and BrightAuthor |

### Video and Display

| Plugin | Description |
|--------|-------------|
| [ChromaLuma-Key-Editor](ChromaLuma-Key-Editor/README.md) | Apply Chroma or Luma keying to video zones |
| [Set-Video-Mode](Set-Video-Mode/README.md) | Dynamically change Series 4 video output mode |
| [Screenshot-with-URL](Screenshot-with-URL/README.md) | Capture player screenshots via HTTP |

### Cloud and Setup

| Plugin | Description |
|--------|-------------|
| [Add-To-Cloud](Add-To-Cloud/README.md) | Register a BrightAuthor Classic player with BSN.cloud |
| [Setup-with-Publish](Setup-with-Publish/README.md) | Remotely configure devices by publishing a setup presentation |
| [Publish-Node](Publish-Node/README.md) | Unzip and run a Node.js (chronode) application from the presentation |
| [Add-Client-Certificates](Add-Client-Certificates/README.md) | Install client certificates for remote HTML content |

### Presentation Management

| Plugin | Description |
|--------|-------------|
| [Restore-Presentation](Restore-Presentation/README.md) | Save and restore the previous presentation in a multi-presentation setup |
| [Player-Rename-Local-File-Networking](Player-Rename-Local-File-Networking/README.md) | Rename the player in Local File Networking environments |
| [System-Log-Saver](System-Log-Saver/README.md) | Save kernel logs to local storage |

### Utilities

| Plugin | Description |
|--------|-------------|
| [PDF-Printer](PDF-Printer/README.md) | Send PDF files to a network printer over TCP port 9100 |
| [Variable-Countdown](Variable-Countdown/README.md) | Count down a User Variable on a timer interval |

## License

See [LICENSE](LICENSE).
