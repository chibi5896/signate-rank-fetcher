import os
import pandas as pd
from datetime import datetime

def save_ranking_to_csv(df, quest_id):
    # 実行日ごとのフォルダ名を作成
    date_str = datetime.now().strftime('%Y%m%d')
    dir_path = os.path.join('result_csv_files', date_str)

    # フォルダが存在しない場合は作成
    os.makedirs(dir_path, exist_ok=True)

    # 保存するファイルパスを指定
    file_path = os.path.join(dir_path, f'quest_{quest_id}_rankings.csv')

    # DataFrameをCSVファイルとして保存
    df.to_csv(file_path, index=False)
    print(f'Quest {quest_id} のランキングを {file_path} に保存しました。')
