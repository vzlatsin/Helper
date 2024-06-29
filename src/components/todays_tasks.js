document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed for Today\'s Tasks');

    const taskList = document.getElementById('tasks-list');
    const taskForm = document.getElementById('task-form');
    const taskDescription = document.getElementById('task-description');
    const saveButton = document.getElementById('save-button');
    const reviewButton = document.getElementById('review-button');

    if (!taskForm || !taskDescription || !taskList || !saveButton || !reviewButton) {
        console.error('One or more elements are missing from the DOM');
        return;
    }

    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const taskDescriptionValue = taskDescription.value;

        if (taskDescriptionValue) {
            const taskItem = document.createElement('li');
            taskItem.textContent = taskDescriptionValue;
            taskList.appendChild(taskItem);

            // Clear the form
            taskDescription.value = '';
        }
    });

    saveButton.addEventListener('click', function(event) {
        event.preventDefault();
        const tasks = [];
        taskList.querySelectorAll('li').forEach(taskItem => {
            tasks.push(taskItem.textContent);
        });

        fetch('/save-todays-tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ tasks: tasks })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Tasks saved successfully!');
            } else {
                alert('Error saving tasks.');
            }
        });
    });

    reviewButton.addEventListener('click', function() {
        console.log('Review button clicked');
        fetch('/get-todays-tasks')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(entries => {
                console.log('Entries received', entries);
                if (Array.isArray(entries)) {
                    taskList.innerHTML = ''; // Clear previous tasks
                    entries.forEach(entry => {
                        const listItem = document.createElement('li');
                        listItem.textContent = entry.description;
                        taskList.appendChild(listItem);
                    });
                } else {
                    console.error('Received data is not an array');
                }
            })
            .catch(error => {
                console.error('Error fetching tasks:', error);
            });
    });
});
