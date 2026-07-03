# System Log Saver

> [日本語版はこちら](README_ja.md)

## Overview

Saves detailed kernel system logs to local player storage. These logs contain more debugging information than standard setup logs. If the Diagnostic Web Server is enabled, logs can be retrieved remotely without removing the SD card.

Log files are named with the date prefix in `mmddyyyy` format (e.g. `kernel_log.txt`). A new file is created each day; within a day, the same file is overwritten each time the parser runs.

**Warning:** Not recommended for permanent deployments. Log files will eventually fill local storage at an unpredictable rate. Intended for laboratory and test setups only.

## Installation (Data Feed Parser)

This plugin is added as a **Data Feed parser**, not an Autorun script plugin.

1. Download `klog.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Data Feeds**.
3. Click **Add Data Feed**.
4. Enter a **Feed name**.
5. In **Feed Specification**, enter: `file:///autoplugins.brs`
   - This URL is a placeholder; a working Data Feed is not required.
6. Choose an **Update Interval** (determines how often logs are saved).
7. Click **Browse** and select `klog.brs`.
8. Enter `klog` in **Parser Function Name**.
9. Click **OK**.

## Related Files

| File | Description |
|------|-------------|
| `klog.brs` | Parser script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
