# Tech Stack

## Project

Console ToDo Manager

## Programming Language

Python

Python was chosen because it is simple, readable, and suitable for building small terminal applications.

## User Interface

Command-line interface.

The user interacts with the app through a numbered text menu in the terminal.

## Data Storage

The current version uses in-memory storage.

Tasks are stored in a Python list:

```python
tasks = []
```

Each task is stored as a dictionary:

```python
{
    "title": "Example task",
    "done": False
}
```

## Development Tools

- Visual Studio Code
- Terminal
- Git/GitHub

## Testing Approach

The app is tested manually through the terminal.

The main testing methods are:

- Normal input testing
- Empty input testing
- Invalid number testing
- Invalid menu option testing

## Main Functions

| Function | Purpose |
|---|---|
| `show_menu()` | Displays the menu options in the terminal. |
| `add_task()` | Lets the user enter a task title and adds it to the task list. |
| `show_tasks()` | Displays all current tasks with their number and status. |
| `mark_task_done()` | Lets the user select a task number and marks that task as done. |
| `delete_task()` | Lets the user select a task number and removes that task from the list. |

## Constraints

- Tasks are not saved after exiting the program.
- The app only runs in the terminal.
- The app does not use a database.
- The app does not use external Python libraries.
- The app is intended for single-user local use.

## AI Usage

I used AI to help create the table and structure the techstack.md file