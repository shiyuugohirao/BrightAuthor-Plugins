# Change Ticker Separator

> [English version](README.md)

## 概要

スクロール Ticker ゾーンの項目間区切り記号を変更するプラグインです。BrightAuthor のデフォルトはダイヤモンドですが、円・四角などに変更できます。

## プラグイン名

```
customT
```

## インストール手順

1. このフォルダから `ChangeSeparator.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`ChangeSeparator.brs` を選択する。
4. プラグインの **Name** を `customT` に設定する。

## 使い方

プレゼンテーション開始時および各イベント処理時に、すべての Ticker（`roTextWidget`）ゾーンへ区切り記号が適用されます。

## 設定

`ChangeSeparator.brs` の `s.symbol` 値を編集します:

| 値 | 記号 |
|----|------|
| `:diamond:` | ダイヤモンド（BrightAuthor デフォルト） |
| `:circle:` | 円 |
| `:square:` | 四角 |

例:

```brightscript
s.symbol = ":circle:"
```

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `ChangeSeparator.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
