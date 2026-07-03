# Setup with Publish

> [English version](README.md)

## 概要

プレゼンテーションを公開することでデバイスセットアップを実行するプラグインです。通常、デバイスセットアップにはストレージデバイスの物理挿入が必要ですが、Local File Networking（LFN）および Simple File Networking（SFN）プレイヤーでは、このプラグインによりセットアップファイルのリモート配信が可能になります。

## プラグイン名

```
setup
```

## デバイスセットアップパッケージの作成

1. **Tools > Setup BrightSign Unit** を開く。
2. 必要なデバイス設定を行う。
3. **Create Setup Files** をクリックする。
4. セットアップファイルを PC 上のフォルダに保存する。
5. セットアップファイルを `autorun.zip` という名前で zip 化する。

**重要:** セットアップファイル（`autoplugins.brs`、`brightsign-dumps` 等）は zip の**ルート**に配置し、サブディレクトリ内に入れないこと。

**注意:** 空フォルダは zip 化時に消える場合があります。プラグインがプレイヤー上で必要なフォルダを再作成します。

## インストール手順

1. このフォルダから `setup_plugin.brs` をダウンロードする。
2. 対象プレイヤーへ公開するプレゼンテーションを開く。
3. **File > Presentation Properties > Autorun** を開く。
4. **Add Script Plugin** をクリックし、`setup_plugin.brs` を選択する。
5. プラグインの **Name** を `setup` に設定する。
6. **File > Presentation Properties > Files** で `autorun.zip` を追加する。
7. 通常どおりプレゼンテーションを公開する。

## 使い方

プレイヤーがプレゼンテーションを受信すると、`autorun.zip` 内のファイルでデバイスセットアップを実行し、再起動後に公開されたプレゼンテーションの再生を開始します。

すべての公開方式に対応しています。

## 注意事項

- `autorun.zip` 内に `pool` が含まれない場合、既存の pool フォルダは保持されます。
- 再起動前に `uservariables.db` ファイルが削除されます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `setup_plugin.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
