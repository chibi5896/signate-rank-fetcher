from signate_scraper.scraper import SignateScraper
from signate_scraper.config import *
from signate_scraper.utils import save_ranking_to_csv
import pandas as pd

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
            save_ranking_to_csv(df, quest_id)
    
    finally:
        # WebDriverを終了
        scraper.close()

if __name__ == '__main__':
        main()