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
        const date = document.getElementById('task-date').value;
        const response = await fetch('/tasks/select', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ date })
        });
        const result = await response.json();
        alert(result.message);
    }

    async function fetchTodayTasks() {
        try {
            const response = await fetch('/tasks/today');
            const tasks = await response.json();
            displayTasks(tasks, 'today-tasks-list');
        } catch (error) {
            console.error('Error fetching today\'s tasks:', error);
        }
    }
    
    function displayTasks(tasks, elementId) {
        const taskList = document.getElementById(elementId);
        taskList.innerHTML = ''; // Clear existing tasks
        tasks.forEach(task => {
            const taskItem = document.createElement('li');
            taskItem.textContent = task.task;
            taskList.appendChild(taskItem);
        });
    }
    

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
