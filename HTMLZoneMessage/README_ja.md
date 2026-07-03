# HTML Zone Message

> [English version](README.md)

## 概要

HTML ウィジェットと BrightAuthor のゾーンメッセージ間で双方向通信を行うプラグインです。BrightAuthor から送られたゾーンメッセージは `PostJSMessage` で HTML ウィジェットへ転送され、HTML ページからのメッセージはプレゼンテーションへゾーンメッセージとして戻せます。

## 要件

- 最小ファームウェア: 1.0.0
- HTML ウィジェットゾーンを含むプレゼンテーション

## プラグイン名

**File > Presentation Properties > Autorun**（ファイル > プレゼンテーションのプロパティ > 自動実行）で追加する際、プラグインの **Name** を次の値に設定してください:

```
htmlZoneMessage
```

## インストール手順

1. このフォルダから `htmlZoneMessage.brs` をダウンロードする（**Raw** を右クリックし **リンク先を別名で保存**）。
2. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
3. **Add Script Plugin** をクリックし、`htmlZoneMessage.brs` を選択する。
4. プラグインの **Name** を `htmlZoneMessage` に設定する。
5. 必要に応じてサンプルの HTML および BPF ファイルをプレゼンテーションに含める。

## 使い方

### BrightAuthor → HTML

**Send Zone Message**（ゾーンメッセージの送信）イベントが発生すると、プラグインがメッセージパラメータを HTML ウィジェットへ転送します:

```
PostJSMessage({ zoneMessage: <イベントパラメータ> })
```

HTML ページ側で JavaScript によりこのメッセージを受信する処理を実装してください。

### HTML → BrightAuthor

HTML ウィジェットが `button` フィールドを含むメッセージを送信すると、プラグインがゾーンメッセージをプレゼンテーションへ投稿します:

```javascript
// 例: HTML からゾーンメッセージをトリガーするメッセージ
{ button: "myParameter" }
```

これにより `eventParameter` が `myParameter` に設定された `SEND_ZONE_MESSAGE` イベントが発生します。

### Plugin Message

`htmlZoneMessage` 宛の Plugin Message を受け付けます。カスタムメッセージの処理はスクリプト内のハンドラを拡張して実装してください。

## 設定

プラグインはプレゼンテーション内の最初の HTML ウィジェット（ゾーン HSM の `loadingHtmlWidget`）を自動検出します。1 つのプラグインインスタンスで対応できる HTML ウィジェットは 1 つのみです。

## 関連ファイル

| ファイル | 説明 |
|---------|------|
| `htmlZoneMessage.brs` | メインプラグインスクリプト |
| `SendAndReceiveZoneMessagesInHTML.bpf` | サンプル BrightAuthor プレゼンテーション |
| `HTMLSite.html` | サンプル HTML ページ |
| `html/` | サンプルファイルのコピー |

## 注意事項

- イベント受信時にデバッグ出力がシリアルコンソールへ出力されます。
- HTML ページで `PostJSMessage` のコールバック処理と、期待される形式でのウィジェットイベント送信を実装してください。

## 参考リンク

- [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
