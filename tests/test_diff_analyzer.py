import sys
import os
# プロジェクトのルートディレクトリを PYTHONPATH に追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
                
import pandas as pd
import numpy as np
from signate_scraper.diff_analyzer import compare_dataframes

# テストデータの準備
def create_test_data():
    # 古いデータフレーム
    old_data = {
        'ニックネーム': ['abc', 'xyz', '合格ライン', '五苓'],
        '組織順位': [10, 490, '合格ライン', 5],
        'ベストスコア': [6.0, 6.38, 6.3, 6.38671],
        '総合順位': [50, 490, '合格ライン', 5],
        '投稿件数': [10, 20, np.nan, 3],
        '最終投稿日時': ['2023-08-01', '2023-08-02', np.nan, '2023-08-01']
    }

    # 新しいデータフレーム
    new_data = {
        'ニックネーム': ['abc', 'xyz', '合格ライン', '五苓', '新規ユーザ'],
        '組織順位': [11, 491, '合格ライン', 5, 300],
        'ベストスコア': [6.0, 6.38, 6.3, 6.38611, 5.0],
        '総合順位': [50, 491, '合格ライン', 5, 300],
        '投稿件数': [10, 21, np.nan, 3, 1],
        '最終投稿日時': ['2023-08-01', '2023-08-03', np.nan, '2023-08-01', '2023-08-05']
    }

    # DataFrameに変換
    old_df = pd.DataFrame(old_data)
    new_df = pd.DataFrame(new_data)
    
    return old_df, new_df

# テストケースの実行
def test_compare_dataframes():
    old_df, new_df = create_test_data()
    
    # 差分があるか確認
    result = compare_dataframes(old_df, new_df)
    
    # 結果を確認
    assert result == True, "テスト失敗: 差分があるはずです。"

# テストの実行
test_compare_dataframes()
