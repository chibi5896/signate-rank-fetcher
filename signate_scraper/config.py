import os
from dotenv import load_dotenv

load_dotenv()  # .envファイルを読み込む

# ログイン情報
SIGNATE_EMAIL = os.getenv('SIGNATE_EMAIL')
SIGNATE_PASSWORD = os.getenv('SIGNATE_PASSWORD')

# 5つのクエストのIDリスト
quest_ids_str = os.getenv('QUEST_IDS', '')
QUEST_IDS = list(map(int, quest_ids_str.split(',')))

# 出力時の設定
OUTPUT_FORMAT = os.getenv('OUTPUT_FORMAT', 'csv')
OUTPUT_ENCODING = os.getenv('OUTPUT_ENCODING', 'utf-8')

# GoogleChromeをヘッドレスモードで実行するか
IS_HEADLESS = True