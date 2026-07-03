# UDP Hex CR Command Sender

> [English version](README.md)

## 概要

16 進文字列でエンコードされた UDP コマンドを送信するプラグインです。16 進データはバイト配列に変換され、BrightAuthor で設定した UDP 送信先へ送信されます。

## プラグイン名

```
udphex
```

## インストール手順

1. このフォルダから `udphex.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`udphex.brs` を選択する。
4. プラグインの **Name** を `udphex` に設定する。
5. **File > Presentation Properties > I/O** で UDP 送信先を設定する。

## 使い方

次の形式で Plugin Message または UDP コマンドを送信します:

```
Udp!<16進コマンド>
```

16 進文字列は `FromHexString` でバイト配列に変換され、UDP で送信されます。

### 使用例

```
Udp!FF0102030D
```

## 注意事項

- [UDP-CR-Command-Sender](../UDP-CR-Command-Sender/) とは異なり、CR は自動付加されません。必要な場合は 16 進文字列に終端バイトを含めてください。
- UDP 送信先は BrightAuthor の I/O 設定から読み取られます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `udphex.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
