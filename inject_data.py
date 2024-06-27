import requests

url = "http://localhost:5000/api/tasks"
data = {
    "title": "New Task",
    "description": "This is a new task",
    "status": "pending"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json())
