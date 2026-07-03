# Chroma Luma Key Editor

> [English version](README.md)

## 概要

Video Only または Video or Images ゾーンに Chroma / Luma キーイングを適用し、指定色を透過させるプラグインです。グリーンスクリーン風のオーバーレイやピクチャインピクチャに利用できます。

## プラグイン名

```
chromaLuma
```

## インストール手順

1. このフォルダから `chromaLuma.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`chromaLuma.brs` を選択する。
4. プラグインの **Name** を `chromaLuma` に設定する。

## 使い方

次の形式で Plugin Message を送信します:

```
chromaLuma!<zone_name>!<luma>!<cr>!<cb>
```

| フィールド | 説明 |
|-----------|------|
| `zone_name` | キーイングを適用する動画ゾーン名 |
| `luma` | Luma 値（6 文字の 16 進、例: `FF0000`） |
| `cr` | Cr 色差値（16 進） |
| `cb` | Cb 色差値（16 進） |

プラグインはゾーンの video player に対して `SetKeyingValue` を呼び出します。

### 使用例

```
chromaLuma!main!00FF00!008000!008000
```

## 注意事項

- ゾーン名は大文字小文字を含め完全一致が必要です。
- ゾーンに有効な `videoPlayer` オブジェクトが必要です。
- 色値は 6 文字の 16 進文字列から解析されます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `chromaLuma.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
