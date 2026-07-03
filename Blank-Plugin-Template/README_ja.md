# Blank Plugin Template

> [English version](README.md)

## 概要

新規 BrightAuthor プラグイン開発用のスターターテンプレートです。初期化、イベント処理、Plugin Message の受信といった基本的なプラグイン構造を示しています。

## 要件

- 最小ファームウェア: 1.0.0

## プラグイン名

```
blank
```

## インストール手順

1. このフォルダから `blankPlugin.brs` をダウンロードする。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`blankPlugin.brs` を選択する。
4. プラグインの **Name** を `blank` に設定する。

## 使い方

### はじめに

1. `blankPlugin.brs` をコピーし、プラグイン用にリネームする。
2. ファイル内の文字列 `blank` を一括置換する（関数名、プラグイン名、オブジェクト名）。
3. `ProcessEvent` ハンドラ内に独自のロジックを実装する。

### Plugin Message

テンプレートは `blank` 宛の Plugin Message を受信します。受信時は `true` を返し、他のハンドラによる処理を防ぎます。

他のプラグインへメッセージを送信する場合は、スクリプト内の `PostMessage` ブロックのコメントを解除して修正してください。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `blankPlugin.brs` | テンプレートプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
