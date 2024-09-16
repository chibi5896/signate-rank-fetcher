import json

def remove_empty_lists(d):
    """辞書から空のリストを持つキーを削除する"""
    return {k: v for k, v in d.items() if v}

def analyze_differences(old_df, new_df):
    """古いDataFrameと新しいDataFrameを比較して、変動の種類を分析"""
    changes = {
        '既存ユーザ': [],
        '新規ユーザ': []
    }

    # 行単位で比較
    for index, new_row in new_df.iterrows():
        if new_row['ニックネーム'] == "合格ライン":
            # ニックネームが "合格ライン" の場合、次の行へスキップ
            continue

        old_row = old_df.loc[old_df['ニックネーム'] == new_row['ニックネーム']]
        
        if not old_row.empty:
            old_row = old_row.iloc[0]  # 対応する行を取得
            
            if old_row['ベストスコア'] != new_row['ベストスコア']:
                changes['既存ユーザ'].append({
                    'ニックネーム': new_row['ニックネーム'],
                    'new': {
                        '組織順位': str(new_row['組織順位']),
                        'ベストスコア': str(new_row['ベストスコア']),
                        '投稿件数': str(new_row['投稿件数']),
                    },
                    'old':{
                        '組織順位': str(old_row['組織順位']),
                        'ベストスコア': str(old_row['ベストスコア']),
                        '投稿件数': str(old_row['投稿件数'])
                    }
                })

        else:
            changes['新規ユーザ'].append(new_row.to_dict())

    return remove_empty_lists(changes)

def compare_dataframes(old_df, new_df):
    """古いDataFrameと新しいDataFrameを比較して差分を返す"""
    differences = analyze_differences(old_df, new_df)
    
    # 差分があれば出力
    if any(differences.values()):  # いずれかのリストに差分があれば
        print(f'差分が見つかりました:')
        print(json.dumps(differences, ensure_ascii=False, indent=2))
        return True
    return False
