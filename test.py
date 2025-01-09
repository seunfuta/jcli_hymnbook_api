from fastapi import FastAPI, Query
from typing import List, Optional
import json

# Define the FastAPI app
app = FastAPI()

# Sample dataset of JSON objects
dataset = [
    {"name": "John", "age": 30, "skills": ["Python", "Java", "C++"]},
    {"name": "Jane", "age": 25, "skills": ["Python", "JavaScript"]},
    {"name": "Alice", "age": 28, "skills": ["Python", "Ruby", "Go"]},
    {"name": "Bob", "age": 35, "skills": ["Java", "C++"]},
]

# Define a route that handles filtering of the dataset
@app.get("/filter")
async def filter_data(
    name: Optional[str] = Query(None, min_length=3, max_length=50),
    age: Optional[int] = Query(None, gt=0),
    skill: Optional[str] = Query(None)
):
    # Filter the dataset based on query parameters
    filtered_data = dataset

    if name:
        filtered_data = [item for item in filtered_data if name.lower() in item["name"].lower()]
    if age:
        filtered_data = [item for item in filtered_data if item["age"] == age]
    if skill:
        filtered_data = [item for item in filtered_data if skill.lower() in [s.lower() for s in item["skills"]]]

    return filtered_data