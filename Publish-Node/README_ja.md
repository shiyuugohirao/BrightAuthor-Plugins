# Publish Node

> [English version](README.md)

## 概要

BrightAuthor プレゼンテーション内から chronode（Node.js）アプリケーションを展開・実行するプラグインです。Chronode アプリは BrightSign プレイヤー上で Electron アプリと同様に動作します。

## 要件

- 最小ファームウェア: 8.0.*

## プラグイン名

```
unzipNode
```

## インストール手順

1. このフォルダから `unzipNode.brs` をダウンロードする。
2. Node.js アプリケーションを `node.zip` としてパッケージ化する。
3. **File > Presentation Properties > Autorun** を開く。
4. **Add Script Plugin** をクリックし、`unzipNode.brs` を選択する。
5. プラグインの **Name** を `unzipNode` に設定する。
6. **File > Presentation Properties > Files** で `node.zip` を追加する。

## 使い方

プレゼンテーション開始時に、プラグインが `node.zip` を展開し chronode アプリケーションを起動します。

## 注意事項

- webpack 等のバンドラーを使用してアプリケーションを小さく保つことを推奨します。`node_modules` を単一スクリプトにバンドルすると zip/展開が大幅に高速化されます。
- chronode の詳細は [BrightSign Node.js ドキュメント](https://docs.brightsign.biz/display/DOC/Node.js) を参照してください。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `unzipNode.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Node.js ドキュメント](https://docs.brightsign.biz/display/DOC/Node.js)
- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
