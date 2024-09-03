# signate-rank-fetcher

signate-rank-fetcherは、SIGNATEから特定のクエストの最新ランキングを自動的に取得するPythonツールです。  
このツールはSeleniumを使用してログインプロセスを自動化し、ランキングを取得してCSVファイルとして保存します。

## 機能

- SIGNATEへの自動ログイン
- 指定されたクエストのランキングを取得
- 日付で整理されたCSVファイルとしてランキングを保存

## インストール

1. リポジトリをクローンします：
    ```bash
    git clone https://github.com/chibi5896/signate-rank-fetcher.git
    cd signate-rank-fetcher
    ```

2. 仮想環境を作成してアクティブにする（推奨）：
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
    ```

3. 必要なパッケージをインストールします：
    ```bash
    pip install -r requirements.txt
    ```

4. プロジェクトのルートに `.env` ファイルを作成し、以下の設定について記述します。

    - SIGNATEの認証情報
        - メールアドレス
        - パスワード
    - 取得対象のクエスト
    - 出力ファイルのフォーマット（省略可。デフォルトは`csv`）
    - 出力ファイルのエンコード（省略可。デフォルトは`utf-8`）

    ```plaintext
    SIGNATE_EMAIL=your_email@example.com
    SIGNATE_PASSWORD=your_password
    QUEST_IDS=10002,10005,10006,10060,10079
    OUTPUT_FORMAT=csv  # または 'tsv'
    OUTPUT_ENCODING=shift-jis  # または 'shift-jis', 'utf-16' など
    ```

## 使い方

1. スクリプトを実行して最新のランキングを取得します：
    ```bash
    python main.py
    ```

2. ランキングは `result_csv_files/yyyyMMdd/` ディレクトリに保存され、ファイル名は `quest_{quest_id}_rankings.csv` の形式になります。

3. 取得するクエストを修正したい場合、`.env`ファイル中の`QUEST_IDS`を編集します。
    ```
    QUEST_IDS=10002,10005,10006,10060,10079,10080
    ```

## プロジェクト構成

- `main.py`: ツールを実行するメインスクリプト。
- `signate_ranker.py`: ログインとランキング取得のコアロジックを含む。
- `utils.py`: ディレクトリとファイル管理のユーティリティ関数。
- `requirements.txt`: Pythonの依存関係をリストアップ。

## 貢献

バグを見つけたり、改善の提案があれば、問題を報告したりプルリクエストを送ったりしてください。
