# Add to Cloud

> [English version](README.md)

## 概要

BrightAuthor Classic プレイヤーを BSN.cloud（コントロールクラウド、コンテンツクラウド、または両方）に登録するプラグインです。`cloudParams.json` を読み取り、値をプレイヤーレジストリに書き込みます。

## プラグイン名

`addToCloud.brs` をプレゼンテーションに追加します（BrightAuthor でスクリプト追加時にプラグイン名を設定）。

## セットアップ手順

1. BrightAuthor:Connected で BSN セットアップを作成する。
2. セットアップ内の `current-sync.json` から 3 つの値を `cloudParams.json` にコピーする:
   - `account` → `a`
   - `group` → `g`
   - `bsnRegistrationToken` → `bsnrt`
3. プラグインを含むプレゼンテーションをカードに公開する。
4. `cloudParams.json` をカードのルートに配置する。

## 設定

### サンプルファイル

| ファイル | 説明 |
|---------|------|
| `ControlCloud_cloudParams.json` | コントロールクラウドのみ |
| `ContentCloud_cloudParams.json` | コントロール + コンテンツクラウド |

コントロールクラウドのみ使用する場合は、`cloudParams.json` で `"contentCloud": false` に設定するか、キーを削除します。

コンテンツクラウドのリカバリが有効な場合、レジストリ書き込み後にプラグインがリカバリを開始します。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `addToCloud.brs` | メインプラグインスクリプト |
| `ControlCloud_cloudParams.json` | サンプル: コントロールクラウドのみ |
| `ContentCloud_cloudParams.json` | サンプル: コントロール + コンテンツクラウド |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
