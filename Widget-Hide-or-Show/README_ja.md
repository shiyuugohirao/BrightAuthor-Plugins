# Widget Hide or Show

> [English version](README.md)

## 概要

Plugin Message または UDP コマンドで、Ticker および Clock ウィジェットゾーンの表示・非表示を実行時に切り替えるプラグインです。

## プラグイン名

```
custom
```

## インストール手順

1. このフォルダから ` Widget hide or show.brs` をダウンロードする（ファイル名の先頭にスペースがあります）。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、プラグインファイルを選択する。
4. プラグインの **Name** を `custom` に設定する。

## 使い方

**Send Plugin Message** または UDP ポート **555** からコマンドを送信できます。

### Clock ウィジェット

| コマンド | 説明 |
|---------|------|
| `clock!hide` | 最初に見つかった Clock ウィジェットを非表示 |
| `clock!show` | 最初に見つかった Clock ウィジェットを表示 |
| `clock!hide!<zone_name>` | 指定ゾーンの Clock を非表示 |
| `clock!show!<zone_name>` | 指定ゾーンの Clock を表示 |

### Ticker ウィジェット

| コマンド | 説明 |
|---------|------|
| `ticker!hide` | 最初に見つかった Ticker（Text）ウィジェットを非表示 |
| `ticker!show` | 最初に見つかった Ticker ウィジェットを表示 |
| `ticker!hide!<zone_name>` | 指定ゾーンの Ticker を非表示 |
| `ticker!show!<zone_name>` | 指定ゾーンの Ticker を表示 |

### 使用例

```
clock!hide
ticker!show!MyTicker
```

## 注意事項

- ゾーン名は大文字小文字を区別せずに照合されます。
- 複数ゾーンがある場合は、ゾーン名を含む 3 フィールド形式を使用してください。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| ` Widget hide or show.brs` | メインプラグインスクリプト（ファイル名の先頭にスペースあり） |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
