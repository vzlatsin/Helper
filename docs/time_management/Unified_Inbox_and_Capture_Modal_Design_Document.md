# Unified Inbox and Capture Modal Design Document

### 1. Introduction

**Objective**: 
To add a Unified Inbox and Capture Modal feature to the existing Task Diary application. This feature will allow users to manually capture tasks, ideas, and notes from various sources and organize them effectively.

**Scope**:
- Add a new tab for the Unified Inbox.
- Implement a Capture Modal for quick task input.
- Ensure seamless integration with existing features.

### 2. Features and Requirements

**Unified Inbox Tab**:
- Display a list of captured items from various sources.
- Provide options to move items to the appropriate lists (Today, Tomorrow, Backlog, Reference).

**Capture Modal**:
- Provide a user interface for quickly capturing new tasks, ideas, or notes.
- Include a field for description.
- Implement functionality to add captured items to the Unified Inbox.

**Integration**:
- Ensure the new tab and modal integrate smoothly with the existing tabs and task management features.
- Maintain user-friendly navigation and interaction.

### 3. User Stories

**User Story 1: Capturing an App Development Idea**
- As a user, I want to quickly capture an idea for app development so that I can refer to it later.
- **Example**: "Idea for app development: Add a feature to integrate with social media."

**User Story 2: Capturing a Tax-Related Letter**
- As a user, I want to capture a reminder to address a letter relating to my tax file number so that I don't forget to handle it.
- **Example**: "Letter relating to tax file number: Submit tax documents by end of the month."

**User Story 3: Capturing a Jira Message at Work**
- As a user, I want to capture an important Jira message from work so that I can prioritize it in my task list.
- **Example**: "Jira message: Update project status report by Friday."

**User Story 4: Capturing a Teams Message**
- As a user, I want to capture a Teams message from a colleague so that I can follow up on it later.
- **Example**: "Teams message from John: Review the new feature specs."

### 4. User Interface Design

**Main Page Layout**:
- **Header**: Displays the title "Task Diary" and the current date.
- **Navigation Bar**: Includes tabs for Add Tasks, Today’s Tasks, Forgotten Tasks, Tomorrow’s Tasks, and Unified Inbox.
- **Main Content Area**: Divided into sections corresponding to the tabs.

**Unified Inbox Section**:
- **List of Captured Items**: Displays tasks, ideas, and notes added via the Capture Modal.
- **Move Button**: Allows moving items to the appropriate lists.

**Capture Modal**:
- **Modal Container**: Pop-up window containing the form elements.
- **Close Button**: Allows users to close the modal without submitting.
- **Form Elements**:
  - **Description Input**: Text field for entering the task or idea description.
  - **Submit Button**: Adds the new item to the Unified Inbox.

### 5. Workflow and Interaction

**Morning Routine**:
1. **Review Closed List for Today**: Check tasks planned for today.
2. **Check Inboxes**: Manually review Gmail, work email, and ServiceNow. Capture relevant tasks.
3. **Use Capture Button**: Add new tasks or ideas to the Unified Inbox.

**Throughout the Day**:
1. **Work on Closed List Tasks**: Focus on completing today's tasks.
2. **Capture New Items**: Use the Capture Button to add spontaneous tasks or ideas to the Unified Inbox without altering today's closed list.

**Evening Routine**:
1. **Review and Process Unified Inbox**: Categorize and organize captured items.
2. **Reflect on Completed Tasks**: Review the closed list and note any quick wins.
3. **Plan for Tomorrow**: Set tasks for the next day, incorporating tasks captured during the day.

### 6. Backend Design

**Database Changes**:
- **Unified Inbox Table**: Create a new table in `init_db.py` to store captured items.
  - **Table Name**: `unified_inbox`
  - **Columns**:
    - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
    - `description` (TEXT NOT NULL)

**API Endpoints**:
1. **GET /unified-inbox**
   - **Description**: Retrieve all captured items.
   - **Response**: List of captured items.

2. **POST /unified-inbox**
   - **Description**: Add a new item to the Unified Inbox.
   - **Request Body**: { "description": "Task description" }
   - **Response**: Status and new item details.

3. **PUT /unified-inbox/:id**
   - **Description**: Update a captured item.
   - **Request Body**: { "description": "Updated task description" }
   - **Response**: Status and updated item details.

4. **DELETE /unified-inbox/:id**
   - **Description**: Delete an item from the Unified Inbox.
   - **Response**: Status and deleted item details.

### 7. Data Access Layer Changes

To support the new Unified Inbox feature, the `data_access.py` file will need to be updated to include new functions for managing the Unified Inbox.

**New Functions**:

1. **Insert a new item into the Unified Inbox**
   - **Function**: `insert_unified_inbox_item(conn, description)`
   - **Description**: Inserts a new item into the `unified_inbox` table.
   - **Parameters**: `conn` (Database connection), `description` (Text description of the item)

2. **Fetch all items from the Unified Inbox**
   - **Function**: `fetch_unified_inbox_items(conn)`
   - **Description**: Fetches all items from the `unified_inbox` table.
   - **Parameters**: `conn` (Database connection)

3. **Update an item in the Unified Inbox**
   - **Function**: `update_unified_inbox_item(conn, item_id, description)`
   - **Description**: Updates the description of an item in the `unified_inbox` table.
   - **Parameters**: `conn` (Database connection), `item_id` (ID of the item), `description` (New description of the item)

4. **Delete an item from the Unified Inbox**
   - **Function**: `delete_unified_inbox_item(conn, item_id)`
   - **Description**: Deletes an item from the `unified_inbox` table.
   - **Parameters**: `conn` (Database connection), `item_id` (ID of the item)

### 8. Technical Design

**HTML Changes**:
- Add a new tab for the Unified Inbox.
- Create the Capture Modal structure.

**CSS Updates**:
- Style the Unified Inbox tab and Capture Modal for consistency with the existing design.

**JavaScript Functionality**:
- Create a new JavaScript file `unified_inbox.js` for the Capture Modal functionality.
- Implement event listeners for opening and closing the modal.
- Add logic to handle form submission and categorization.

**Server-Side Logic**:
- Implement the new API endpoints in the backend.
- Update the database schema to include the Unified Inbox table.

### 9. Implementation Plan

**Step 1: Update HTML**: Add the Unified Inbox tab and section, Capture Modal structure.
**Step 2: Create CSS Styles**: Style the new tab and modal.
**Step 3: Develop JavaScript Functionality**: Create `unified_inbox.js`, handle modal logic.
**Step 4: Implement Backend Endpoints**: Develop new API endpoints, update the database schema.
**Step 5: Integration and Testing**: Integrate new features, perform testing.
**Step 6: Documentation and Deployment**: Document new features, deploy the updated application.

### 10. Risks and Mitigations

**Potential Risks**:
- Integration Issues.
- User Confusion.

**Mitigations**:
- Thorough Testing.
- User Training.

### 11. Conclusion

The Unified Inbox and Capture Modal feature will enhance the Task Diary application by providing a streamlined way to capture and organize tasks, ideas, and notes.

