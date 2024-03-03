from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
import json
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="People's FastAPI App")
app.mount("/", StaticFiles(directory="ui", html=True), name="index.html")

db = './db/people.json'
    
class Person(BaseModel):
    id: Optional[int] = None
    name: str
    age: int
    gender: str

def get_people():
    with open(db, 'r') as f:
        people = json.load(f)
        return people

@app.get('/people/{p_id}')
def get_person(p_id: int):
    people = get_people()
    person = [p for p in people if p['id'] == p_id]
    return person[0] if len(person) > 0 else {}

@app.get('/search')
def search_person(age: Optional[int] = Query(None, title="Age", description="Age to search"), 
                  name: Optional[str] = Query(None, title="Name", description="Name to search")):
    people = get_people()
    people1 = [p for p in people if p['age'] == age]
    
    if name is None:
        if age is None:
            return people
        else:
            return people1
    else:
        people2 = [p for p in people if name.lower() in p['name'].lower()]
        if age is None:
            return people2
        else:
            combined = [p for p in people1 if p in people2]
            return combined

@app.get('/people')
def get_all_people():
    current_records = get_people()
    return current_records

def get_total_people():
    # Read the JSON file
    data = get_people()

    # Count the number of objects
    num_objects = len(data)
    print(f"Total objects in the JSON file: {num_objects}")
    return(num_objects)

@app.post('/people/add/{}')
def post_person(name: str, age: int, gender: str):
    # Read the existing JSON file
    existing_data = get_people()

    # Add a new record to the dictionary
    new_id = get_total_people() + 1
    new_record = {
        'id': new_id,
        'age': age,
        'gender': gender.lower(),
        'name': name,
    }
    existing_data.append(new_record)
    
    # Write the updated data back to the file
    with open(db, mode='w') as f:
        json.dump(existing_data, f, indent=4)

    return(f"{name} with id {new_id} was added successfully")

@app.delete('/people/remove/{id}')
def delete_person(id: int):
    data = get_people()
    data[:] = [item for item in data if item['id'] != id]
    
    # Write the updated data back to the file
    with open(db, mode='w') as f:
        json.dump(data, f, indent=4)

    return(f"record with id {id} was removed successfully")
