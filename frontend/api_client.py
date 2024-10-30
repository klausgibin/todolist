import requests

API_URL = "http://localhost:8000"

def fetch_data():
    response = requests.get(f"{API_URL}/tarefas")
    return response.json()

def update_task(task_id, updated_data):
    response = requests.put(f"{API_URL}/tarefas/{task_id}", json=updated_data)
    return response.json()

def create_task(task_data):
    response = requests.post(f"{API_URL}/tarefas", json=task_data)
    return response.json()

def delete_task(task_id):
    response = requests.delete(f"{API_URL}/tarefas/{task_id}")
    return response.json()