import chardet

def detect_encoding(file_path):
    """ファイルのエンコーディングを検出する"""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']
