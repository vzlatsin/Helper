import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';
import TimeManagement from './components/TimeManagement';

document.addEventListener("DOMContentLoaded", function() {
    const rootElement = document.getElementById('root');
    const timeManagementElement = document.getElementById('time-management-root');
    
    console.log('root element:', rootElement);
    console.log('time-management-root element:', timeManagementElement);

    if (rootElement) {
        console.log('Rendering App on root element');
        ReactDOM.render(<App />, rootElement);
    } else if (timeManagementElement) {
        console.log('Rendering TimeManagement on time-management-root element');
        ReactDOM.render(<TimeManagement />, timeManagementElement);
    } else {
        console.error('No valid root element found');
    }
});
