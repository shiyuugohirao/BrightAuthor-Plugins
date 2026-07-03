# Framerate Matcher

> [English version](README.md)

## 概要

BrightAuthor プレゼンテーションは通常、画面解像度で設定された固定フレームレートを維持し、再生動画のフレームレートを無視します。このプラグインは、新しい動画の再生開始時に映像出力のフレームレートを動画ファイルに動的に合わせます。

## 要件

- ファームウェア 6.1.76 以降（スクリプト内の最小 FW: 6.1.58）
- プレゼンテーションに**動画ゾーンは 1 つのみ**

## プラグイン名

```
matchFrameRate
```

## インストール手順

1. このフォルダから `matchFrameRate.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`matchFrameRate.brs` を選択する。
4. プラグインの **Name** を `matchFrameRate` に設定する。

## 動画形式の制限

`roVideoPlayer.GetStreamInfo()` で実行時にフレームレートをプローブします。対応コンテナ:

- MP4 カプセル化でフレームレートが定義されている MP4（任意の動画コーデック）
- MPEG2-TS
- H.265 Elementary Stream (ES)

条件を満たさない動画は、フレームレート変更なしで通常再生されます。

## 注意事項

- 動画ファイルのプローブデータを使用して `roVideoMode.SetMode()` を動的に呼び出します。
- 1 プレゼンテーションあたり動画ゾーンは 1 つのみ対応です。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `matchFrameRate.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
