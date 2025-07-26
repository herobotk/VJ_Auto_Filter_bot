import os

def get_excluded_ids():
    raw = os.getenv("GROUP_EXCLUDED_IDS", "")
    # comma ya space separated
    return [int(x) for x in raw.replace(",", " ").split() if x.strip().isdigit()]

def is_excluded(id):
    return id in get_excluded_ids()
