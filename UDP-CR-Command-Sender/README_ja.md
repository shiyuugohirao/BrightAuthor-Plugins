# UDP CR Command Sender

> [English version](README.md)

## 概要

キャリッジリターン（CR、ASCII 13）を末尾に付加して UDP 文字列を送信するプラグインです。BrightAuthor のプレゼンテーションプロパティで設定した UDP 送信先アドレス・ポートを使用します。

## プラグイン名

```
udpcr
```

## インストール手順

1. このフォルダから `udpcr.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`udpcr.brs` を選択する。
4. プラグインの **Name** を `udpcr` に設定する。
5. **File > Presentation Properties > I/O** で UDP 送信先アドレスとポートを設定する。

## 使い方

次の形式で Plugin Message または UDP コマンドを送信します:

```
Udp!<文字列>
```

文字列の末尾に CR 文字（`chr(13)`）が付加されて UDP 送信されます。

### 使用例

```
Udp!POWER ON
```

## 注意事項

- UDP 送信先は `bsp.udpAddress$` と `bsp.udpSendPort`（BrightAuthor の I/O 設定）から読み取られます。
- UDP で `udp` で始まるコマンドを受信した場合も処理されます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `udpcr.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
