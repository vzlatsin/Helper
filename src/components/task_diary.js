document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('task-form');
    const taskDate = document.getElementById('task-date');
    const startTime = document.getElementById('start-time');
    const endTime = document.getElementById('end-time');
    const taskDesc = document.getElementById('task-desc');
    const taskList = document.getElementById('tasks-list');
    const saveButton = document.getElementById('save-button');
    const entriesContainer = document.getElementById('entries-container');

    // Ensure all elements exist
    if (!taskForm || !taskDate || !startTime || !endTime || !taskDesc || !taskList || !saveButton || !entriesContainer) {
        console.error('One or more elements are missing from the DOM');
        return;
    }

    // Form submission event
    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const date = taskDate.value;
        const start = startTime.value;
        const end = endTime.value;
        const description = taskDesc.value;

        if (date && description) {
            const taskItem = document.createElement('li');
            taskItem.textContent = `${date} ${start}-${end}: ${description}`;
            taskItem.dataset.status = 'pending'; // Add status data attribute
            taskList.appendChild(taskItem);

            // Clear the form
            taskDate.value = '';
            startTime.value = '';
            endTime.value = '';
            taskDesc.value = '';
        }
    });

    // Save button event
    saveButton.addEventListener('click', function(event) {
        event.preventDefault();

        const tasks = [];
        taskList.querySelectorAll('li').forEach(taskItem => {
            const [dateTime, ...descriptionParts] = taskItem.textContent.split(': ');
            const [date, timeRange] = dateTime.split(' ');
            const [start, end] = timeRange.split('-');
            const description = descriptionParts.join(': ');
            tasks.push({
                date: date,
                start_time: start,
                end_time: end,
                task_description: description
            });
        });

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
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert('Task diary entry saved!');
                loadEntries();
            } else {
                alert('Error saving task diary entry.');
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
        try {
            const response = await fetch('/tasks/today');
            const tasks = await response.json();
            
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

    function displayTasks(tasks, elementId) {
        const taskList = document.getElementById(elementId);
        taskList.innerHTML = ''; // Clear existing tasks
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
        console.log('Reverting task IDs:', closedTaskIds);  // Log the task IDs to check
    
        if (closedTaskIds.length === 0) {
            alert('No tasks to revert');
            return;
        }
    
        fetch('/tasks/revert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ task_ids: closedTaskIds })  // Send only the closedTaskIds
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                console.log('Tasks reverted successfully:', data.message);  // Log success message
                const closedTasksList = document.getElementById('closed-tasks-list');
                const pendingTasksList = document.getElementById('pending-tasks-list');
    
                closedTaskIds.forEach(taskId => {
                    const checkbox = document.querySelector(`input[value="${taskId}"]`);
                    if (checkbox) {
                        const taskItem = checkbox.parentElement;
                        if (taskItem) {
                            taskItem.querySelector('input[type="checkbox"]').checked = false;  // Uncheck the checkbox
                            pendingTasksList.appendChild(taskItem);
                        }
                    }
                });
                closedTaskIds = [];  // Clear the list after reverting
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

    
    

    // Load task diary entries
    function loadEntries() {
        fetch('/get-task-diary-entries')
        .then(response => response.json())
        .then(entries => {
            entriesContainer.innerHTML = ''; // Clear previous entries
            entries.forEach(entry => {
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
        });
    }

    // Load entries on page load
    loadEntries();

    // Attach functions to window object to make them accessible in HTML
    window.viewTasksForDate = viewTasksForDate;
    window.selectTasksForDate = selectTasksForDate;
    window.fetchTodayTasks = fetchTodayTasks;
});
