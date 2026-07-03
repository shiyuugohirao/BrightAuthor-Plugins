# PDF Printer

> [日本語版はこちら](README_ja.md)

## Overview

Prints PDF documents to a networked printer by opening a TCP socket on port 9100 and sending PDF data to the printer's IP address.

See `PrintPDF.bpf` in this repository for a sample presentation.

## Plugin Name

```
printPDF
```

## Installation

1. Download `printPDFplugin.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `printPDFplugin.brs`.
4. Set the plugin **Name** to `printPDF`.
5. In **File > Presentation Properties > Files**, add the PDF files to print.
6. Create a User Variable `printerIP` with the printer's IP address as the default value.

## Usage

Attach a **Send Plugin Message** command to an event or state:

| Message | Description |
|---------|-------------|
| `printFiles` | Send all attached PDFs to `printerIP` on TCP port 9100 |

When printing completes, the plugin sends `printPDFsFinishedEvent`. Use this as a Plugin Message event trigger for transitions.

## User Variables

| Variable | Description |
|----------|-------------|
| `printerIP` | IP address of the network printer |

## Related Files

| File | Description |
|------|-------------|
| `printPDFplugin.brs` | Main plugin script |
| `PrintPDF.bpf` | Sample presentation |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
