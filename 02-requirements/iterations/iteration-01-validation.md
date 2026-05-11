# Iteration 01 Validation

## Validation Goal

The goal of this validation is to check whether iteration 1 satisfies its specification.

## Requirements Validated

| Requirement ID | Title | Result |
|---|---|---|
| REQ-001 | Show menu | Passed |
| REQ-002 | Add task | Passed |
| REQ-003 | Reject empty task title | Passed |
| REQ-004 | Show tasks | Passed |
| REQ-005 | Show message when no tasks exist | Passed |
| REQ-009 | Exit program | Passed |

## Test Cases

### TC-001: Show Menu

| Field | Description |
|---|---|
| Requirement | REQ-001 |
| Input | Start the program |
| Expected Result | The menu is displayed |
| Actual Result | The menu was displayed |
| Status | Passed |

### TC-002: Add Valid Task

| Field | Description |
|---|---|
| Requirement | REQ-002 |
| Input | Select `1`, enter `Finish homework` |
| Expected Result | Task is added and confirmation is shown |
| Actual Result | Program displayed `Task added...` |
| Status | Passed |

### TC-003: Reject Empty Task

| Field | Description |
|---|---|
| Requirement | REQ-003 |
| Input | Select `1`, enter an empty title |
| Expected Result | Error message is displayed and task is not added |
| Actual Result | Program displayed `Error: Task title cannot be empty!` |
| Status | Passed |

### TC-004: Show Tasks

| Field | Description |
|---|---|
| Requirement | REQ-004 |
| Input | Select `2` after adding a task |
| Expected Result | The task is displayed with number and status |
| Actual Result | Program displayed `1. Finish homework [open]` |
| Status | Passed |

### TC-005: Show No Tasks Message

| Field | Description |
|---|---|
| Requirement | REQ-005 |
| Input | Select `2` before adding any tasks |
| Expected Result | Program displays `No tasks available...` |
| Actual Result | Program displayed `No tasks available...` |
| Status | Passed |

### TC-006: Exit Program

| Field | Description |
|---|---|
| Requirement | REQ-009 |
| Input | Select `5` |
| Expected Result | Program displays `Goodbye!` and exits |
| Actual Result | Program displayed `Goodbye!` and exited |
| Status | Passed |

## Issues Found

| Issue | Severity | Planned Fix |
|---|---|---|
| Tasks cannot be marked as done yet | Medium | Add in iteration 2 |
| Tasks cannot be deleted yet | Medium | Add in iteration 2 |
| Tasks are not saved after exiting | Low | Possible future improvement |

## Validation Summary

Iteration 1 passed the main validation tests. The user can open the program, use the menu, add tasks, show tasks, reject empty titles, and exit the program.

## AI Usage

I used AI to help structure the document.