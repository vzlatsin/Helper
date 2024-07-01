import requests

def test_save_tasks():
    url = 'http://127.0.0.1:5000/task-diary'
    data = {'tasks': {'2024-07-01': ['Task 1', 'Task 2']}}
    response = requests.post(url, json=data)
    print('POST /task-diary:', response.json())

def test_get_tasks():
    url = 'http://127.0.0.1:5000/get-task-diary-entries'
    response = requests.get(url)
    print('GET /get-task-diary-entries:', response.json())

if __name__ == '__main__':
    test_save_tasks()
    test_get_tasks()
