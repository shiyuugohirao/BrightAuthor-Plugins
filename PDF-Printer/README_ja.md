# PDF Printer

> [English version](README.md)

## 概要

TCP ポート 9100 でソケットを開き、プリンターの IP アドレスへ PDF データを送信してネットワークプリンターに印刷するプラグインです。

サンプルプレゼンテーションはリポジトリ内の `PrintPDF.bpf` を参照してください。

## プラグイン名

```
printPDF
```

## インストール手順

1. このフォルダから `printPDFplugin.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`printPDFplugin.brs` を選択する。
4. プラグインの **Name** を `printPDF` に設定する。
5. **File > Presentation Properties > Files** で印刷する PDF ファイルを追加する。
6. `printerIP` という User Variable を作成し、プリンターの IP アドレスをデフォルト値に設定する。

## 使い方

イベントまたはステートに **Send Plugin Message** コマンドを追加します:

| メッセージ | 説明 |
|-----------|------|
| `printFiles` | 添付された全 PDF を TCP ポート 9100 経由で `printerIP` へ送信 |

印刷完了時、プラグインは `printPDFsFinishedEvent` を送信します。遷移の Plugin Message イベントトリガーとして使用できます。

## User Variable

| 変数 | 説明 |
|------|------|
| `printerIP` | ネットワークプリンターの IP アドレス |

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `printPDFplugin.brs` | メインプラグインスクリプト |
| `PrintPDF.bpf` | サンプルプレゼンテーション |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
