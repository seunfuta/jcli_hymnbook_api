# JCLI Hymnbook API Instructions

This is a FastAPI-based REST API for managing and querying a bilingual (English/Yoruba) hymnbook database for JCLI (Jesus Christ Love International).

## Project Structure

- `main.py`: Core API implementation with FastAPI endpoints and data models
- `*.json`: Individual hymn data files containing song details
- `*.txt`: Raw hymn data files and hymn ranges
- `*.csv`: Group categorization data
- `jcli_hymnbook_api.ipynb`: Jupyter notebook for data processing
- `test_server.py`: API endpoint testing

## Data Model

Hymns are structured as JSON objects with the following schema:
```json
{
    "id": integer,
    "title": string,
    "language": "english" | "yoruba",
    "group": string (from predefined groups),
    "tunelink": string (URL),
    "verses": array[array[string]],
    "chorus": array[string],
    "addedChorus": array[string]
}
```

## Key Components

1. **FastAPI Endpoints**:
   - `/`: List all hymns
   - `/hymns/{hymn_id}`: Get hymn by ID
   - `/hymns/`: Query hymns by parameters
   - `/filters`: Advanced filtering with validation
   - `/filterx`: Extended filtering with nested array search

2. **Data Models**:
   - `Language` enum: YORUBA, ENGLISH
   - `Group` enum: 68 predefined hymn categories
   - `Hymn` Pydantic model: Core data structure

## Development Guidelines

1. **Adding New Endpoints**:
   - Follow existing parameter validation patterns using Query()
   - Include appropriate error handling (404 for missing resources)
   - Add test cases in `test_server.py`

2. **Data Processing**:
   - Use `jcli_hymnbook_api.ipynb` for data transformation tasks
   - Maintain bilingual parallel between English and Yoruba hymns
   - Preserve group categorization as defined in CSV files

3. **Testing**:
   ```bash
   # Start the server
   uvicorn main:app --reload
   
   # Test endpoints
   python test_server.py
   ```

4. **Data Validation**:
   - Ensure hymn IDs are unique
   - Validate tune links are valid URLs
   - Verify group names match predefined categories

## Common Tasks

1. **Adding New Hymns**:
   - Create JSON entry following schema
   - Add both English and Yoruba versions
   - Update group categorization if needed

2. **Modifying Endpoints**:
   - Reference existing filter implementations for nested array searches
   - Use type hints and Pydantic models consistently
   - Maintain backward compatibility with existing queries