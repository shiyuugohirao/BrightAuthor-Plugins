# Screenshot with URL

> [English version](README.md)

## 概要

プレイヤー画面のスクリーンショットを取得し、HTTP で提供するプラグインです。プレイヤーのローカル Web サーバー上の URL にアクセスして最新のスナップショットを取得できます。

## プラグイン名

```
Custom
```

## インストール手順

1. このフォルダから `GenerateSnapshotViaHTTP.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`GenerateSnapshotViaHTTP.brs` を選択する。
4. プラグインの **Name** を `Custom` に設定する。

## 使い方

プラグインはポート **8081** で HTTP サーバーを起動します。スクリーンショットの取得:

```
http://<player_ip>:8081/mySnap
```

`<player_ip>` をプレイヤーの IP アドレスに置き換えます（例: `http://192.168.1.78:8081/mySnap`）。

### 動作

1. SD カード上に `mySnap` フォルダがなければ作成する。
2. 現在の映像解像度で JPEG スクリーンショットを取得する。
3. `mySnap/LastSnapshot.jpg` として保存する。
4. HTTP レスポンスで JPEG 画像を返す。

## 設定

スクリプト内のスクリーンショットパラメータ:

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| `filetype` | JPEG | 画像形式 |
| `quality` | 25 | JPEG 品質 |
| `Storage` | SD: | ストレージデバイス |
| HTTP ポート | 8081 | ローカル Web サーバーポート |

## 注意事項

- HTTP サーバーはメイン autorun Web サーバーとは別ポートで動作します。
- スクリーンショットは現在の `roVideoMode` 解像度を使用します。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `GenerateSnapshotViaHTTP.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
