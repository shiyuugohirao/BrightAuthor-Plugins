# Variable Countdown

> [English version](README.md)

## 概要

カウントダウンコマンドを受信するたびに User Variable を 1 減算するプラグインです。Live Text タイマーや User Variable 駆動のカウントダウン表示に利用できます。

## プラグイン名

```
countdown
```

## インストール手順

1. このフォルダから `var_countdown.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`var_countdown.brs` を選択する。
4. プラグインの **Name** を `countdown` に設定する。
5. **File > Presentation Properties > Variables** で整数のデフォルト値を持つ User Variable を作成する。

## 使い方

次の形式で Plugin Message または UDP コマンド（ポート **555**）を送信します:

```
Countdown!<変数名>
```

コマンドごとに変数が 1 減算されます（最小値 0）。更新後の値は `SetCurrentValue` で書き戻されます。

### 使用例

User Variable `timer` の値が `60` の場合:

```
Countdown!timer
```

結果: `timer` は `59` になります。

## 注意事項

- BrightAuthor のイベントで一定間隔（例: 1 秒ごと）にカウントダウンコマンドをトリガーしてください。
- コマンド内の変数名は User Variable 名と完全に一致する必要があります。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `var_countdown.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
