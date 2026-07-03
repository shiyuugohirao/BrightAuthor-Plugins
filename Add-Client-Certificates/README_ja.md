# Add Client Certificates

> [English version](README.md)

## 概要

相互 TLS 認証が必要なリモート HTML コンテンツ用に、プレイヤーへクライアント証明書をインストールするプラグインです。プラグイン起動時に User Variable から証明書を読み込みます。

## プラグイン名

```
keystore
```

## インストール手順

1. このフォルダから `keystore.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`keystore.brs` を選択する。
4. プラグインの **Name** を `keystore` に設定する。
5. 証明書ファイルをプレゼンテーションのアセットプールに追加する。
6. `cert` という User Variable を作成し、証明書ファイル名をデフォルト値に設定する。

## 使い方

初期化時にプラグインは次を実行します:

1. `cert` User Variable から証明書ファイル名を読み取る。
2. プレゼンテーションのアセットプール（またはルートパス）でファイルを検索する。
3. プレイヤーのキーストアに証明書を追加する。

Plugin Message で `keystore!reload` を送信すると、再起動なしで証明書の再チェック・インストールが可能です。

## User Variable

| 変数 | 説明 |
|------|------|
| `cert` | アセットプール内のクライアント証明書ファイル名 |

## 注意事項

- プレイヤー再起動後は、証明書を再インストールするためにプラグインを再実行する必要があります。
- 公開前に証明書ファイルをプレゼンテーションに含めてください。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `keystore.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
