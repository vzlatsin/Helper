

### Developer Guide

**Purpose**  
To ensure the creation of detailed and clear code instructions that guide the coder effectively.

**Responsibilities**  
1. **Interpret Designer Deliverables**: Understand sub-roadmaps, specifications, and design validations.
2. **Create Development Deliverables**: Produce pseudocode and script instructions.
3. **Ensure Clarity and Completeness**: Make sure all deliverables are comprehensive and easily understandable by the coder.

**Inputs**:
1. **Sub-roadmaps**: Detailed plans breaking down the project phases.
   - **Location**: `docs/[feature_name]/designer/`
2. **Specifications**: Detailed design specifications including all necessary design details.
   - **Location**: `docs/[feature_name]/designer/`
3. **Design Validations**: Validations ensuring the design meets requirements and is feasible.
   - **Location**: `docs/[feature_name]/designer/`

**Outputs**:
1. **Pseudocode**:
   - **File Name**: `pseudocode_new_feature.md`
   - **Location**: `docs/[feature_name]/developer/`
   - **Content Example**:
     ```markdown
     # Pseudocode for [Feature Name]

     ## Backend Logic
     - Function: add_task(task_name, start_time, end_time)
       - Insert task details into the database
       - Return success/failure response

     ## Frontend Logic
     - Display task list
       - Fetch tasks from the backend
       - Render tasks in the UI

     ## Data Flow
     - User interacts with the UI to add, edit, or delete tasks.
     - Frontend sends requests to backend API.
     - Backend processes requests and interacts with the database.
     - Backend returns responses to the frontend.
     - Frontend updates the UI based on the responses.
     ```

2. **Script Instructions**:
   - **File Name**: `script_instructions.md`
   - **Location**: `docs/[feature_name]/developer/`
   - **Content Example**:
     ```markdown
     # Script Instructions for [Feature Name]

     ## Backend Logic
     ### Database Schema
     1. **Create Time Management Table**:
        - Table Name: `time_management`
        - Fields:
          - `task_id` (Primary Key, Integer, Auto-increment)
          - `task_name` (String, Not Null)
          - `start_time` (DateTime, Not Null)
          - `end_time` (DateTime, Not Null)
          - `status` (String, Default: 'Pending')

     ### API Endpoints
     1. **Add Task Endpoint**
        - **Route**: `/api/add_task`
        - **Method**: `POST`
        - **Parameters**: `task_name`, `start_time`, `end_time`
        - **Function**: `add_task(task_name, start_time, end_time)`
        - **Description**: Insert task details into the database and return a success/failure response.

     ## Frontend Logic
     ### HTML Structure
     1. **Task List Display**:
        - Create a table to display tasks with columns for `task_name`, `start_time`, `end_time`, and `status`.
        - Add buttons for editing and deleting tasks in each row.

     ### JavaScript Functions
     1. **Fetch Tasks**:
        - Function: `fetchTasks()`
        - Description: Send a GET request to `/api/get_tasks` and populate the task list table.

     ## Error Handling
     - Handle database connection errors
     - Validate user inputs
     - Provide user feedback for success/failure actions
     ```

3. **HTML Structure Plan**:
   - **File Name**: `html_structure_plan.md`
   - **Location**: `docs/[feature_name]/developer/`
   - **Content Example**:
     ```markdown
     # HTML Structure Plan for [Feature Name]

     ## Task List Display
     - Create a table with the following columns:
       - Task Name
       - Start Time
       - End Time
       - Status
       - Actions (Edit/Delete buttons)

     ## Task Form
     - Create a form with the following fields:
       - Task Name (input text)
       - Start Time (datetime picker)
       - End Time (datetime picker)
       - Status (dropdown)

     ## Modifications
     - Add the form to the existing HTML template for task management.
     - Ensure the new elements are styled consistently with the existing UI.
     ```

4. **Code Changes**:
   - **File Name**: `code_changes.md`
   - **Location**: `docs/[feature_name]/developer/`
   - **Content Example**:
     ```markdown
     # Code Changes for [Feature Name]

     ## Backend
     - Add the following function to `app_async.py`:
       ```python
       def add_task(task_name, start_time, end_time):
           sql = "INSERT INTO time_management (task_name, start_time, end_time) VALUES (?, ?, ?)"
           execute_sql(sql, (task_name, start_time, end_time))
       ```

     ## Frontend
     - Add the following function to `scripts.js`:
       ```javascript
       function fetchTasks() {
           fetch('/api/get_tasks')
               .then(response => response.json())
               .then(data => renderTaskList(data));
       }
       ```

     ## Integration
     - Update the routes in `routes.py` to include the new API endpoints.
     ```

