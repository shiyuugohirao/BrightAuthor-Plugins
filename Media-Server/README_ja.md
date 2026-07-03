# Media Server

> [English version](README.md)

## 概要

XT、XD、4K プレイヤーをメディアサーバーに変換し、マルチキャスト配信またはクライアントからの RTSP ストリーミング要求に応答します。HDMI 入力、プレゼンテーション画面、動画ファイルのストリーミングに対応しています。

ファイルがキャッシュされている場合（SD カードからの読み込みでない場合）、XDx30/XDx32 は最大 4 本の 19Mbps ストリーム、XT・4K・XDx33 は同一ファイル最大 50 本または異なるファイル 11 本（平均 16Mbps）に対応します。

**注意:** ファイルストリーミングは MPEG-2 トランスポートストリーム形式のみ対応です。

## 要件

- BrightAuthor 4.3 以降
- 画面または HDMI 入力のストリーミング: XTx43、XDx33、4Kx42、XDx32

## プラグイン名

```
server
```

## インストール手順

1. このフォルダから `server_plugin.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`server_plugin.brs` を選択する。
4. プラグインの **Name** を `server` に設定する。

## サーバーパラメータ

`server_plugin.brs` 内の値を編集します:

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| `s.streamdisplayenabled` | false | `true` でプレゼンテーション画面をストリーミング |
| `s.hdmioutenabled` | true | `false` でデフォルトの HDMI ストリーミングを無効化 |
| `s.hdmimultienabled` | false | `true` で HDMI 入力をマルチキャスト |

**注意:** 3 つすべてが false の場合、クライアントはサーバーから動画ファイルをストリーミングします。

### エンコーダー設定

HDMI 入力ストリーミング:

```
pipleline$="hdmi:,encoder:vformat=720p60&vbitrate=8000,"
```

HDMI マルチキャスト:

```
pipelineaddress$ = "hdmi:,encoder:vformat=720p30&vbitrate=8000,"+m.multicast$
```

プレゼンテーション画面:

```
display:mode=1&vformat=720p30&vbitrate=8000,encoder:,mem:/display
```

調整可能パラメータ: `vformat`（720p30、1080p60）、`vbitrate`（8000〜15000）。

### マルチキャストアドレス

`s.multicast$`（53 行目）を編集:

```
s.multicast$ = "rtp://239.192.0.0:5004/"
```

## ストリーミング URL

### ファイルストリーム

```
rtsp://ServerIpAddress:8090/file:///folder/file.ts
rtsp://ServerIpAddress:8090/file:///file.ts
```

### HDMI 入力

```
rtsp://serverIPAddress:8090/mem:/hdmi/stream.ts
```

### 画面ストリーム

```
rtsp://serverIPAddress:8090/mem:/display/stream.ts
```

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `server_plugin.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
