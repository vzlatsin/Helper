### `script_instructions_time_management.md`

```markdown
# Script Instructions for Time Management Feature

## Backend Implementation
### Database Schema
1. Create `backlog` table:
   ```sql
   CREATE TABLE backlog (
       task_id INTEGER PRIMARY KEY,
       task_name TEXT NOT NULL,
       priority INTEGER NOT NULL,
       status TEXT NOT NULL
   );
   ```

2. Create `closed_list` table:
   ```sql
   CREATE TABLE closed_list (
       task_id INTEGER PRIMARY KEY,
       task_name TEXT NOT NULL,
       completion_date DATE NOT NULL,
       FOREIGN KEY (task_id) REFERENCES backlog(task_id)
   );
   ```

### API Endpoints
1. `add_task` Endpoint:
   ```python
   @app.route('/api/add_task', methods=['POST'])
   def add_task():
       task_data = request.json
       # Insert task into the database
       return jsonify({'message': 'Task added successfully'}), 201
   ```

2. `move_task_to_closed_list` Endpoint:
   ```python
   @app.route('/api/move_task_to_closed_list', methods=['POST'])
   def move_task_to_closed_list():
       task_id = request.json['task_id']
       # Update task status and move to closed list
       return jsonify({'message': 'Task moved to closed list successfully'}), 200
   ```

## Frontend Implementation
### Add Task Form
1. HTML:
   ```html
   <form id="add-task-form">
       <input type="text" id="task-name" placeholder="Task Name">
       <input type="number" id="priority" placeholder="Priority">
       <button type="submit">Add Task</button>
   </form>
   ```

2. JavaScript:
   ```javascript
   document.getElementById('add-task-form').addEventListener('submit', function(event) {
       event.preventDefault();
       const taskName = document.getElementById('task-name').value;
       const priority = document.getElementById('priority').value;
       fetch('/api/add_task', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
           },
           body: JSON.stringify({ task_name: taskName, priority: priority }),
       })
       .then(response => response.json())
       .then(data => {
           console.log('Success:', data);
           fetchTasks();
       })
       .catch((error) => {
           console.error('Error:', error);
       });
   });

   function fetchTasks() {
       fetch('/api/get_tasks')
           .then(response => response.json())
           .then(data => {
               const taskList = document.getElementById('task-list');
               taskList.innerHTML = '';
               data.forEach(task => {
                   const listItem = document.createElement('li');
                   listItem.textContent = `${task.task_name} - ${task.priority}`;
                   taskList.appendChild(listItem);
               });
           });
   }

   function moveToClosedList(taskId) {
       fetch('/api/move_task_to_closed_list', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
           },
           body: JSON.stringify({ task_id: taskId }),
       })
       .then(response => response.json())
       .then(data => {
           console.log('Success:', data);
           fetchTasks();
       })
       .catch((error) => {
           console.error('Error:', error);
       });
   }
   ```
```

