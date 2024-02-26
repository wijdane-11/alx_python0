import json
import requests
import sys

def user_info(employee_id):
    """
    Fetches employee information and todo list from a REST API and exports it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Fetching employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Fetching todo list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Constructing tasks in the required format
    tasks = []
    for task in todo_data:
        task_info = {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        tasks.append(task_info)

    # Writing tasks to JSON file
    filename = f"{user_id}.json"
    with open(filename, mode='w') as file:
        json.dump({str(user_id): tasks}, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 <script_name>.py <employee_id>")
        sys.exit(1)
    
    user_info(int(sys.argv[1]))
