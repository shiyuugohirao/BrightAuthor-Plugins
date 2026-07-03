# 4K Image Playback

> [English version](README.md)

## 概要

SD カード上のフォルダから 4K 静止画をスライドショー形式で表示するプラグインです。画像はアルファベット順に再生されます。4K242、4K1042、4K1142 プレイヤー向けで、Standalone 公開方式を使用します。

動作例は[サンプルプレゼンテーション](http://brightsignnetwork.com/download/Romeo/Play4KImagesFrom4KimagesFolder.zip)を参照してください。

## 要件

- 4K242、4K1042、または 4K1142 プレイヤー
- Standalone 公開方式（公開後に SD カードへ画像を追加）
- 全画面を占有する Video Only または Video or Images ゾーン
- インタラクティブプレイリスト

## プラグイン名

```
PlayImagesFromFolder
```

## インストール手順

1. このフォルダから `4K-Image-Plugin.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`4K-Image-Plugin.brs` を選択する。
4. プラグインの **Name** を `PlayImagesFromFolder` に設定する。

## 使い方

### Plugin Message

| メッセージ | 説明 |
|-----------|------|
| `FolderPlay` | `4KImages` フォルダから 4K 画像の再生を開始 |
| `BAPlay` | 画像プレイリスト終了時にプラグインから送信。Plugin Message イベントのトリガーに使用 |

### 4K 画像プレイリストの作成

1. 4K 画像用の Event Handler ステートを作成する（Home State にはできない）。必要なら Home State と Event Handler の間に短い Timeout（0.1 秒）を追加する。
2. Event Handler ステートへ遷移するイベントを追加する。
3. イベントの **Advanced** タブで **Send - Send Plugin Message** を追加し、`PlayImagesFromFolder` へ `FolderPlay` を送信する。
4. Event Handler ステートから離脱する Plugin Message イベントを追加する。
5. Plugin Message フィールドを `BAPlay` に設定し、再生完了時に遷移する。

連続ループする場合は、`BAPlay` の Plugin Message イベントに `FolderPlay` コマンドを追加し、**Remain on current state** に設定する。

## User Variable

| 変数 | 説明 |
|------|------|
| `ImageTimeOUTinSeconds` | 各 4K 画像の表示秒数 |

**File > Presentation Properties > Variables** で作成します。

## 設定

Standalone 方式で公開後:

1. SD カードのルート（`SD:/`）を開く。
2. `4KImages` フォルダを作成する。
3. 4K 画像をフォルダに追加する（アルファベット順に再生）。

## 注意事項

- 4K 動画デコーダーを使用するため、4K 画像と 4K 動画の同時表示はできません。4K 画像 + HD 動画は可能です。
- **Edit > Layout** ではゾーンは 1920x1080 と表示されますが、4K 画像が表示されます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `4K-Image-Plugin.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
