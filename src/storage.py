import json
from pathlib import Path
from typing import  List, Dict, Optional

DB_PATH = Path(__file__).parent / "db.json"

def load_data() -> List[Dict]:
    if not DB_PATH.exists():
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data,list):
                return data
            return []
        except json.JSONDecodeError:
            return []

def save_data(data:List[Dict]) -> None:
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

def get_next_id(data: List[Dict]) -> int:
    if not data:
        return 1
    return max(item.get("id", 0) for item in data) + 1

def find_by_id(data:List[Dict], id_:int) -> Optional[Dict]:
    for item in data:
        if item["id"] == id_:
            return item
    return None


