document.addEventListener('DOMContentLoaded', function() {
    const taskForm = document.getElementById('task-form');
    const taskDate = document.getElementById('task-date');
    const taskDesc = document.getElementById('task-desc');
    const taskList = document.getElementById('tasks-list');
    const saveButton = document.getElementById('save-button');
    const entriesContainer = document.getElementById('entries-container');

    if (!taskForm || !taskDate || !taskDesc || !taskList || !saveButton || !entriesContainer) {
        console.error('One or more elements are missing from the DOM');
        return;
    }

    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const date = taskDate.value;
        const description = taskDesc.value;

        if (date && description) {
            const taskItem = document.createElement('li');
            taskItem.textContent = `${date}: ${description}`;
            taskList.appendChild(taskItem);

            // Clear the form
            taskDate.value = '';
            taskDesc.value = '';
        }
    });

    saveButton.addEventListener('click', function(event) {
        event.preventDefault();

        const tasks = [];
        taskList.querySelectorAll('li').forEach(taskItem => {
            const [date, ...descriptionParts] = taskItem.textContent.split(': ');
            const description = descriptionParts.join(': ');
            tasks.push({
                date: date,
                description: description
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
                // Check if 'tasks' exists and is an array before using join
                const tasks = entry.tasks && Array.isArray(entry.tasks) ? entry.tasks.join(', ') : 'No tasks available';
                entryTasks.innerText = `Tasks: ${tasks}`;
                entryDiv.appendChild(entryTasks);
                entriesContainer.appendChild(entryDiv);
            });
        });
    }

    // Load entries on page load
    loadEntries();
});
