document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('task-form');
    const taskDate = document.getElementById('task-date');
    const startTime = document.getElementById('start-time');
    const endTime = document.getElementById('end-time');
    const taskDesc = document.getElementById('task-desc');
    const taskList = document.getElementById('tasks-list');
    console.log("Initial task list items:", taskList.innerHTML);
    taskList.querySelectorAll('li').forEach(taskItem => {
        console.log(taskItem.innerHTML);
    });
    loadEntries();

    const saveButton = document.getElementById('save-button');
    const entriesContainer = document.getElementById('entries-container');
    const moveToBacklogButton = document.getElementById('move-to-backlog-button'); 

    // Ensure all elements exist
    if (!taskForm || !taskDate || !startTime || !endTime || !taskDesc || !taskList || !saveButton || !entriesContainer) {
        console.error('One or more elements are missing from the DOM');
        return;
    }

    // Add event listeners for tab clicks
    document.querySelectorAll('.tabs .tab').forEach(tab => {
        tab.addEventListener('click', function() {
            const tabId = this.dataset.tab;
            console.log(`Tab clicked: ${tabId}`);
            if (tabId === 'today') {
                fetchTodayTasks();
            } else if (tabId === 'tomorrow') {
                fetchTomorrowTasks();
            } else if (tabId === 'forgotten') {
                fetchForgottenTasks();
            }
        });
    });
    

    // Form submission event
    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();
    
        const date = taskDate.value;
        const start = startTime.value;
        const end = endTime.value;
        const description = taskDesc.value;
    
        if (date && description) {
            const taskItem = document.createElement('li');
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.classList.add('task-checkbox');
            checkbox.value = description;
            taskItem.appendChild(checkbox);
            taskItem.appendChild(document.createTextNode(`${date} ${start}-${end}: ${description}`));
            taskList.appendChild(taskItem);
    
            // Clear the form
            taskDate.value = '';
            startTime.value = '';
            endTime.value = '';
            taskDesc.value = '';
        }
    });
    



    saveButton.addEventListener('click', function(event) {
        event.preventDefault();

        console.log("Save button clicked");

        const taskDate = document.getElementById('task-date').value;
        const startTime = document.getElementById('start-time').value;
        const endTime = document.getElementById('end-time').value;
        const taskDesc = document.getElementById('task-desc').value.trim();

        console.log(`Task Date: ${taskDate}`);
        console.log(`Start Time: ${startTime}`);
        console.log(`End Time: ${endTime}`);
        console.log(`Task Description: ${taskDesc}`);

        const tasks = [];

        // Validate and format the task input
        if (taskDate && taskDesc) {
            tasks.push({
                date: taskDate,
                start_time: startTime,
                end_time: endTime,
                task_description: taskDesc
            });
        } else {
            alert("Please enter a valid date and description.");
            return;
        }

        console.log("Tasks to be saved:", tasks);

        // Send the task to the backend
        fetch('/task-diary', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                tasks: tasks,
                reflections: "" // Modify this part to include actual reflections if needed
            })
        })
        .then(response => {
            console.log("Save response:", response);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log("Response data from save:", data);
            if (data.success) {
                alert('Task diary entry saved!');
                // Clear the input fields
                document.getElementById('task-form').reset();
                // Optionally, refresh the task list or update the UI
            } else {
                alert('Error saving task diary entry.');
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    });

    
        
    
    














    // Move to backlog button event with diagnostics
    moveToBacklogButton.addEventListener('click', function(event) {
        console.log("Move to Backlog button clicked");
    
        const taskDate = document.getElementById('task-date').value;
        const startTime = document.getElementById('start-time').value;
        const endTime = document.getElementById('end-time').value;
        const taskDesc = document.getElementById('task-desc').value.trim();
    
        console.log(`Task Date: ${taskDate}`);
        console.log(`Start Time: ${startTime}`);
        console.log(`End Time: ${endTime}`);
        console.log(`Task Description: ${taskDesc}`);
    
        const tasks = [];
    
        // Validate and format the task input
        if (taskDate && taskDesc) {
            tasks.push(taskDesc);
        } else {
            alert("Please enter a valid date and description.");
            return;
        }
    
        console.log("Tasks to be moved to backlog:", tasks);
    
        // Send the task to the backend
        fetch('/move_to_backlog', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                task_descriptions: tasks
            })
        })
        .then(response => {
            console.log("Move to Backlog response:", response);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log("Response data from move to backlog:", data);
            if (data.message) {
                alert('Tasks moved to backlog successfully!');
                // Clear the input fields
                document.getElementById('task-form').reset();
                // Optionally, refresh the task list or update the UI
            } else {
                alert('Error moving tasks to backlog.');
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    });
    
    



    // View tasks for a specific date
    async function viewTasksForDate() {
        const date = document.getElementById('task-date').value;
        const response = await fetch(`/tasks?date=${date}`);
        const data = await response.json();
        const taskContainer = document.getElementById('tasks-for-date');
        taskContainer.innerHTML = '';
        data.forEach(task => {
            const taskElement = document.createElement('div');
            taskElement.textContent = task.task_description + (task.status === 'selected' ? ' (Selected)' : '');
            taskContainer.appendChild(taskElement);
        });
    }

    // Select tasks for a specific date
    async function selectTasksForDate() {
        console.log("selectTasksForDate function called"); // Log function call
    
        const taskList = document.getElementById('today-tasks-list');
        const selectedTaskIds = [];
    
        taskList.querySelectorAll('li').forEach(taskItem => {
            const checkbox = taskItem.querySelector('input[type="checkbox"]');
            const status = taskItem.dataset.status; // Assuming status is stored in a data attribute
    
            if (checkbox.checked && status === 'pending') {
                selectedTaskIds.push(parseInt(checkbox.value));
            }
        });
    
        console.log("Selected task IDs:", selectedTaskIds); // Log selected task IDs
    
        const payload = { task_ids: selectedTaskIds };
        console.log("Payload being sent to /tasks/select:", JSON.stringify(payload)); // Log the payload
    
        fetch('/tasks/select', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(response => {
            console.log("Response from /tasks/select:", response); // Log the response
            return response.json();
        })
        .then(data => {
            console.log("Data from /tasks/select:", data); // Log the response data
            if (data.message) {
                // Update the UI to reflect the task state changes
                alert(data.message);
                selectedTaskIds.forEach(taskId => {
                    const taskItem = document.querySelector(`input[value="${taskId}"]`).parentElement;
                    taskItem.dataset.status = 'selected'; // Update status
                });
            } else if (data.error) {
                alert(`Error: ${data.error}`);
            } else {
                alert('Unknown error occurred.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    
    


    async function fetchTodayTasks() {
        console.log("fetchTodayTasks");
        try {
            const response = await fetch('/tasks/today');
            const tasks = await response.json();

            console.log("Tasks fetched for today:", tasks); // Log the tasks fetched
            
            // Separate tasks into pending and closed lists
            const pendingTasks = tasks.filter(task => task.status === 'pending');
            const closedTasks = tasks.filter(task => task.status === 'selected');
    
            // Populate closedTaskIds with the IDs of closed tasks
            closedTaskIds = closedTasks.map(task => task.id);

    
            // Display tasks in their respective lists
            displayTasks(pendingTasks, 'pending-tasks-list');
            displayTasks(closedTasks, 'closed-tasks-list');
        } catch (error) {
            console.error('Error fetching today\'s tasks:', error);
        }
    }

    async function fetchTomorrowTasks() {
        console.log("fetchTomorrowTasks");
        try {
            const response = await fetch('/tasks/tomorrow');
            const tasks = await response.json();
            
            // Separate tasks into pending and closed lists
            const pendingTasks = tasks.filter(task => task.status === 'pending');
            const closedTasks = tasks.filter(task => task.status === 'selected');
            
            // Populate closedTaskIds with the IDs of closed tasks
            closedTaskIds = closedTasks.map(task => task.id);
    
            // Display tasks in their respective lists
            displayTasks(pendingTasks, 'tomorrow-pending-tasks-list');
            displayTasks(closedTasks, 'tomorrow-closed-tasks-list');
        } catch (error) {
            console.error('Error fetching tomorrow\'s tasks:', error);
        }
    }
    
    
    

    function displayTasks(tasks, elementId) {
        const taskList = document.getElementById(elementId);
        taskList.innerHTML = ''; // Clear existing tasks

        console.log(`Displaying tasks in element: ${elementId}`, tasks); // Log the tasks being displayed

        if (tasks.length === 0) {
            // If there are no tasks, display a message or handle the empty state
            const emptyMessage = document.createElement('li');
            emptyMessage.textContent = 'No tasks found';
            taskList.appendChild(emptyMessage);
            return;
        }
        tasks.forEach(task => {
            const taskItem = document.createElement('li');
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.value = task.id;
            taskItem.dataset.status = task.status; // Set the status
            taskItem.appendChild(checkbox);
            taskItem.appendChild(document.createTextNode(`${task.task_description} (${task.start_time} - ${task.end_time})`));
            taskList.appendChild(taskItem);
        });
    }

    let selectedTasks = [];

    function trackSelectedTasks() {
        const checkboxes = document.querySelectorAll('#today-tasks-list input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                if (this.checked) {
                    selectedTasks.push(this.value);
                } else {
                    selectedTasks = selectedTasks.filter(id => id !== this.value);
                }
            });
        });
    }

    let closedTaskIds = [];

    function moveSelectedTasks() {
        const taskList = document.getElementById('pending-tasks-list');
        const selectedTaskIds = [];
        const nonSelectedTasks = [];
    
        taskList.querySelectorAll('li').forEach(taskItem => {
            const checkbox = taskItem.querySelector('input[type="checkbox"]');
            if (checkbox && checkbox.checked) {
                selectedTaskIds.push(parseInt(checkbox.value));
            } else {
                nonSelectedTasks.push(taskItem);
            }
        });
    
        // Check if there are any selected tasks
        if (selectedTaskIds.length === 0) {
            alert('No tasks selected to move.');
            return;
        }
    
        const date = new Date().toISOString().split('T')[0];  // Get today's date in YYYY-MM-DD format
        const payload = { task_ids: selectedTaskIds, date: date };
    
        console.log('Payload being sent:', payload);  // Log the payload to check its format
    
        fetch('/tasks/select', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                closedTaskIds = selectedTaskIds;  // Track the moved task IDs
                const closedTasksList = document.getElementById('closed-tasks-list');
                const pendingTasksList = document.getElementById('pending-tasks-list');
    
                // Append the moved tasks to the closed tasks list
                selectedTaskIds.forEach(taskId => {
                    const checkbox = document.querySelector(`input[value="${taskId}"]`);
                    if (checkbox) {
                        const taskItem = checkbox.parentElement;
                        if (taskItem) {
                            taskItem.querySelector('input[type="checkbox"]').checked = false;  // Uncheck the checkbox
                            closedTasksList.appendChild(taskItem);
                        }
                    }
                });
    
                // Clear the pending tasks list and re-append non-selected tasks
                pendingTasksList.innerHTML = '';
                nonSelectedTasks.forEach(task => pendingTasksList.appendChild(task));
            } else {
                alert('Error closing tasks');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    
    
    // Add event listener for the "Move to Closed List" button
    document.getElementById('move-tasks-button').addEventListener('click', moveSelectedTasks);
    
    

    function undoMove() {
        const closedTasksList = document.getElementById('closed-tasks-list');
        const selectedClosedTaskIds = [];
        const nonSelectedClosedTasks = [];
    
        closedTasksList.querySelectorAll('li').forEach(taskItem => {
            const checkbox = taskItem.querySelector('input[type="checkbox"]');
            if (checkbox && checkbox.checked) {
                selectedClosedTaskIds.push(parseInt(checkbox.value));
            } else {
                nonSelectedClosedTasks.push(taskItem);
            }
        });
    
        console.log('Reverting task IDs:', selectedClosedTaskIds);  // Log the task IDs to check
    
        // Check if there are any tasks to revert
        if (selectedClosedTaskIds.length === 0) {
            alert('No tasks selected to revert.');
            return;
        }
    
        fetch('/tasks/revert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task_ids: selectedClosedTaskIds })  // Send only the selected closed task IDs
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                console.log('Tasks reverted successfully:', data.message);  // Log success message
                const pendingTasksList = document.getElementById('pending-tasks-list');
    
                selectedClosedTaskIds.forEach(taskId => {
                    const checkbox = document.querySelector(`input[value="${taskId}"]`);
                    if (checkbox) {
                        const taskItem = checkbox.parentElement;
                        if (taskItem) {
                            taskItem.querySelector('input[type="checkbox"]').checked = false;  // Uncheck the checkbox
                            pendingTasksList.appendChild(taskItem);
                        }
                    }
                });
    
                // Update closedTaskIds to remove the reverted tasks
                closedTaskIds = closedTaskIds.filter(id => !selectedClosedTaskIds.includes(id));
    
                // Update the closed tasks list with non-selected tasks
                closedTasksList.innerHTML = '';
                nonSelectedClosedTasks.forEach(task => closedTasksList.appendChild(task));
            } else {
                console.error('Error reverting tasks:', data.error);  // Log the error message
                alert('Error reverting tasks');
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);  // Log any fetch errors
            alert('Error reverting tasks');
        });
    }
  
    document.getElementById('undo-move-button').addEventListener('click', undoMove);

    function moveSelectedTasksTomorrow() {
        const taskList = document.getElementById('tomorrow-pending-tasks-list');
        const selectedTaskIds = [];
        const nonSelectedTasks = [];
    
        taskList.querySelectorAll('li').forEach(taskItem => {
            const checkbox = taskItem.querySelector('input[type="checkbox"]');
            if (checkbox && checkbox.checked) {
                selectedTaskIds.push(parseInt(checkbox.value));
            } else {
                nonSelectedTasks.push(taskItem);
            }
        });
    
        if (selectedTaskIds.length === 0) {
            alert('No tasks selected to move.');
            return;
        }
    
        const payload = { task_ids: selectedTaskIds };
        console.log('Payload being sent:', JSON.stringify(payload));
    
        fetch('/tasks/select', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                const closedTasksList = document.getElementById('tomorrow-closed-tasks-list');
                const pendingTasksList = document.getElementById('tomorrow-pending-tasks-list');
    
                selectedTaskIds.forEach(taskId => {
                    const checkbox = document.querySelector(`input[value="${taskId}"]`);
                    if (checkbox) {
                        const taskItem = checkbox.parentElement;
                        if (taskItem) {
                            taskItem.querySelector('input[type="checkbox"]').checked = false;
                            closedTasksList.appendChild(taskItem);
                        }
                    }
                });
    
                pendingTasksList.innerHTML = '';
                nonSelectedTasks.forEach(task => pendingTasksList.appendChild(task));
            } else {
                alert('Error closing tasks');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    document.getElementById('move-tasks-button-tomorrow').addEventListener('click', moveSelectedTasksTomorrow);

    function undoMoveTomorrow() {
        const closedTasksList = document.getElementById('tomorrow-closed-tasks-list');
        const selectedClosedTaskIds = [];
        const nonSelectedClosedTasks = [];
    
        closedTasksList.querySelectorAll('li').forEach(taskItem => {
            const checkbox = taskItem.querySelector('input[type="checkbox"]');
            if (checkbox && checkbox.checked) {
                selectedClosedTaskIds.push(parseInt(checkbox.value));
            } else {
                nonSelectedClosedTasks.push(taskItem);
            }
        });
    
        if (selectedClosedTaskIds.length === 0) {
            alert('No tasks selected to revert.');
            return;
        }
    
        fetch('/tasks/revert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task_ids: selectedClosedTaskIds })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                const pendingTasksList = document.getElementById('tomorrow-pending-tasks-list');
    
                selectedClosedTaskIds.forEach(taskId => {
                    const checkbox = document.querySelector(`input[value="${taskId}"]`);
                    if (checkbox) {
                        const taskItem = checkbox.parentElement;
                        if (taskItem) {
                            taskItem.querySelector('input[type="checkbox"]').checked = false;
                            pendingTasksList.appendChild(taskItem);
                        }
                    }
                });
    
                closedTaskIds = closedTaskIds.filter(id => !selectedClosedTaskIds.includes(id));
    
                closedTasksList.innerHTML = '';
                nonSelectedClosedTasks.forEach(task => closedTasksList.appendChild(task));
            } else {
                console.error('Error reverting tasks:', data.error);
                alert('Error reverting tasks');
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            alert('Error reverting tasks');
        });
    }
    
    document.getElementById('undo-move-button-tomorrow').addEventListener('click', undoMoveTomorrow);


    
    
    
    
    
    async function fetchForgottenTasks() {
        console.log("fetchForgottenTasks function executed");  // Log when the function is executed
        try {
            const response = await fetch('/tasks/forgotten');
            const tasks = await response.json();
            
            // Ensure the tasks variable is an array
            if (!Array.isArray(tasks)) {
                console.error('Invalid response format for forgotten tasks:', tasks);
                return;
            }
    
            // Log the tasks array
            console.log('Tasks for forgotten:', tasks);
    
            // Display tasks in the forgotten tasks list
            displayTasks(tasks, 'forgotten-tasks-list');
        } catch (error) {
            console.error('Error fetching forgotten tasks:', error);
        }
    }
    
    
    
    // Add event listener for the "Forgotten Tasks" tab
    document.querySelector('.tabs .tab[data-tab="forgotten"]').addEventListener('click', fetchForgottenTasks);
    
    // Load task diary entries
    function loadEntries() {
        const tasksList = document.getElementById('tasks-list');
        console.log("Initial task list items:");
        tasksList.querySelectorAll('li').forEach(taskItem => {
            console.log(taskItem.innerHTML);
        });
        fetch('/get-task-diary-entries')
        .then(response => response.json())
        .then(entries => {
            console.log("Entries loaded from backend:", entries); 
            if (entries.length === 0) {
                console.log("No entries found in backend response."); // Add this line
            }
            entriesContainer.innerHTML = ''; // Clear previous entries
            entries.forEach(entry => {
                console.log("Processing entry:", entry);
                const entryDiv = document.createElement('div');
                entryDiv.classList.add('entry');
                const entryDate = document.createElement('h3');
                entryDate.innerText = `Date: ${entry.date}`;
                entryDiv.appendChild(entryDate);
                const entryTasks = document.createElement('p');
                const tasks = entry.tasks && Array.isArray(entry.tasks) ? entry.tasks.join(', ') : 'No tasks available';
                entryTasks.innerText = `Tasks: ${tasks}`;
                entryDiv.appendChild(entryTasks);
                entriesContainer.appendChild(entryDiv);
            });

            console.log("Final task list items:");
            tasksList.querySelectorAll('li').forEach(taskItem => {
                console.log(taskItem.innerHTML);
            });
        });
    }


    // Load entries on page load
    loadEntries();

    // Attach functions to window object to make them accessible in HTML
    window.viewTasksForDate = viewTasksForDate;
    window.selectTasksForDate = selectTasksForDate;
    window.fetchTodayTasks = fetchTodayTasks;
    window.fetchTomorrowTasks = fetchTomorrowTasks;
    window.fetchForgottenTasks = fetchForgottenTasks;
});
