# BrightAuthor-Plugins

> [English version](README.md)

## このリポジトリについて

このリポジトリは、GitHub 上の公式リポジトリ **[BrightSign/BrightAuthor-Plugins](https://github.com/brightsign/BrightAuthor-Plugins)** をフォークし、**解説用のドキュメントを追加したもの**です。プラグインのソースコード（`.brs` / `.bpf`）は BrightSign 公式サンプルをベースにしており、学習・参照用としてそのまま利用できます。

**このフォークで追加した内容:**

- 各プラグインの **README** を拡充（要件・プラグイン名・コマンド・設定方法など）
- 全プラグインおよびルート一覧の **日本語版 README（README_ja.md）**
- カテゴリ別のプラグイン一覧と簡易説明・リンク

**目的:** 本リポジトリは **学習・勉強用** です。公式サンプルプラグインが何をするものか、BrightAuthor への追加方法、Plugin Message・UDP コマンド・User Variable の使い方を理解しやすくすることを目的としています。BrightSign 公式の製品・サポート対象リポジトリではありません。

最新の公式プラグインコードは [公式リポジトリ（upstream）](https://github.com/brightsign/BrightAuthor-Plugins) を参照してください。正式な技術情報は [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers) を参照してください。

## プラグインについて

各フォルダには、[BrightAuthor](https://www.brightsign.biz/products/brightauthor) の機能を拡張するプラグインファイル（`.brs` または `.bpf`）が含まれています。プラグインは **File > Presentation Properties > Autorun**（ファイル > プレゼンテーションのプロパティ > 自動実行）からプレゼンテーションに追加し、プレイヤー上で実行されます。

## プラグインの使い方

1. 使用するプラグインのフォルダを開き、[README](Blank-Plugin-Template/README_ja.md) で要件・プラグイン名・コマンドを確認する。
2. GitHub からプラグインファイルをダウンロードする：`.brs` ファイルの **Raw** リンクを右クリックし、**リンク先を別名で保存** を選択する。
3. BrightAuthor で **File > Presentation Properties > Autorun** を開く。
4. **Add Script Plugin**（スクリプトプラグインの追加）をクリックし、ダウンロードした `.brs` を選択する。
5. プラグインの **Name**（名前）を、各 README に記載の値と**完全に一致**させる（誤設定では動作しない）。
6. プレゼンテーションをプレイヤーに公開する。

詳細は [BrightSign Plugins and Parsers 公式ドキュメント](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers) を参照してください。

## プラグイン一覧

### 開発

| プラグイン | 説明 |
|-----------|------|
| [Blank-Plugin-Template](Blank-Plugin-Template/README_ja.md) | 新規プラグイン開発用テンプレート |

### メディア再生

| プラグイン | 説明 |
|-----------|------|
| [4K-Image-Playback](4K-Image-Playback/README_ja.md) | SD カード上のフォルダから 4K 静止画をスライドショー再生 |
| [Download-and-Play](Download-and-Play/README_ja.md) | URL から画像をダウンロードして全画面表示 |
| [Framerate-Matcher](Framerate-Matcher/README_ja.md) | 再生中動画のフレームレートに映像出力を動的に同期 |
| [Play-File](Play-File/README_ja.md) | Plugin Message で画像・動画を再生 |
| [Rotate-and-Seek](Rotate-and-Seek/README_ja.md) | 動画の回転・シーク・速度変更・フェード、Ticker ゾーン生成 |
| [Screenshot-and-Playback](Screenshot-and-Playback/README_ja.md) | 定期スクリーンショット保存とメディア再生コマンド |
| [Subtitles-Widget](Subtitles-Widget/README_ja.md) | `.txt` ファイルからタイムコード付き字幕を動画上にオーバーレイ |

### ストリーミング

| プラグイン | 説明 |
|-----------|------|
| [Media-Server](Media-Server/README_ja.md) | HDMI 入力・画面・ファイルを RTSP / マルチキャストで配信 |
| [Media-Server-RTSP](Media-Server-RTSP/README_ja.md) | ポート 8090 の RTSP ファイルストリーミングサーバー |

### ネットワーク制御

| プラグイン | 説明 |
|-----------|------|
| [TCP-Network-Command](TCP-Network-Command/README_ja.md) | TCP で 16 進コマンドを送信（PJLink プロジェクター制御など） |
| [UDP-CR-Command-Sender](UDP-CR-Command-Sender/README_ja.md) | キャリッジリターン（CR）付き UDP 文字列を送信 |
| [UDP-Hex-CR-Command-Sender](UDP-Hex-CR-Command-Sender/README_ja.md) | CR 付き UDP 16 進コマンドを送信 |
| [Telnet-Enable](Telnet-Enable/README_ja.md) | プレイヤーの Telnet を有効化・無効化・再起動 |
| [Pronto-Hex-Transmitter](Pronto-Hex-Transmitter/README_ja.md) | Pronto Hex Code で IR コマンドを送信 |

### UI・ウィジェット

| プラグイン | 説明 |
|-----------|------|
| [Widget-Hide-or-Show](Widget-Hide-or-Show/README_ja.md) | Ticker / Clock ゾーンの表示・非表示を切り替え |
| [Change-Ticker-Separator](Change-Ticker-Separator/README_ja.md) | スクロール Ticker の区切り記号をカスタマイズ |
| [Touch-Audio-Feedback](Touch-Audio-Feedback/README_ja.md) | タッチイベント時に HDMI 経由で音声フィードバックを再生 |
| [Send-User-Variables-To-HTML](Send-User-Variables-To-HTML/README_ja.md) | User Variable の更新を HTML ウィジェットへ送信 |
| [HTMLZoneMessage](HTMLZoneMessage/README_ja.md) | HTML と BrightAuthor 間でゾーンメッセージを送受信 |

### 映像・表示

| プラグイン | 説明 |
|-----------|------|
| [ChromaLuma-Key-Editor](ChromaLuma-Key-Editor/README_ja.md) | 動画ゾーンに Chroma / Luma キーイングを適用 |
| [Set-Video-Mode](Set-Video-Mode/README_ja.md) | Series 4 プレイヤーの VideoMode を動的に変更 |
| [Screenshot-with-URL](Screenshot-with-URL/README_ja.md) | HTTP 経由でプレイヤーのスクリーンショットを取得 |

### クラウド・セットアップ

| プラグイン | 説明 |
|-----------|------|
| [Add-To-Cloud](Add-To-Cloud/README_ja.md) | BrightAuthor Classic プレイヤーを BSN.cloud に登録 |
| [Setup-with-Publish](Setup-with-Publish/README_ja.md) | セットアップ用プレゼンを公開してデバイスをリモート設定 |
| [Publish-Node](Publish-Node/README_ja.md) | プレゼンテーション内の Node.js（chronode）アプリを展開・実行 |
| [Add-Client-Certificates](Add-Client-Certificates/README_ja.md) | リモート HTML 表示用のクライアント証明書をインストール |

### プレゼン管理

| プラグイン | 説明 |
|-----------|------|
| [Restore-Presentation](Restore-Presentation/README_ja.md) | 複数プレゼン構成で前のプレゼンに戻る |
| [Player-Rename-Local-File-Networking](Player-Rename-Local-File-Networking/README_ja.md) | Local File Networking 環境でプレイヤー名を変更 |
| [System-Log-Saver](System-Log-Saver/README_ja.md) | カーネルログをローカルストレージに保存 |

### ユーティリティ

| プラグイン | 説明 |
|-----------|------|
| [PDF-Printer](PDF-Printer/README_ja.md) | TCP ポート 9100 でネットワークプリンタへ PDF を送信 |
| [Variable-Countdown](Variable-Countdown/README_ja.md) | User Variable をタイマー間隔でカウントダウン |

## ライセンス

[LICENSE](LICENSE) を参照してください。
