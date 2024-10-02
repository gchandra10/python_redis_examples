from db_config import get_redis_connection
import json

r = get_redis_connection()

## r.flushall()

data = {
    "name": "Ross Geller",
    "occupation": "Paleontologist",
    "relationship_status": "Divorced",
    "friends": [
        "Rachel Green",
        "Monica Geller",
        "Joey Tribbiani",
        "Chandler Bing",
        "Phoebe Buffay",
    ],
    "children": [
        {"name": "Ben Geller", "mother": "Carol Willick"},
        {"name": "Emma Geller-Green", "mother": "Rachel Green"},
    ],
    "education": {"college": "Columbia University", "degree": "Ph.D. in Paleontology"},
}

r.json().set("friends:character:ross", ".", json.dumps(data))

## This part is to retrieve the data

import json

# Get JSON and decode
json_data = r.json().get("friends:character:ross")
data = json.loads(json_data)

# Extract fields
name = data["name"]
occupation = data["occupation"]
education = data["education"]

print(f"Name: {name}")
print(f"Occupation: {occupation}")
print(f"Education: {education}")
