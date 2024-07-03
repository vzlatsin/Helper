// tabs.js
document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('.tab');
    const tabContents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            tabs.forEach(tab => tab.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            tab.classList.add('active');
            const tabContent = document.getElementById(tab.getAttribute('data-tab'));
            tabContent.classList.add('active');

            // Fetch tasks if the "Today's Tasks" tab is clicked
            if (tab.getAttribute('data-tab') === 'today') {
                fetchTodayTasks();
            }
        });
    });
});
