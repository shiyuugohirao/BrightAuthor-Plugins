# Telnet Enable

> [English version](README.md)

## 概要

ネットワークレジストリへ書き込むことで、プレイヤーの Telnet を有効化・無効化するプラグインです。Telnet はリモートデバッグやログ取得に利用できます。

## プラグイン名

```
telnet
```

## インストール手順

1. このフォルダから `telnet_enable.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`telnet_enable.brs` を選択する。
4. プラグインの **Name** を `telnet` に設定する。

## 使い方

**Send Plugin Message** または UDP ポート **555** からコマンドを送信できます。

| コマンド | 説明 |
|---------|------|
| `telnet!on` | ポート 23 で Telnet を有効化 |
| `telnet!off` | Telnet を無効化 |
| `telnet!reboot` | プレイヤーを再起動 |
| `telnet!debug` | デバッグログを有効化 |

## 注意事項

- レジストリ変更は手動再起動が必要な場合があります（スクリプト内の自動再起動はコメントアウトされています）。
- `networking` レジストリセクションの `telnet` キーに `23` または空白を書き込みます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `telnet_enable.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
