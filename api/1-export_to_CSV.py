#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import csv
import requests
import sys

def get_todo_progress(employee_id):
    # Get employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["name"]
    employee_username = user_data["username"]

    # Get TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Count completed tasks and total tasks
    completed_tasks = [task for task in todos_data if task["completed"]]

    # Print the result
    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{len(todos_data)}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

    # Export data to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in completed_tasks:
            writer.writerow([employee_id, employee_username, "Completed", task['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid employee ID.")