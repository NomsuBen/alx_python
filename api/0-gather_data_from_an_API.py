#/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to get employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")
    employee_data = employee_response.json()

    if "id" not in employee_data:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_name = employee_data["name"]

    # Make a GET request to get the TODO list for the employee
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    todos_data = todos_response.json()

    # Initialize counters
    total_tasks = len(todos_data)
    completed_tasks = 0

    # Store completed task titles in a list
    completed_task_titles = []

    for todo in todos_data:
        if todo["completed"]:
            completed_tasks += 1
            completed_task_titles.append(todo["title"])

    # Print employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for title in completed_task_titles:
        print(f"\t{title}")

if __name__ == "__main__":
    try:
        employee_id = int(input("Enter the employee ID: "))
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")
