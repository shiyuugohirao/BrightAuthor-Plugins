# Set Video Mode

> [English version](README.md)

## 概要

Series 4 プレイヤーの映像出力モードを Plugin Message で動的に変更するプラグインです。解像度、フレームレート、色空間、色深度の設定に対応しています。

## 要件

- Series 4 プレイヤー

## プラグイン名

```
videomode
```

## インストール手順

1. このフォルダから `videomode_plugin.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`videomode_plugin.brs` を選択する。
4. プラグインの **Name** を `videomode` に設定する。

## 使い方

フィールド区切りに `!!` を使用して Plugin Message を送信します:

```
brightsign!!videomode!!<解像度>!!<色空間>!!<色深度>
```

| フィールド | 説明 | 必須 |
|-----------|------|------|
| `解像度` | 例: `1920x1080x60i` | はい |
| `色空間` | 例: `444` | 任意 |
| `色深度` | 例: `10bit` | 任意 |

### 使用例

解像度のみ:

```
brightsign!!videomode!!1920x1080x60i
```

解像度と色空間:

```
brightsign!!videomode!!1920x1080x60i!!444
```

全指定:

```
brightsign!!videomode!!1920x1080x60i!!444!!10bit
```

## 注意事項

- 無効な VideoMode はシリアルコンソールにログ出力されます。
- 内部で `roVideoMode.SetMode()` を使用します。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `videomode_plugin.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
