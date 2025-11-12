from fastapi import FastAPI, Query, HTTPException
from typing import List, Dict, Any
from pydantic import BaseModel
from enum import Enum
import json
import os

app = FastAPI(title="Hymn Search API (JSON-based)")

# Enums for Language and Group
class Language(str, Enum):
    ENGLISH = "English"
    SPANISH = "Spanish"
    FRENCH = "French"

class Group(str, Enum):
    YOUTH = "Youth"
    ADULT = "Adult"
    CHILDREN = "Children"

# Hymn model
class Hymn(BaseModel):
    id: int
    title: str
    language: Language
    group: Group
    tunelink: str
    verses: list[str]
    chorus: str
    addedChorus: str

# JSON file path
DB_FILE = "jcli_hymnbook_new.json"

'''
hymn_id = 1
def get_hymns:
    return next((h for h in data["hymns"] if h["id"] == hymn_id), None)
'''

# Load hymns from JSON
def load_hymns():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r",encoding="utf-8") as f:
        data = json.load(f)
        return data.get("hymns", [])
    
def search_hymns(search_term: str) -> List[Dict[str, Any]]:
    """Search hymns by title, chorus, addedChorus, or verses."""
    hymns = load_hymns()
    term = search_term.lower()
    matches = []

    for hymn in hymns:
        # Search in title, chorus, and addedChorus
        if (
            term in hymn.get("title", "").lower()
            or term in hymn.get("chorus", "").lower()
            or term in hymn.get("addedChorus", "").lower()
        ):
            matches.append(hymn)
            continue

        # Search in verses
        verses = hymn.get("verses", [])
        for verse_group in verses:
            # Flatten the list of lines for easier matching
            combined = " ".join(verse_group).lower()
            if term in combined:
                matches.append(hymn)
                break  # Avoid duplicates

    return matches

# Save hymns to JSON
def save_hymns(hymns):
    with open(DB_FILE, "w") as f:
        json.dump(hymns, f, indent=4)

# Convert dict to Hymn object
def dict_to_hymn(data):
    return Hymn(**data)

# 🔍 Read all hymns
@app.get("/hymns")
def get_hymns():
    return load_hymns()

# 🔍 Read hymn by ID
@app.get("/hymns/{hymn_id}")
def get_hymn(hymn_id: int):
    hymns = load_hymns()
    for hymn in hymns:
        if hymn["id"] == hymn_id:
            return hymn
    raise HTTPException(status_code=404, detail="Hymn not found")

@app.get("/filter_data", response_model=List[Dict[str, Any]])
def filter_data(search: str = Query(..., min_length=1, description="Search term")):
    """
    Search hymns in the JSON file where the title, chorus, added chorus,
    or any verse contains the given term (case-insensitive).
    """
    results = search_hymns(search)
    if not results:
        raise HTTPException(status_code=404, detail="No hymns found for your search.")
    return results


# ➕ Create new hymn
@app.post("/hymns")
def create_hymn(hymn: Hymn):
    hymns = load_hymns()
    if any(h["id"] == hymn.id for h in hymns):
        raise HTTPException(status_code=400, detail="Hymn ID already exists")
    hymns.append(hymn.dict())
    save_hymns(hymns)
    return hymn

# ✏️ Update hymn
@app.put("/hymns/{hymn_id}")
def update_hymn(hymn_id: int, updated_hymn: Hymn):
    hymns = load_hymns()
    for i, hymn in enumerate(hymns):
        if hymn["id"] == hymn_id:
            hymns[i] = updated_hymn.dict()
            save_hymns(hymns)
            return updated_hymn
    raise HTTPException(status_code=404, detail="Hymn not found")

# ❌ Delete hymn
@app.delete("/hymns/{hymn_id}")
def delete_hymn(hymn_id: int):
    hymns = load_hymns()
    for i, hymn in enumerate(hymns):
        if hymn["id"] == hymn_id:
            deleted = hymns.pop(i)
            save_hymns(hymns)
            return deleted
    raise HTTPException(status_code=404, detail="Hymn not found")

