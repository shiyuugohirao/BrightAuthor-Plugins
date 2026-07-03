# TCP Network Command

> [English version](README.md)

## 概要

16 進コマンドを TCP でネットワーク機器へ送信するプラグインです。デフォルト実装はプロジェクターへ PJLink 電源オンコマンドを送信しますが、スクリプト内でメッセージとポートをカスタマイズできます。

## プラグイン名

```
PJLinkOn
```

## インストール手順

1. このフォルダから `PJLinkOn.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`PJLinkOn.brs` を選択する。
4. プラグインの **Name** を `PJLinkOn` に設定する。

## 使い方

**Send Plugin Message** コマンドで、プロジェクターの IP アドレスをメッセージテキストとして送信します:

```
192.168.1.100
```

プラグインは TCP ポート **4352**（PJLink デフォルト）で機器に接続し、スクリプトで定義された 16 進メッセージを送信します。

### デフォルト PJLink コマンド

デフォルトの 16 進メッセージ `2531504F575220310D0A` は `%1POWR 1`（電源オン）に対応します。

## 設定

`PJLinkOn.brs` でカスタマイズ可能:

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| `projector_port` | 4352 | TCP ポート |
| `projector_message$` | `2531504F575220310D0A` | 送信する 16 進コマンド |

## 注意事項

- Plugin Message のテキストが送信先 IP アドレスとして直接使用されます。
- 接続失敗時はシリアルコンソールにログ出力されます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `PJLinkOn.brs` | メインプラグインスクリプト（Tweaklab による PJLink サンプル） |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
