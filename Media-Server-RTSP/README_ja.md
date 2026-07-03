# Media Server RTSP

> [English version](README.md)

## 概要

XD または 4K プレイヤーを RTSP メディアサーバーに変換し、クライアント接続を待ってからストリーミングを開始します。MPEG-2 トランスポートストリームファイルのみ対応です。

ファイルがキャッシュされている場合、XD プレイヤーは最大 4 本の 19Mbps ストリーム、4K プレイヤーは同一ファイル最大 50 本または異なるファイル 11 本（平均 16Mbps）に対応します。

## プラグイン名

```
server
```

## インストール手順

1. このフォルダから `Media_Server_RTSP.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`Media_Server_RTSP.brs` を選択する。
4. プラグインの **Name** を `server` に設定する。

## ストリーミング URL

RTSP サーバーはポート **8090** で動作します（変更可能）:

```
rtsp://ServerIpAddress:8090/file:///folder/file.ts
rtsp://ServerIpAddress:8090/file:///file.ts
```

## サーバーパラメータ

### Maxbitrate

RTP の最大瞬間ビットレートを Kbps で設定します。値 `80000`（80Mbps）は XD プレイヤーで良好に動作します。デフォルト（ゼロ）は制限なしです。

例: `rtsp:port=554&trace&maxbitrate=80000`

### Threads

各スレッドが 1 クライアントを処理します。デフォルトは `5` です。

例: `http:port=8080&threads=10`

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `Media_Server_RTSP.brs` | メインプラグインスクリプト |

## 参考リンク

- HDMI・画面ストリーミングは [Media Server](../Media-Server/) を参照
- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
