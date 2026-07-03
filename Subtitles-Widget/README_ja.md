# Subtitles Widget

> [English version](README.md)

## 概要

タイムコード付きの `.txt` ファイルを使用して動画ファイルの字幕を表示するプラグインです。1 プレゼンテーション内の複数動画に対応します。字幕テキストファイルは **UTF-8** エンコードである必要があります。

## プラグイン名

```
custom
```

## インストール手順

1. このフォルダから `subtitles_widget.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`subtitles_widget.brs` を選択する。
4. プラグインの **Name** を `custom` に設定する。
5. **File > Presentation Properties > Files** で、各動画用の `.txt` 字幕ファイルを追加する。

## 字幕ファイルの作成

動画と同じベースファイル名を使用します（拡張子のみ異なる）。例: `Information_Clip.mov` → `Information_Clip.txt`。

形式: 1 行目にタイムコード、次の行に字幕テキスト。キャリッジリターン（`\r\n`）で区切ります。

```
00:00:00:00
This is the first line of text.
00:00:04:23
This is the second line of text.
00:00:08:23
This is the third line of text.
```

タイムコード形式: `hours:minutes:seconds:frames`（時:分:秒:フレーム）

字幕を表示しない区間は、タイムコードの後に空行を置きます。

## 使い方

対応する動画が再生されると字幕が自動表示されます。コマンドやテキストウィジェットの設定は不要です。

## 設定

### 字幕ウィジェットのリサイズ

`subtitles_widget.brs` の 45 行目を編集します:

```brightscript
s.rect=CreateObject("roRectangle", x, y, width, height)
```

1920x1080 画面の下部ストリップの例:

```brightscript
s.rect=CreateObject("roRectangle", 0, 900, 1920, 180)
```

デフォルトでは「アクションセーフ」領域が使用されます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `subtitles_widget.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
