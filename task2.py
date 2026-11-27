import csv
import json

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

for emp in employees:
    emp["salary"] = int(emp["salary"])

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print("Employees JSON created")

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

print("API KEY loaded:", API_KEY is not None)

import requests
url = "https://jsonplaceholder.typicode.com/users"

try:

    response = requests.get(url, timeout=5)

    response.raise_for_status()

    users = response.json()

    for user in users[:3]:
        print(
            user["id"],
            user["name"],
            user["email"]
        )

except requests.exceptions.Timeout:
    print("Error: Request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")

    else:
        response.raise_for_status()

except requests.exceptions.Timeout:
    print("Timeout error")

except requests.exceptions.ConnectionError:
    print("Connection error")

except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    result = []

    for user in data:

        employee = {
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),

            "city": user.get("address", {}).get("city"),

            "company": user.get("company", {}).get("name")
        }

        result.append(employee)

    with open("users.json", "w") as file:
        json.dump(result, file, indent=4)

    print("users.json created successfully")

except requests.exceptions.RequestException as e:
    print("API Error:", e)
