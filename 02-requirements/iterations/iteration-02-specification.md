# Iteration 02 Specification

## Iteration Goal

The goal of iteration 2 is to complete the main todo management features by allowing users to mark tasks as done, delete tasks, and handle invalid task numbers.

## Scope

### In Scope

- Mark a task as done
- Delete a task
- Handle invalid task numbers
- Keep tasks available during the current program session

### Out of Scope

- Saving tasks after the program exits
- Loading tasks from a file
- Editing task titles
- User accounts
- Graphical user interface

## Related Requirements

| Requirement ID | Title |
|---|---|
| REQ-006 | Mark task as done |
| REQ-007 | Delete task |
| REQ-008 | Handle invalid task numbers |
| REQ-010 | Session-only storage |

## Functional Specification

### Mark Task as Done

The user selects option `3`.

The program first displays the current task list.

The user then enters the task number to mark as done.

Expected behavior:

- If the task number is valid, the task's `done` value is changed to `True`.
- The program displays `Task marked as done.`

Example:

```text
Task number to mark as done: 1
Task marked as done.
```

### Delete Task

The user selects option 4.

The program first displays the current task list.

The user then enters the task number to delete.

Expected behavior:

- If the task number is valid, the task is removed from the task list.
- The program displays the deleted task title.

Example:

```text
Task number to delete: 1
Deleted task: Finish homework
```

### Invalid Task Number Handling

If the user enters a non-number or a number that does not exist, the program displays:

```text
Error: Invalid task number!
```

This applies to:

Marking a task as done
Deleting a task

### Session-Only Storage

Tasks are stored in the tasks list while the program is running.

The app does not save tasks after the program exits.

### Acceptance Criteria

- The user can mark an existing task as done.
- A completed task is displayed with [done].
- The user can delete an existing task.
- A deleted task no longer appears in the task list.
- Invalid task numbers do not crash the program.
- Invalid task numbers show an error message.
- Tasks remain available while the program is running.

### AI Usage

I used AI to structure the document.