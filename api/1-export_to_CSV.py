import csv
import os
import requests
import sys

def user_info(employee_id):
    # Fetching employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Fetching todo list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Writing data to CSV file
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in todo_data:
            writer.writerow([user_id, username, task['completed'], task['title']])

    # Checking if the file exists before trying to read from it
    if os.path.exists(filename):
        print(f"User ID and Username: OK (Expected {user_id}, {username})")
    else:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main_1.py <employee_id>")
        sys.exit(1)
    
    user_info(int(sys.argv[1]))
