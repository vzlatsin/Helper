
### Backend Pseudocode for Time Management

1. **Closed Lists Feature:**
   - **Route 1:** `POST /add-closed-list-task`
     - Receive task data from the request form.
     - Store the task in the database with a daily timestamp.
     - Respond with a success or error message.
   - **Route 2:** `GET /daily-tasks`
     - Retrieve tasks for the current day from the database.
     - Send the list of tasks to the frontend.
   - **Route 3:** `POST /archive-tasks`
     - Move completed tasks to an archive table.
     - Respond with success or error message.

2. **Backlog Feature:**
   - **Route 1:** `POST /add-backlog-task`
     - Receive backlog task data from the request form.
     - Store the task in a separate backlog table.
     - Respond with a success or error message.
   - **Route 2:** `GET /backlog-tasks`
     - Retrieve backlog tasks from the database.
     - Send the list of tasks to the frontend.
   - **Route 3:** `POST /move-to-closed-list`
     - Receive task selection from the request form.
     - Move tasks from the backlog to the daily closed list.
     - Respond with success or error message.

