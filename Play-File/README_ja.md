# Play File

> [English version](README.md)

## 概要

Plugin Message または UDP コマンドで、画像・動画ファイルをオンデマンド再生するプラグインです。単一ファイルの再生、またはフォルダ内の全ファイルを順次再生（動画プレイリストモード）に対応しています。

## 要件

- 対応画像形式: PNG, JPG, BMP
- 対応動画形式: MP4, WMV, MOV, VOB, MPG, TS
- 画像はデフォルトで 5 秒間表示後にクリアされます

## プラグイン名

**File > Presentation Properties > Autorun** で追加する際、プラグインの **Name** を次の値に設定してください:

```
play
```

## インストール手順

1. このフォルダから `play.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`play.brs` を選択する。
4. プラグインの **Name** を `play` に設定する。

## 使い方

BrightAuthor の **Send Plugin Message** または UDP ポート **555** からコマンドを送信できます。

### コマンド形式

| コマンド | 説明 |
|---------|------|
| `play!<filename>` | 指定した画像または動画ファイルを再生 |
| `play!folder!<folder_path>` | フォルダ内の全ファイルを順次再生（動画プレイリスト） |
| `play!debug` | デバッグログを有効化 |
| `play!reboot` | プレイヤーを再起動 |

### UDP

UDP ポート **555** に同じコマンド文字列を送信します。コマンドは `play` で始まる必要があります。

## 使用例

```
play!myvideo.mp4
play!folder!/videos
```

## 設定

`play.brs` 内で次の値を編集できます:

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| `s.imagetime%` | 5 | 各画像の表示秒数 |
| `s.udpReceiverPort` | 555 | UDP 受信ポート |
| `s.vclear` | true | 再生終了後に動画プレイヤーをクリア |
| `s.loop` | false | 単一動画ファイルをループ再生 |

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `play.brs` | メインプラグインスクリプト |

## 注意事項

- フォルダ再生（プレイリストモード）は現在動画ファイルのみ対応しています。
- 定期スクリーンショットと再生が必要な場合は [Screenshot-and-Playback](../Screenshot-and-Playback/) を参照してください。

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
