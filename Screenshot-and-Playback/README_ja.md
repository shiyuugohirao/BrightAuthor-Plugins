# Screenshot and Playback

> [English version](README.md)

## 概要

2 つの機能を提供します: (1) 10 秒ごとにプレイヤー画面のスクリーンショットを取得（前のファイルを上書き）、(2) Plugin Message または UDP コマンドで画像・動画をオンデマンド再生。

## プラグイン名

```
play
```

## インストール手順

1. このフォルダから `Screenshot_and_Playback.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`Screenshot_and_Playback.brs` を選択する。
4. プラグインの **Name** を `play` に設定する。

## スクリーンショット設定

`Screenshot_and_Playback.brs` の 380 行目付近のパラメータを編集します:

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| `width` / `height` | 1280 x 720 | スクリーンショット解像度 |
| `filename` | `screen.jpg`（SD ルート） | 出力ファイルパス |
| `filetype` | JPEG | 画像形式（または BMP） |

## 再生コマンド

| コマンド | 説明 |
|---------|------|
| `play!<filename>` | 指定した画像または動画ファイルを再生 |
| `play!folder!<foldername>` | SD カード上のフォルダ内の全ファイルを再生 |
| `play!transition!<number>` | 画像トランジションタイプを設定（0〜29） |

### トランジションタイプ

| 番号 | 効果 |
|------|------|
| 0 | トランジションなし（即時切替） |
| 1–4 | ワイプ（上、下、左、右） |
| 5–8 | 中心/コーナーからのエクスプロード |
| 10–11 | ベネチアンブラインド（縦/横） |
| 12–13 | コーム（縦/横） |
| 14 | 背景色へフェードアウト後フェードイン |
| 15 | 画像間クロスフェード |
| 16–19 | 端からスライド |
| 20–23 | 画面全体スライド |
| 24–25 | スケール疑似回転 |
| 26–29 | 端から拡大 |

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `Screenshot_and_Playback.brs` | メインプラグインスクリプト |

## 参考リンク

- スクリーンショットなしの再生は [Play-File](../Play-File/) を参照
- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
