# Touch Audio Feedback

> [English version](README.md)

## 概要

プレイヤーでタッチイベントが検出されたとき、HDMI 経由で音声ファイルを再生するプラグインです。インタラクティブなタッチプレゼンテーションに音声フィードバックを提供します。

## プラグイン名

```
touch
```

## インストール手順

1. このフォルダから `touch_audio_feedback.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`touch_audio_feedback.brs` を選択する。
4. プラグインの **Name** を `touch` に設定する。
5. `ping.mp3`（または任意の音声ファイル）をプレゼンテーションのアセットプールに追加する。

## 使い方

`roTouchEvent` が発生すると、プレゼンテーションプール内の `ping.mp3` を HDMI 音声出力で再生します。

Plugin Message にも対応しています:

| コマンド | 説明 |
|---------|------|
| `touch!debug` | デバッグログを有効化 |
| `touch!reboot` | プレイヤーを再起動 |

## 設定

`touch_audio_feedback.brs` でデフォルトの音声ファイルを変更できます:

```brightscript
s.file$ = "ping.mp3"
```

音声は `roAudioOutput("HDMI")` 経由で HDMI に出力されます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `touch_audio_feedback.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
