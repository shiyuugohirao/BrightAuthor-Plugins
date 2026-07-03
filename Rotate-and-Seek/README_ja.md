# Rotate and Seek

> [English version](README.md)

## 概要

動画の回転、シーク、再生速度変更、フェード、スクロール Ticker ゾーンの生成が可能です。すべて Plugin Message または UDP ポート **555** のコマンドでトリガーします。

## プラグイン名

```
custom
```

## インストール手順

1. このフォルダから `rotate_and_seek.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`rotate_and_seek.brs` を選択する。
4. プラグインの **Name** を `custom` に設定する。

## 使い方

### 回転（Rotate）

```
rotate!<zone_name>!<rotate_type>
```

| rotate_type | 説明 |
|-------------|------|
| r90 | 時計回り 90° |
| r180 | 180° 回転 |
| r270 | 時計回り 270° |
| mirror | 水平ミラー |
| m90 | ミラー + 時計回り 90° |
| m180 | ミラー + 180° |
| m270 | ミラー + 時計回り 270° |

例: `rotate!main!r90`

### シーク（Seek）

```
seek!<zone_name>!<video_position_ms>
```

ミリ秒単位の位置へシークします。ファイル末尾を超えるシークは行いません。

例: `seek!main!2500`

### 速度（Speed）

```
speed!<playback_speed>
speed!<zone_name>!<playback_speed>
```

| 範囲 | 動作 |
|------|------|
| 0 < speed < 1.0 | スロー再生 |
| 1.0 | 通常速度（順再生） |
| > 1.0 | 早送り |
| -1.0 < speed < 0 | スロー逆再生 |
| -1.0 | 通常速度（逆再生） |
| < -1.0 | 高速逆再生 |

例: `speed!0.5`（半速）、`speed!-2.0`（2 倍速逆再生）

### フェード（Fade）

```
fade!<fade_duration_ms>
fade!<zone_name>!<fade_duration_ms>
```

### スクロール Ticker

ゾーン初期化:

```
ticker!scroll!<x>!<y>!<w>!<h>
```

| コマンド | 説明 |
|---------|------|
| `ticker!show` | Ticker ゾーンを表示 |
| `ticker!hide` | Ticker ゾーンを非表示 |
| `ticker!add!<text>` | スクロールリストにテキストを追加 |
| `ticker!message.txt` | `message.txt` の内容をスクロール（他の文字列をクリア） |
| `ticker!clear` | 全文字列をクリア（現在の文字列完了後に反映） |
| `ticker!solid` | 黒背景（デフォルト） |
| `ticker!transparent` | 透明背景 |

Ticker ゾーンはプラグインが作成するため、レイアウト編集は不要です。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `rotate_and_seek.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
