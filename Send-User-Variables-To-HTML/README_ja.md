# Send User Variables to HTML

> [English version](README.md)

## 概要

`USER_VARIABLE_UPDATED` イベントを監視し、すべての User Variable を `PostJSMessage` で HTML ウィジェットへ送信するプラグインです。ポート 8008 のローカル Web サーバーまたは BrightSign iPad アプリから変数を更新できます。

## 要件

- 最小ファームウェア: 6.2.*

## プラグイン名

```
sendUserVars
```

## インストール手順

1. このフォルダから `sendUserVars.brs` をダウンロードする。
2. BrightAuthor で `sendUserVariablesToHtml.bpf` を開き、不足ファイルをインポートする。
3. **File > Presentation Properties > Autorun** を開く。
4. **Add Script Plugin** をクリックし、`sendUserVars.brs` を選択する。
5. プラグインの **Name** を `sendUserVars` に設定する。
6. プレゼンテーションを公開する。

## 使い方

1. プレゼンテーションをプレイヤーに公開する。
2. BrightSign iPad アプリでローカル Web サーバーにアクセスするか、ブラウザで `http://<player_ip>:8008/` を開く。
3. Web インターフェースで User Variable を変更する。
4. 更新された値が HTML ウィジェットへ送信され、画面上に表示される。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `sendUserVars.brs` | メインプラグインスクリプト |
| `sendUserVariablesToHtml.bpf` | サンプルプレゼンテーション |
| `index.html` | サンプル HTML ページ |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
