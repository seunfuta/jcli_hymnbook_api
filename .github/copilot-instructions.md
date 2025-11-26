# JCLI Hymnbook API Instructions

This is a FastAPI-based REST API for managing and querying a bilingual (English/Yoruba) hymnbook database for JCLI (Jesus Christ Love International).

## Project Structure

- `main.py`: Core API implementation with FastAPI endpoints and data models
- `*.json`: Individual hymn data files containing song details
- `*.txt`: Raw hymn data files and hymn ranges
## JCLI Hymnbook — Agent instructions (concise)

This repo is a small FastAPI backend (single-file `main.py`) that serves a bilingual hymnbook (English/Yoruba) and a simple React frontend in `react_frontend/`.

Key files and places to look
- `main.py` — backend: Pydantic `Hymn`, `Language` and `Group` enums, in-memory test data and JSON loader (`DB_FILE = jcli_hymnbook_new.json`). See filtering endpoints `/filters` and `/filterx` for examples of nested-array searching.
- `jcli_hymnbook_new.json` and many `*.json`/`*.txt` files — canonical hymn data. Notebooks `jcli_hymnbook_api.ipynb` and `hymnbook_jsonify.ipynb` are used for data processing.
- `react_frontend/src/App.jsx` — frontend fetches hymns from `http://127.0.0.1:8000/hymns/{id}` and expects fields: `id, title, language, group, tunelink, verses, chorus, addedChorus`.
- `test_server.py` — example smoke tests (simple requests against localhost:8000).

Quick developer workflows
- Start backend (dev):
  - Ensure Python env activated, then run: `uvicorn main:app --reload` (default port 8000).
- Start frontend (dev):
  - From `react_frontend/`: `npm install` (once), then `npm run dev` (Vite). Frontend runs on Vite's port (usually 5173).
- Run simple API check: `python test_server.py` (it performs requests against `http://localhost:8000`).

Data shapes & repo-specific patterns (be concrete)
- Hymn entries are often nested: `verses` is an array of verses where each verse can be an array of lines. `chorus` and `addedChorus` appear as either string or array-of-strings in different files — code and frontend accept both. Be defensive when reading/writing.
- `tunelink` is sometimes a string and sometimes an array of URLs. Prefer normalizing to a single URL string when adding new hymns, or document the array explicitly.
- Group names must match the `groups` list / `Group` enum in `main.py`. Use exact casing when adding new group values.
- IDs: hymns appear in bilingual pairs (same numeric id for EN and YO versions in some datasets). Keep IDs unique per entry when needed and preserve bilingual mapping where present.

Small but important notes for agents
- The backend does not add CORS middleware by default; if you run the React frontend in the browser (Vite) and fetch `http://127.0.0.1:8000`, you'll likely need to add FastAPI's `CORSMiddleware` in `main.py`.
- Many alternate endpoints and commented examples exist in `main.py` — review before changing behavior to avoid removing intended examples.
- Tests are informal (requests in `test_server.py`). Add unit tests if changing core filter logic.

When adding endpoints or modifying data:
- Use Pydantic models and `Query()` where appropriate (follow existing `/filters` signature patterns).
- Update `jcli_hymnbook_new.json` (or source JSON files) and run the notebooks if you need to re-generate the canonical JSON.
- Add or update a small smoke test in `test_server.py` showing the new behavior.

If anything here is unclear or you want more examples (e.g., exact Group enum list or a sample normalized hymn JSON), tell me which area to expand and I will iterate.