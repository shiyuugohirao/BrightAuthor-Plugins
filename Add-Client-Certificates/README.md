# Add Client Certificates

> [日本語版はこちら](README_ja.md)

## Overview

Installs a client certificate on the player for use with remote HTML content that requires mutual TLS authentication. The certificate is loaded from a User Variable at plugin startup.

## Plugin Name

```
keystore
```

## Installation

1. Download `keystore.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `keystore.brs`.
4. Set the plugin **Name** to `keystore`.
5. Add the certificate file to the presentation asset pool.
6. Create a User Variable named `cert` with the certificate filename as the default value.

## Usage

On initialization, the plugin:

1. Reads the `cert` User Variable for the certificate filename.
2. Looks up the file in the presentation asset pool (or root path as fallback).
3. Adds the certificate to the player keystore.

Send `keystore!reload` via Plugin Message to re-check and install the certificate without rebooting.

## User Variables

| Variable | Description |
|----------|-------------|
| `cert` | Filename of the client certificate in the asset pool |

## Notes

- After a player reboot, the plugin must run again to reinstall the certificate.
- Certificate files should be included in the presentation before publishing.

## Related Files

| File | Description |
|------|-------------|
| `keystore.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
