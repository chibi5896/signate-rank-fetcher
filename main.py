import os
import pandas as pd
from datetime import datetime
from signate_scraper.scraper import SignateScraper
from signate_scraper.config import *
from signate_scraper.file_utils import check_and_move_old_files
from signate_scraper.diff_analyzer import compare_dataframes

def save_ranking_to_csv(df, quest_id, output_format, output_encoding):
    """ランキングをCSV/TSVに保存"""
    # 現在の日付を取得
    date_str = datetime.now().strftime('%Y%m%d')
    
    # ベースディレクトリ
    base_dir = 'result_csv_files'
    os.makedirs(base_dir, exist_ok=True)
    
    # 出力ファイル名を設定
    file_name = f'quest_{quest_id}_rankings_{date_str}.{output_format}'
    file_path = os.path.join(base_dir, file_name)
    
    # 過去ファイルの移動処理と差分チェック
    if check_and_move_old_files(base_dir, quest_id, output_format, df, compare_dataframes):
        # 差分がある場合のみ、新しいファイルを保存
        df.to_csv(file_path, index=False, encoding=output_encoding, sep='\t' if output_format == 'tsv' else ',')
        print(f'Quest {quest_id} のランキングを {file_path} に保存しました。')

def main():
    # SignateScraperインスタンスを初期化
    scraper = SignateScraper(IS_HEADLESS)
    
    try:
        # ログイン
        scraper.login(SIGNATE_EMAIL, SIGNATE_PASSWORD)
        
        # クエストごとのランキングを取得
        all_rankings = {}
        for quest_id in QUEST_IDS:
            print(f'Fetching rankings for Competition ID: {quest_id}')
            df = scraper.get_latest_rank(quest_id)
            all_rankings[quest_id] = df
            print(f'Quest {quest_id} - 最新の順位を取得しました。')
        
        # 例として、各クエストのDataFrameをCSVとして保存
        for quest_id, df in all_rankings.items():
            save_ranking_to_csv(df, quest_id, OUTPUT_FORMAT, OUTPUT_ENCODING)
    
    finally:
        # WebDriverを終了
        scraper.close()

if __name__ == '__main__':
        main()