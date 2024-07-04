# User Interface Functionality

This document provides an overview of the user interface elements and how their functionality is mapped internally through JavaScript.

## Introduction

This document maps the functionality of various user interface elements in the application, showing how they are referenced and handled in the JavaScript code. It focuses on forms and key functionalities to help identify redundant code and potential areas for reuse.

## Forms and Their Functionalities

### 1. Add Task Form
- **Form ID**: `task-form`
- **Purpose**: To add new tasks to the task list.
- **HTML Location**: `task_diary.html`
- **JavaScript Location**: `task_diary.js`
- **Functionality**:
  - **Event**: Form submission when clicking the "Add Task" button.
  - **Handler**: `handleTaskFormSubmit(event)`
  - **Description**: 
    - Collects task details (date, start time, end time, and description).
    - Adds the task to the list displayed on the page.
    - Clears the form fields after adding the task.

## Buttons and Other Interactive Elements

### 1. Save Tasks Button
- **Button ID**: `save-button`
- **Purpose**: To save the list of tasks.
- **HTML Location**: `task_diary.html`
- **JavaScript Location**: `task_diary.js`
- **Functionality**:
  - **Event**: Button click to save tasks.
  - **Handler**: `handleSaveButtonClick(event)`
  - **Description**:
    - Collects all tasks from the list.
    - Sends the tasks to the server to be saved.

### 2. View Tasks for Date Button
- **Purpose**: To view tasks for a specific date.
- **HTML Location**: `task_diary.html`
- **JavaScript Location**: `task_diary.js`
- **Functionality**:
  - **Event**: Button click to view tasks.
  - **Handler**: `viewTasksForDate()`
  - **Description**:
    - Fetches tasks from the server for the specified date.
    - Displays the fetched tasks on the page.

### 3. Select Tasks for Date Button
- **Purpose**: To select tasks for a specific date.
- **HTML Location**: `task_diary.html`
- **JavaScript Location**: `task_diary.js`
- **Functionality**:
  - **Event**: Button click to select tasks.
  - **Handler**: `selectTasksForDate()`
  - **Description**:
    - Allows users to select tasks.
    - Updates the status of selected tasks on the server.

### 4. Move to Closed List Button
- **Button ID**: `move-tasks-button`
- **Purpose**: To move selected tasks to a closed list.
- **HTML Location**: `task_diary.html`
- **JavaScript Location**: `task_diary.js`
- **Functionality**:
  - **Event**: Button click to move tasks.
  - **Handler**: `moveSelectedTasks()`
  - **Description**:
    - Moves selected tasks to a closed list.
    - Updates the status of the tasks on the server.

### 5. Undo Move Button
- **Button ID**: `undo-move-button`
- **Purpose**: To undo the move of tasks to the closed list.
- **HTML Location**: `task_diary.html`
- **JavaScript Location**: `task_diary.js`
- **Functionality**:
  - **Event**: Button click to undo move.
  - **Handler**: `undoMove()`
  - **Description**:
    - Reverts the status of tasks moved to the closed list.
    - Updates the task status on the server.

### 6. Lock Selected Tasks Button
- **Button ID**: `lock-tasks-button`
- **Purpose**: To lock selected tasks.
- **HTML Location**: `task_diary.html`
- **JavaScript Location**: `task_diary.js`
- **Functionality**:
  - **Event**: Button click to lock tasks.
  - **Handler**: `lockSelectedTasks()`
  - **Description**:
    - Locks selected tasks.
    - Updates the task status on the server.

## Key JavaScript Functions

### 1. handleTaskFormSubmit
- **Location**: `task_diary.js`
- **Description**: Handles the submission of the add task form by adding a new task to the list and clearing the form fields.

### 2. handleSaveButtonClick
- **Location**: `task_diary.js`
- **Description**: Gathers tasks from the list and sends them to the server to be saved.

### 3. viewTasksForDate
- **Location**: `task_diary.js`
- **Description**: Fetches and displays tasks for a specific date.

### 4. selectTasksForDate
- **Location**: `task_diary.js`
- **Description**: Selects tasks for a specific date and updates their status on the server.

### 5. moveSelectedTasks
- **Location**: `task_diary.js`
- **Description**: Moves selected tasks to a closed list and updates their status on the server.

### 6. undoMove
- **Location**: `task_diary.js`
- **Description**: Reverts the status of tasks moved to the closed list and updates the task status on the server.

### 7. lockSelectedTasks
- **Location**: `task_diary.js`
- **Description**: Locks selected tasks and updates the task status on the server.

## Event Listeners

### 1. Save Tasks Button
- **Button ID**: `save-button`
- **Location**: `task_diary.js`
- **Description**: Gathers tasks from the list and sends them to the server to be saved.

### 2. View Tasks for Date Button
- **Button ID**: N/A (Inline Event)
- **Location**: `task_diary.js`
- **Description**: Fetches tasks from the server for the specified date and displays them.

### 3. Select Tasks for Date Button
- **Button ID**: N/A (Inline Event)
- **Location**: `task_diary.js`
- **Description**: Allows users to select tasks and updates their status on the server.

### 4. Move to Closed List Button
- **Button ID**: `move-tasks-button`
- **Location**: `task_diary.js`
- **Description**: Moves selected tasks to a closed list and updates their status on the server.

### 5. Undo Move Button
- **Button ID**: `undo-move-button`
- **Location**: `task_diary.js`
- **Description**: Reverts the status of tasks moved to the closed list and updates the task status on the server.

### 6. Lock Selected Tasks Button
- **Button ID**: `lock-tasks-button`
- **Location**: `task_diary.js`
- **Description**: Locks selected tasks and updates the task status on the server.
