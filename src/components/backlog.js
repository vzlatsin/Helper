document.addEventListener('DOMContentLoaded', function() {
    // Function to fetch and display backlog tasks
    async function fetchBacklogTasks() {
        const backlogContainer = document.getElementById('backlog-tasks');
        
        // Ensure the element exists before trying to modify it
        if (!backlogContainer) {
            console.error('Element with ID "backlog-tasks" not found in the DOM.');
            return;
        }
        
        try {
            const response = await fetch('/tasks/backlog');
            const tasks = await response.json();

            backlogContainer.innerHTML = '';  // Clear previous tasks

            if (tasks.length === 0) {
                backlogContainer.innerHTML = '<p>No backlog tasks available.</p>';
            } else {
                tasks.forEach(task => {
                    const taskItem = document.createElement('li');
                    taskItem.textContent = task.task_description;
                    backlogContainer.appendChild(taskItem);
                });
            }
        } catch (error) {
            console.error('Error fetching backlog tasks:', error);
        }
    }

    // Call the function to fetch and display backlog tasks on page load
    fetchBacklogTasks();
});
