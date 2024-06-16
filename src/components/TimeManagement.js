import React, { useState } from 'react';

function TimeManagement() {
    const [startTime, setStartTime] = useState('');
    const [endTime, setEndTime] = useState('');
    const [taskDescription, setTaskDescription] = useState('');
    const [tasks, setTasks] = useState([]);

    return (
        <form>
            <label htmlFor="start-time">Start Time</label>
            <input id="start-time" type="time" value={startTime} onChange={(e) => setStartTime(e.target.value)} />
            
            <label htmlFor="end-time">End Time</label>
            <input id="end-time" type="time" value={endTime} onChange={(e) => setEndTime(e.target.value)} />
            
            <label htmlFor="task-description">Task Description</label>
            <input id="task-description" type="text" value={taskDescription} onChange={(e) => setTaskDescription(e.target.value)} />
            
            <button type="submit">Submit</button>
        </form>
    );
}

export default TimeManagement;
