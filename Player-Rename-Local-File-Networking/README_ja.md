# Player Rename (Local File Networking)

> [English version](README.md)

## 概要

Local File Networking（LFN）環境でプレイヤー名を変更するプラグインです。ネットワークレジストリへ書き込み、起動時の User Variable または実行時の Plugin Message / UDP で新しい名前を設定できます。

## プラグイン名

```
lfnrename
```

## インストール手順

1. このフォルダから `LFNRename` をダウンロードする（拡張子なし）。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`LFNRename` を選択する。
4. プラグインの **Name** を `lfnrename` に設定する。

## 使い方

### User Variable（起動時）

**File > Presentation Properties > Variables** で `lname` という User Variable を作成します。プラグイン初期化時に `lname` が現在のレジストリ名と異なる場合、プレイヤー名を変更して再起動します。

### Plugin Message / UDP（ポート 555）

```
lfnrename!<新しい名前>
```

| コマンド | 説明 |
|---------|------|
| `lfnrename!<name>` | プレイヤー名を `<name>` に設定して再起動 |
| `lfnrename!debug` | デバッグログを有効化 |
| `lfnrename!reboot` | プレイヤーを再起動 |

## 注意事項

- `networking` レジストリセクションの `un` キーへ書き込みます。
- 名前が変更されるとプレイヤーは自動的に再起動します。
- 新しい名前が現在の名前と同じ場合は変更されません。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `LFNRename` | メインプラグインスクリプト（拡張子なし） |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
