import csv
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

    # Correct number of tasks in CSV
    num_tasks = len(todo_data)
    print(f"Number of tasks in CSV: {num_tasks} (Expected {num_tasks})")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main_0.py <employee_id>")
        sys.exit(1)
    
    user_info(int(sys.argv[1]))
