document.addEventListener('DOMContentLoaded', function() {
    const currentDate = new Date().toISOString().split('T')[0];
    const currentWeekday = new Date().toLocaleDateString('en-US', { weekday: 'long' });
    document.getElementById('current-date').innerText = currentDate;
    document.getElementById('current-weekday').innerText = currentWeekday;

    const taskList = document.getElementById('tasks-list');
    const taskForm = document.getElementById('task-form');

    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const taskDescription = document.getElementById('task-description').value;

        if (taskDescription) {
            const taskItem = document.createElement('li');
            taskItem.textContent = taskDescription;
            taskList.appendChild(taskItem);

            // Clear the form
            document.getElementById('task-description').value = '';
        }
    });

    document.getElementById('save-button').addEventListener('click', function(event) {
        event.preventDefault();
        const tasks = [];
        taskList.querySelectorAll('li').forEach(taskItem => {
            tasks.push(taskItem.textContent);
        });
        const reflections = document.getElementById('task-reflection').value;

        fetch('/task-diary', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                date: currentDate,
                tasks: tasks,
                reflections: reflections
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Task diary entry saved!');
                loadEntries(); // Load entries after saving a new one
            } else {
                alert('Error saving task diary entry.');
            }
        });
    });

    function loadEntries() {
        fetch('/get-task-diary-entries')
            .then(response => response.json())
            .then(entries => {
                const entriesContainer = document.getElementById('entries-container');
                entriesContainer.innerHTML = ''; // Clear previous entries
                entries.forEach(entry => {
                    if (entry.date === currentDate) { // Only display tasks for the current date
                        const entryDiv = document.createElement('div');
                        entryDiv.classList.add('entry');
                        const entryTasks = document.createElement('p');
                        entryTasks.innerText = `Tasks: ${entry.tasks.join(', ')}`;
                        const entryReflections = document.createElement('p');
                        entryReflections.innerText = `Reflections: ${entry.reflections}`;
                        entryDiv.appendChild(entryTasks);
                        entryDiv.appendChild(entryReflections);
                        entriesContainer.appendChild(entryDiv);
                    }
                });
            });
    }

    // Load entries on page load
    loadEntries();
});
