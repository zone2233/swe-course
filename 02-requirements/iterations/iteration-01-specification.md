# Iteration 01 Specification

## Iteration Goal

The goal of iteration 1 is to create the basic version of Console ToDo Manager. The user should be able to see a menu, add tasks, view tasks, and exit the program.

## Scope

### In Scope

- Display a console menu
- Add a task
- Reject empty task titles
- Show all tasks
- Show a message when no tasks exist
- Exit the program

### Out of Scope

- Marking tasks as done
- Deleting tasks
- Saving tasks to a file
- Loading tasks after restart
- Graphical user interface

## Related Requirements

| Requirement ID | Title |
|---|---|
| REQ-001 | Show menu |
| REQ-002 | Add task |
| REQ-003 | Reject empty task title |
| REQ-004 | Show tasks |
| REQ-005 | Show message when no tasks exist |
| REQ-009 | Exit program |

## Functional Specification

### Menu Display

When the program runs, it displays the following menu:

```text
Console ToDo Manager
1. Add task
2. Show tasks
3. Mark task as done
4. Delete task
5. Exit
```

### Add Task

The user selects option 1 and enters a task title.

Expected behavior:

- If the title is not empty, the task is added.
- The task is stored with done set to False.
- The program displays Task added....

### Empty Task Title

If the user enters an empty task title, the task is not added.

Expected message:

```text
Error: Task title cannot be empty!
```

### Show Tasks

The user selects option 2.

Expected behavior:

If tasks exist, they are displayed with a number and status.
If no tasks exist, the program displays No tasks available....

Example output:

```text
1. Finish homework [open]
```

### Exit Program

The user selects option 5.

Expected behavior:

The program displays Goodbye!.
The program stops running.

### Acceptance Criteria

- The menu is displayed when the program starts.
- The user can add a task with a non-empty title.
- Empty task titles are rejected.
- The user can view the current task list.
- The app displays a message when there are no tasks.
- The user can exit the program.

### AI Usage

I used AI to help convert the first set of implemented features into a formal specification document.