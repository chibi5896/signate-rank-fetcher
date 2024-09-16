import os
import shutil
import pandas as pd
from signate_scraper.utils import detect_encoding

def move_old_file(base_dir, old_file):
    """古いファイルを 'old' ディレクトリに移動"""
    old_dir = os.path.join(base_dir, 'old')
    os.makedirs(old_dir, exist_ok=True)
    shutil.move(os.path.join(base_dir, old_file), os.path.join(old_dir, old_file))

def check_and_move_old_files(base_dir, quest_id, output_format, new_df, compare_dataframes):
    """過去ファイルをチェックして、更新があれば移動し、差分を分析"""
    existing_files = [f for f in os.listdir(base_dir) if f.startswith(f'quest_{quest_id}_rankings_') and f.endswith(output_format)]
    
    for old_file in existing_files:
        old_file_path = os.path.join(base_dir, old_file)
        detected_encoding = detect_encoding(old_file_path)
        old_df = pd.read_csv(old_file_path, encoding=detected_encoding, sep='\t' if output_format == 'tsv' else ',')
        
        # 差分があれば古いファイルを移動し、Trueを返す
        if compare_dataframes(old_df, new_df):
            move_old_file(base_dir, old_file)
            return True
        else:
            print(f'Quest {quest_id} のランキングに更新はありません。')
            return False
    
    # 差分がないか、初めてのファイルの場合
    return True
