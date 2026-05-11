# Iteration 02 Validation

## Validation Goal

The goal of this validation is to check whether iteration 2 satisfies its specification.

## Requirements Validated

| Requirement ID | Title | Result |
|---|---|---|
| REQ-006 | Mark task as done | Passed |
| REQ-007 | Delete task | Passed |
| REQ-008 | Handle invalid task numbers | Passed |
| REQ-010 | Session-only storage | Passed |

## Test Cases

### TC-007: Mark Task as Done

| Field | Description |
|---|---|
| Requirement | REQ-006 |
| Input | Add `Finish homework`, select `3`, enter `1` |
| Expected Result | Task is marked as done |
| Actual Result | Program displayed `Task marked as done.` |
| Status | Passed |

### TC-008: Show Done Status

| Field | Description |
|---|---|
| Requirement | REQ-006 |
| Input | Select `2` after marking task as done |
| Expected Result | Task is displayed with `[done]` status |
| Actual Result | Program displayed `1. Finish homework [done]` |
| Status | Passed |

### TC-009: Delete Task

| Field | Description |
|---|---|
| Requirement | REQ-007 |
| Input | Add `Finish homework`, select `4`, enter `1` |
| Expected Result | Task is deleted |
| Actual Result | Program displayed `Deleted task: Finish homework` |
| Status | Passed |

### TC-010: Confirm Deleted Task Is Removed

| Field | Description |
|---|---|
| Requirement | REQ-007 |
| Input | Select `2` after deleting the task |
| Expected Result | Deleted task does not appear |
| Actual Result | Program displayed `No tasks available...` |
| Status | Passed |

### TC-011: Invalid Number While Marking Done

| Field | Description |
|---|---|
| Requirement | REQ-008 |
| Input | Select `3`, enter `99` |
| Expected Result | Error message is displayed |
| Actual Result | Program displayed `Error: Invalid task number!` |
| Status | Passed |

### TC-012: Invalid Text While Deleting

| Field | Description |
|---|---|
| Requirement | REQ-008 |
| Input | Select `4`, enter `abc` |
| Expected Result | Error message is displayed |
| Actual Result | Program displayed `Error: Invalid task number!` |
| Status | Passed |

### TC-013: Session-Only Storage

| Field | Description |
|---|---|
| Requirement | REQ-010 |
| Input | Add multiple tasks during one program run |
| Expected Result | Tasks remain available while the program keeps running |
| Actual Result | Tasks remained available until the program exited |
| Status | Passed |

## Issues Found

| Issue | Severity | Planned Fix |
|---|---|---|
| Tasks are lost after closing the program | Low | Could be improved later with file storage |
| User cannot edit task titles | Low | Could be added in a future version |
| User cannot save deadlines | Low | Could be added in a future version |

## Validation Summary

Iteration 2 passed the validation tests. The app now supports marking tasks as done, deleting tasks, handling invalid task numbers, and keeping tasks available during the current session.

## AI Usage

I used AI to help structure the document.