import os
import pandas as pd
from datetime import datetime
import shutil
import chardet

def detect_encoding(file_path):
    """ファイルのエンコーディングを検出する"""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def move_old_files(base_dir, quest_id, output_format, df):
    """過去ファイルをチェックして、更新があれば移動"""
    existing_files = [f for f in os.listdir(base_dir) if f.startswith(f'quest_{quest_id}_rankings_') and f.endswith(output_format)]
    
    for old_file in existing_files:
        old_file_path = os.path.join(base_dir, old_file)
        detected_encoding = detect_encoding(old_file_path)
        old_df = pd.read_csv(old_file_path, encoding=detected_encoding, sep='\t' if output_format == 'tsv' else ',')
        if not df.equals(old_df):
            old_dir = os.path.join(base_dir, 'old')
            os.makedirs(old_dir, exist_ok=True)
            shutil.move(old_file_path, os.path.join(old_dir, old_file))
        else:
            print(f'Quest {quest_id} のランキングに更新はありません。')
            return False
    return True

def save_ranking_to_csv(df, quest_id, output_format, output_encoding):
    # 現在の日付を取得
    date_str = datetime.now().strftime('%Y%m%d')
    
    # ベースディレクトリ
    base_dir = 'result_csv_files'
    os.makedirs(base_dir, exist_ok=True)
    
    # 出力ファイル名を設定
    file_name = f'quest_{quest_id}_rankings_{date_str}.{output_format}'
    file_path = os.path.join(base_dir, file_name)
    
    # 過去ファイルの移動処理
    if move_old_files(base_dir, quest_id, output_format, df):
        # 差分がある場合のみ、新しいファイルを保存
        df.to_csv(file_path, index=False, encoding=output_encoding, sep='\t' if output_format == 'tsv' else ',')
        print(f'Quest {quest_id} のランキングを {file_path} に保存しました。')