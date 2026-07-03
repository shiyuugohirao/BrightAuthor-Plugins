# System Log Saver

> [English version](README.md)

## 概要

詳細なカーネルシステムログをプレイヤーのローカルストレージに保存するプラグインです。標準のセットアップログより多くのデバッグ情報を含みます。Diagnostic Web Server が有効な場合、SD カードを取り外さずにリモートでログを取得できます。

ログファイル名には `mmddyyyy` 形式の日付プレフィックスが付きます（例: `kernel_log.txt`）。日ごとに新しいファイルが作成され、同一日內はパーサー実行のたびに同じファイルが上書きされます。

**警告:** 恒久的な運用には推奨しません。ログファイルが予測不能な速度でローカルストレージを満杯にします。実験室・テスト環境向けです。

## インストール手順（Data Feed パーサー）

このプラグインは Autorun スクリプトではなく、**Data Feed パーサー**として追加します。

1. このフォルダから `klog.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Data Feeds** を開く。
3. **Add Data Feed** をクリックする。
4. **Feed name** を入力する。
5. **Feed Specification** に `file:///autoplugins.brs` を入力する。
   - プレースホルダー URL です。動作する Data Feed は不要です。
6. **Update Interval**（ログ保存間隔）を選択する。
7. **Browse** で `klog.brs` を選択する。
8. **Parser Function Name** に `klog` を入力する。
9. **OK** をクリックする。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `klog.brs` | パーサースクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
