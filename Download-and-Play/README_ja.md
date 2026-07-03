# Download and Play

> [English version](README.md)

## 概要

URL から画像をダウンロードし、プレイヤー上で全画面表示するプラグインです。ネットワーク上のソースからサイネージコンテンツを動的に更新する用途に利用できます。

## プラグイン名

```
downplay
```

## インストール手順

1. このフォルダから `downplay.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`downplay.brs` を選択する。
4. プラグインの **Name** を `downplay` に設定する。

## 使い方

次の形式で Plugin Message または UDP コマンド（ポート **5000**）を送信します:

```
downplay!<URL>
```

プラグインは画像を非同期でダウンロードし、画面いっぱいにスケールして表示します。

| コマンド | 説明 |
|---------|------|
| `downplay!<URL>` | URL から画像をダウンロードして表示 |
| `downplay!stop` | 画像表示を停止 |
| `downplay!debug` | デバッグログを有効化 |
| `downplay!reboot` | プレイヤーを再起動 |

### 使用例

```
downplay!http://example.com/images/banner.jpg
```

## 注意事項

- 画像ファイルのみ対応（`roImagePlayer` で表示）。
- ダウンロードしたファイルは URL から抽出したファイル名でローカル保存されます。
- UDP コマンドは `downplay` で始まる必要があります。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `downplay.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