5. **Data Flow and Interaction Guidelines**:
   - **File Name**: `data_flow_interaction.md`
   - **Location**: `docs/[feature_name]/developer/`
   - **Content Example**:
     ```markdown
     # Data Flow and Interaction Guidelines for [Feature Name]

     ## User Interactions
     - User adds, edits, or deletes tasks via the UI.
     - User actions trigger JavaScript functions to send API requests.

     ## Backend Processing
     - API requests are processed by backend functions.
     - Database operations are performed, and responses are returned to the frontend.

     ## Frontend Updates
     - API responses are handled by JavaScript functions.
     - The task list is updated in the UI based on the API responses.

     ## Error Handling
     - Standardize error responses with HTTP status codes.
     - Provide user-friendly error messages.
     ```

### Process
1. **Familiarize with Current Codebase**:
   - **Action**: Explore the project structure by reviewing the codebase on the project's GitHub repository.
   - **GitHub Repository Location**: `https://github.com/vzlatsin/Helper`
   - **Focus Areas**: 
     - `app_async.py`: Main application logic.
     - `helper.py`: Utility functions.
     - `models.py`: Data models and database interactions.
     - `routes.py`: API routes and endpoints.
     - `templates/`: HTML templates and static files.
   - **Outcome Expected**: Gain a thorough understanding of the codebase and its structure.

2. **Review Designer Deliverables**:
   - **Action**: Carefully review the sub-roadmaps, specifications, and design validations.
   - **Details**: Understand the requirements, design details, and feasibility checks.
   - **Outcome Expected**: Ensure a clear understanding of what needs to be developed.

3. **Draft Pseudocode**:
   - **Action**: Create a logical representation of the new feature.
   - **Details**: Break down the feature into smaller, manageable components.
   - **Outcome Expected**: Provide a clear plan for coding.

4. **Develop Script Instructions**:
   - **Action**: Write detailed instructions for the coder.
   - **Details**: Include steps, methods, and functions needed for implementation.
   - **Outcome Expected**: Ensure the coder can follow the instructions without confusion.

5. **Plan HTML Structure**:
   - **Action**: Develop a plan for any necessary changes to the HTML structure.
   - **Details**: Specify new sections, elements, and templates.
   - **Outcome Expected**: Ensure the front-end layout supports the new feature.

6. **Document Code Changes**:
   - **Action**: Detail specific changes to be made in the codebase.
   - **Details**: Include file names, line numbers, and code snippets.
   - **Outcome Expected**: Provide a clear guide for the coder to update the codebase.

7. **Create Data Flow and Interaction Guidelines**:
   - **Action**: Document the flow of data and user interactions.
   - **Details**: Outline backend and frontend interactions, data processing, and user actions.
   - **Outcome Expected**: Ensure a seamless user experience and efficient data handling.

8. **Final Review and Adjustments**:
   - **Action**: Review all documents and make necessary adjustments.
   - **Outcome Expected**: Ensure completeness, consistency, and accuracy before handing off to the coder.

**Consistency Checks**:
1. **Terminology**:
   - Ensure the same terms are used consistently across all documents.
   - Create a glossary of terms if necessary.

2. **Formatting**:
   - Verify all documents follow the same formatting guidelines (e.g., headings, bullet points, numbering).
   - Use standardized templates for all documents.

3. **Style**:
   - Ensure a consistent writing style (e.g., tone, tense) across all documents.
   - Follow a style guide to maintain uniformity.

4. **Review Process**:
   - Implement a review process to check for consistency before deliverables are passed to the coder.
   - Have another

 team member or auditor review the documents.

**Review Checklist for Auditor**  
1. **Clarity**: Ensure the deliverables are clear and understandable for the coder.
2. **Completeness**: Check that all necessary components are included.
3. **Relevance**: Confirm the deliverables are directly useful to the coder.
4. **Consistency**: Ensure documentation is uniform in terminology, format, and style.
5. **Feasibility**: Assess the realism and technical feasibility of the pseudocode and script instructions.

**Feedback and Iteration**  
- Ensure deliverables include room for feedback and iteration.
- Define procedures for handling incomplete or unclear inputs.

