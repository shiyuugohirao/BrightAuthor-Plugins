# Restore Presentation

> [English version](README.md)

## 概要

複数のリンクされたプレゼンテーション間を切り替える際、前のプレゼンテーションに戻る機能を提供するプラグインです。このプラグインがない場合、3 つ以上のプレゼン群で確実に前のプレゼンに戻るには、複雑な条件式と User Variable が必要になります。

## プラグイン名

```
switch
```

## インストール手順

グループ内の**すべて**のプレゼンテーションに追加します:

1. このフォルダから `Restore_Presentation.brs` をダウンロードする。
2. **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`Restore_Presentation.brs` を選択する。
4. プラグインの **Name** を `switch` に設定する。
5. **File > Presentation Properties > Switch Presentations** でグループ内の他のプレゼンテーションをすべて追加する。各プレゼンテーションで繰り返す。

## 使い方

### 保存（切り替え前）

`switch` プラグインへ Plugin Message を送信:

```
save!<project_name>
```

`<project_name>` を後で復帰するプレゼンテーション名に置き換えます。

### 復帰（前のプレゼンへ戻る）

```
restore
```

### ワークフロー

1. 最初のプレゼンテーションが開始される。
2. Plugin Message `save!<project_name>` が送信される。
3. Switch Presentation コマンドで次のプレゼンテーションへ遷移する。
4. 次のプレゼンテーションが開始される。Plugin Message `restore` で保存した `<project_name>` に戻る。

### UDP コマンド

| コマンド | 説明 |
|---------|------|
| `switch!save!<project_name>` | プレゼンテーション名を保存 |
| `switch!restore` | 保存したプレゼンテーションに復帰 |

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `Restore_Presentation.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
