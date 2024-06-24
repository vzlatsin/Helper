import React, { useState } from 'react';

function TimeManagement() {
    const [date, setDate] = useState('');
    const [startTime, setStartTime] = useState('');
    const [endTime, setEndTime] = useState('');
    const [taskDescription, setTaskDescription] = useState('');
    const [tasks, setTasks] = useState([]);
    const [errorMessage, setErrorMessage] = useState('');

    const validateTimeInput = (time) => {
        const timePattern = /^([01]\d|2[0-3]):([0-5]\d)$/;
        return timePattern.test(time);
    };

    const isEndTimeAfterStartTime = (start, end) => {
        return start < end;
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Validate time inputs
        if ((startTime && !endTime) || (!startTime && endTime)) {
            setErrorMessage('Both start time and end time must be provided');
            return;
        }

        if (startTime && endTime) {
            if (!validateTimeInput(startTime) || !validateTimeInput(endTime)) {
                setErrorMessage('Invalid time format');
                return;
            }

            if (!isEndTimeAfterStartTime(startTime, endTime)) {
                setErrorMessage('End time must be after start time');
                return;
            }
        }

        const newTask = { date, startTime: startTime || '00:00', endTime: endTime || '00:00', taskDescription };
        setTasks(prevTasks => [...prevTasks, newTask]); // Correct state update
        console.log('Task added:', newTask); // Debug log
        // Reset form fields
        setDate('');
        setStartTime('');
        setEndTime('');
        setTaskDescription('');
        setErrorMessage('');
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label htmlFor="date">Date</label>
                <input id="date" type="date" value={date} onChange={(e) => setDate(e.target.value)} required/><br />

                <label htmlFor="start-time">Start Time</label>
                <input id="start-time" type="time" value={startTime} onChange={(e) => setStartTime(e.target.value)} /><br />
                
                <label htmlFor="end-time">End Time</label>
                <input id="end-time" type="time" value={endTime} onChange={(e) => setEndTime(e.target.value)} /><br />
                
                <label htmlFor="task-description">Task Description</label>
                <input id="task-description" type="text" value={taskDescription} onChange={(e) => setTaskDescription(e.target.value)} required /><br />
                
                <button type="submit">Submit</button>
            </form>
            {errorMessage && <p style={{color: 'red'}}>{errorMessage}</p>}
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

