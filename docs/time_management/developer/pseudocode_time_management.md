# Pseudocode for Time Management Feature

## Backend Logic
- Function: `add_task(task_name, priority)`
  - Validate input
  - Insert task into `backlog` table
  - Return success/failure response

- Function: `move_task_to_closed_list(task_id)`
  - Validate task exists in `backlog`
  - Update task status to 'closed'
  - Insert task into `closed_list` table with completion date
  - Return success/failure response

## Frontend Logic
- UI Component: Add Task Form
  - Input fields: `task_name`, `priority`
  - Submit button triggers `add_task` API call

- UI Component: Task List
  - Display tasks from `backlog` and `closed_list`
  - Button to move tasks to closed list triggers `move_task_to_closed_list` API call

## Data Flow
1. User adds a task through the form -> API call to `add_task` -> Task added to `backlog`
2. User moves a task to the closed list -> API call to `move_task_to_closed_list` -> Task status updated and moved to `closed_list`

