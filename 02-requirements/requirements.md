# Requirements

## Project

Console ToDo App

## Project Description

The console ToDo app is a small Python terminal application that allows a user to create, view, complete, and delete tasks during one program session.

The application uses a simple text menu and stores tasks in a Python list while the program is running.

## Requirement Attributes Used

Each requirement includes the following attributes:

- ID
- Title
- Description
- Type
- Priority
- Status
- Stakeholder
- Acceptance Criteria
- Validation Method
- Risk
- Iteration
- Related Feature

## Requirements Table

| ID | Title | Description | Type | Priority | Status | Stakeholder | Acceptance Criteria | Validation Method | Risk | Iteration | Related Feature |
|---|---|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | Show menu | The system shall display a console menu with the available options. | Functional | High | Implemented | User | Given the program starts, when the menu is shown, then the user can see options to add, show, mark done, delete, and exit. | Manual terminal test | Low | 1 | Menu |
| REQ-002 | Add task | The user shall be able to add a task with a title. | Functional | High | Implemented | User | Given the user selects option 1, when they enter a valid task title, then the task is added to the task list. | Manual terminal test | Low | 1 | Task creation |
| REQ-003 | Reject empty task title | The system shall reject empty task titles. | Functional | Medium | Implemented | User | Given the user selects option 1, when they enter an empty title, then an error message is shown and no task is added. | Manual negative test | Low | 1 | Input validation |
| REQ-004 | Show tasks | The user shall be able to display all current tasks. | Functional | High | Implemented | User | Given tasks exist, when the user selects option 2, then all tasks are displayed with a number and status. | Manual terminal test | Low | 1 | Task display |
| REQ-005 | Show message when no tasks exist | The system shall show a message if the task list is empty. | Functional | Medium | Implemented | User | Given there are no tasks, when the user selects option 2, then the system displays `No tasks available...`. | Manual terminal test | Low | 1 | Task display |
| REQ-006 | Mark task as done | The user shall be able to mark an existing task as done. | Functional | High | Implemented | User | Given a task exists, when the user selects option 3 and enters a valid task number, then the task status changes to done. | Manual terminal test | Medium | 2 | Task status |
| REQ-007 | Delete task | The user shall be able to delete an existing task. | Functional | High | Implemented | User | Given a task exists, when the user selects option 4 and enters a valid task number, then the task is removed from the task list. | Manual terminal test | Medium | 2 | Task deletion |
| REQ-008 | Handle invalid task numbers | The system shall show an error message for invalid task numbers. | Functional | Medium | Implemented | User | Given the user enters an invalid task number, when marking or deleting a task, then the system displays `Error: Invalid task number!`. | Manual negative test | Medium | 2 | Error handling |
| REQ-009 | Exit program | The user shall be able to exit the program using the menu. | Functional | High | Implemented | User | Given the menu is shown, when the user selects option 5, then the program prints `Goodbye!` and exits. | Manual terminal test | Low | 1 | Exit |
| REQ-010 | Session-only storage | The system shall store tasks only during the current program session. | Technical | Medium | Implemented | Developer | Given tasks are added, when the program is running, then tasks remain available until the program exits. | Manual runtime test | Medium | 2 | Storage |

## AI Usage

I used AI to help structure the requirements and define useful attributes such as priority, acceptance criteria, validation method, risk, and iteration. I adapted the requirements manually so they match my actual Python Console ToDo Manager app.