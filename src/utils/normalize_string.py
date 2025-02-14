import unicodedata

def normalize_string(s: str) -> str:
    normalized = unicodedata.normalize('NFD', s)
    normalized = normalized.encode('ASCII', 'ignore').decode('utf-8')
    return normalized.replace(' ', '').lower()