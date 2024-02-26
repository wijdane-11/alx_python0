#!/usr/bin/env python3

"""
This script fetches employee information and todo list from a REST API and exports it to a JSON file.

The script takes an employee ID as a command-line argument and retrieves the user's details and todo list
from the JSONPlaceholder API. It then constructs the tasks in the required JSON format and writes them 
to a JSON file named USER_ID.json.

Usage: python3 script_name.py employee_id
"""

import json
import requests
import sys

class EmployeeTodoExporter:
    """
    A class to export employee todo list to a JSON file.

    Attributes:
        employee_id (int): The ID of the employee.
    """

    def __init__(self, employee_id):
        """
        Initializes EmployeeTodoExporter with the employee ID.
        """
        self.employee_id = employee_id

    def fetch_employee_details(self):
        """
        Fetches employee details from the JSONPlaceholder API.

        Returns:
            dict: A dictionary containing employee details.
        """
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{self.employee_id}")
        return response.json()

    def fetch_employee_todo_list(self):
        """
        Fetches todo list for the employee from the JSONPlaceholder API.

        Returns:
            list: A list of dictionaries representing todo tasks.
        """
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{self.employee_id}/todos")
        return response.json()

    def export_to_json(self):
        """
        Exports employee todo list to a JSON file.

        Returns:
            None
        """
        employee_details = self.fetch_employee_details()
        username = employee_details['username']

        todo_list = self.fetch_employee_todo_list()
        tasks = []

        for task in todo_list:
            task_info = {
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            }
            tasks.append(task_info)

        filename = f"{self.employee_id}.json"
        with open(filename, mode='w') as file:
            json.dump({str(self.employee_id): tasks}, file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    exporter = EmployeeTodoExporter(employee_id)
    exporter.export_to_json()
