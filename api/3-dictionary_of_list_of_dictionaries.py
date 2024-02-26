#!/usr/bin/python3
"""
Module is documented
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user = response.json()

    if 'id' not in user:
        print("User with ID {} not found.".format(user_id))
        exit(1)

    username = user.get('username')

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No tasks found for user with ID {}.".format(user_id))
        exit(1)

    tasks = []

    for todo in todos:
        task = {
            "username": username,
            "task": todo.get('title'),
            "completed": todo.get('completed'),
        }
        tasks.append(task)

    todo_all_employees = {}
    todo_all_employees[user_id] = tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(todo_all_employees, f)
