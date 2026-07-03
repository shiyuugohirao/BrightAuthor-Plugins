# Pronto Hex Transmitter

> [English version](README.md)

## 概要

[Pronto Hex Code](http://www.remotecentral.com/features/irdisp2.htm)（PHC）プロトコルで IR コマンドを送信するプラグインです。BrightAuthor プレゼンテーションから Plugin Message または UDP でコマンドをトリガーできます。

**注意:** BrightAuthor 3.8.0.27 以降では、**Send IR Remote (Pronto)** コマンドで PHC IR コマンドがネイティブ対応されています。3.8.0.27 以降を使用している場合、このプラグインは不要な場合があります。

## 要件

- ファームウェア 4.7.96 以降（IR 送受信対応）
- IR 出力対応プレイヤー

## プラグイン名

```
sendir
```

## インストール手順

1. お使いの機器の PHC コードで `sendir.brs` を編集する（下記「設定」を参照）。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`sendir.brs` を選択する。
4. プラグインの **Name** を `sendir` に設定する。

## 使い方

### Plugin Message

`sendir` プラグインへ **Send Plugin Message** を送信し、定義済みコマンド名を指定します:

| コマンド | デフォルト動作 |
|---------|---------------|
| `tvon` | テレビ電源オン |
| `tvoff` | テレビ電源オフ |
| `prjon` | プロジェクター電源オン |
| `prjoff` | プロジェクター電源オフ |

### UDP コマンド

ポート **21000** へ次の形式で UDP メッセージを送信します:

```
sendir!<コマンド>
```

使用例:

```
sendir!tvon
sendir!mute
```

## 設定

### PHC コードの編集

1. [Remote Central IR Database](http://www.remotecentral.com/cgi-bin/codes/) で機器の PHC コードを検索する。
2. テキストエディタで `sendir.brs` を開く。
3. `newSendIR` 関数内の `s.tvoff`、`s.tvon`、`s.prjoff`、`s.prjon` の値を置き換える。
4. 各コードの末尾 4 桁の 16 進数を `0000` に変更する。

**例:** Panasonic のコードは `0ac2` で終わることが多いですが、プラグインに追加する際は `0000` に変更してください。

### カスタムコマンドの追加

次の形式で行を追加します:

```brightscript
s.mute = "0000 0071 ..."
```

Plugin Message で `mute`、または UDP で `sendir!mute` としてトリガーできます。

## 注意事項

- プレイヤーは IR 出力（`roIRRemote` オブジェクト）に対応している必要があります。
- `sendir` で始まる UDP コマンドはポート 21000 で処理されます。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `sendir.brs` | メインプラグインスクリプト |

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
