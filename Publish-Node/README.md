# Publish Node

> [日本語版はこちら](README_ja.md)

## Overview

Unzips and runs a chronode (Node.js) application from within a BrightAuthor presentation. Chronode apps work similarly to Electron apps on BrightSign players.

## Requirements

- Minimum firmware: 8.0.*

## Plugin Name

```
unzipNode
```

## Installation

1. Download `unzipNode.brs` from this folder.
2. Package your Node.js application as `node.zip`.
3. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
4. Click **Add Script Plugin** and select `unzipNode.brs`.
5. Set the plugin **Name** to `unzipNode`.
6. Add `node.zip` to **File > Presentation Properties > Files**.

## Usage

On presentation start, the plugin unzips `node.zip` and boots the chronode application.

## Notes

- Use webpack or another bundler to keep the application small. Bundling `node_modules` into a single script dramatically speeds up zip/unzip.
- See [BrightSign Node.js documentation](https://docs.brightsign.biz/display/DOC/Node.js) for chronode details.

## Related Files

| File | Description |
|------|-------------|
| `unzipNode.brs` | Main plugin script |

## See Also

- [BrightSign Node.js documentation](https://docs.brightsign.biz/display/DOC/Node.js)
- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
