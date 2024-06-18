import React, { useState } from 'react';

function TimeManagement() {
    const [date, setDate] = useState('');
    const [startTime, setStartTime] = useState('');
    const [endTime, setEndTime] = useState('');
    const [taskDescription, setTaskDescription] = useState('');
    const [tasks, setTasks] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const newTask = { date, startTime, endTime, taskDescription };
        setTasks(prevTasks => [...prevTasks, newTask]); // Correct state update
        console.log('Task added:', newTask); // Debug log
        // Reset form fields
        setDate('');
        setStartTime('');
        setEndTime('');
        setTaskDescription('');
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="date">Date</label>
                <input id="date" type="date" value={date} onChange={(e) => setDate(e.target.value)} required /><br />

                <label htmlFor="start-time">Start Time</label>
                <input id="start-time" type="time" value={startTime} onChange={(e) => setStartTime(e.target.value)} required /><br />
                
                <label htmlFor="end-time">End Time</label>
                <input id="end-time" type="time" value={endTime} onChange={(e) => setEndTime(e.target.value)} required /><br />
                
                <label htmlFor="task-description">Task Description</label>
                <input id="task-description" type="text" value={taskDescription} onChange={(e) => setTaskDescription(e.target.value)} required /><br />
                
                <button type="submit">Submit</button>
            </form>
            <h3>Submitted Tasks</h3>
            <ul>
                {tasks.map((task, index) => (
                    <li key={index}>
                        {task.date} - {task.startTime} to {task.endTime}: {task.taskDescription}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TimeManagement;
