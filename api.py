from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from JSON
with open("data.json", "r") as file:
    students = json.load(file)

# Create an API endpoint
@app.get("/api")
def get_marks(name: list[str] = []):
    marks_list = [student["marks"] for student in students if student["name"] in name]
    return {"marks": marks_list}
