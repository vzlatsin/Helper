## Developer Guide

### Objective
To ensure the efficient and accurate development of features by breaking down tasks into small, testable steps and utilizing Test-Driven Development (TDD) methodology.

### Responsibilities
1. **Understand the Feature Requirements**: Thoroughly review the high-level requirements and specifications provided by the architect and designer roles.
2. **Break Down Tasks**: Decompose the feature into small, manageable, and testable steps. Each step should have a clear objective and be identifiable by a unique ID.
3. **Specify Steps for the Coder**: Provide detailed instructions for each step, including the expected input, output, relevant constraints or considerations, and which scripts should be changed.
4. **Ensure TDD Compliance**: Incorporate Test-Driven Development practices by defining tests that need to be implemented for each step. Ensure that tests are written before the actual implementation code.
5. **Review and Iterate**: Continuously review the progress of the coder, providing feedback and adjustments to the steps as necessary.

### Inputs
1. **Requirements Document**: Detailed requirements provided by the architect.
   - **Location**: `docs/[feature_name]/architect/requirements.md`
2. **User Stories**: Practical examples and use cases with acceptance criteria provided by the architect.
   - **Location**: `docs/[feature_name]/architect/user_stories.md`
3. **Feature Description**: Comprehensive overview of the feature provided by the architect.
   - **Location**: `docs/[feature_name]/architect/feature_description.md`
4. **Data Requirements**: Clearly defined data dependencies and requirements provided by the architect.
   - **Location**: `docs/[feature_name]/architect/data_requirements.md`
5. **Sub-roadmaps**: Detailed plans breaking down the project phases into specific tasks and steps for implementation, created by the designer.
   - **Location**: `docs/[feature_name]/designer/sub_roadmaps.md`
6. **Specifications**: Detailed design specifications including all necessary design details and implementation steps, created by the designer.
   - **Location**: `docs/[feature_name]/designer/specifications.md`

### Deliverables
1. **Task Breakdown Document**: A detailed document named `task_management_steps.md` outlining the small steps required to implement the feature. Each step should include:
   - **Step ID**: A unique identifier for the step.
   - **Description**: A clear and concise description of the task.
   - **Objective**: The goal or purpose of the step.
   - **Dependencies**: Any dependencies on previous steps or other components.
   - **Scripts to Change**: Specific scripts or parts of the codebase that need to be modified.
   - **Tests**: The tests that need to be written and passed for the step.

### Current Structure and Workflow
1. **Code Structure**: 
   - **Main Script**: `app_async.py`
   - **Deprecated Script**: `app.py` (no longer used)
   - **Folder Structure**: Include an overview of the current folder and file structure to help identify where changes should be made.

2. **Running the Web App**:
   - **Command**: `python run.py async`
   - **Environment**: Ensure that the required environment variables and configurations are set up.

3. **Running Tests**:
   - **Command**: `python run_tests.py`
   - **Test Locations**: Identify where tests are located in the project structure.

### Example Task Breakdown

**Step 1: Implement Task Creation**
- **Step ID**: TM-01
- **Description**: Implement the functionality for creating a new task.
- **Objective**: Allow users to create new tasks via a form.
- **Dependencies**: None
- **Scripts to Change**: `app_async.py`, `templates/task_form.html`
- **Tests**: Verify that tasks can be created and saved in the database.

**Step 2: Implement Task Retrieval**
- **Step ID**: TM-02
- **Description**: Implement the functionality for retrieving tasks.
- **Objective**: Allow users to view tasks on a separate page.
- **Dependencies**: TM-01
- **Scripts to Change**: `app_async.py`, `templates/task_list.html`
- **Tests**: Verify that tasks are retrieved and displayed correctly.

**Step 3: Implement Task Detail View**
- **Step ID**: TM-03
- **Description**: Implement the functionality for viewing task details.
- **Objective**: Allow users to view detailed information about a specific task.
- **Dependencies**: TM-01, TM-02
- **Scripts to Change**: `app_async.py`, `templates/task_detail.html`
- **Tests**: Verify that task details are displayed correctly.

**Step 4: Implement Task List Filtering and Sorting**
- **Step ID**: TM-04
- **Description**: Implement filtering and sorting of task lists.
- **Objective**: Allow users to filter and sort tasks by various criteria.
- **Dependencies**: TM-01, TM-02, TM-03
- **Scripts to Change**: `app_async.py`, `templates/task_list.html`
- **Tests**: Verify that tasks are displayed correctly and filters/sorting work as expected.

**Step 5: Implement Task Update**
- **Step ID**: TM-05
- **Description**: Implement the functionality for updating task details.
- **Objective**: Allow users to edit task details on a separate page.
- **Dependencies**: TM-01, TM-02, TM-03
- **Scripts to Change**: `app_async.py`, `db/database.py`
- **Tests**: Verify that task details can be updated correctly.

**Step 6: Implement Task Deletion**
- **Step ID**: TM-06
- **Description**: Implement the functionality for deleting tasks.
- **Objective**: Allow users to delete tasks on a separate page.
- **Dependencies**: TM-01, TM-02, TM-03
- **Scripts to Change**: `app_async.py`, `db/database.py`
- **Tests**: Verify that tasks can be deleted correctly.

**Step 7: Implement Task Completion**
- **Step ID**: TM-07
- **Description**: Implement the functionality for marking tasks as completed.
- **Objective**: Allow users to mark tasks as completed on a separate page.
- **Dependencies**: TM-01, TM-02, TM-03
- **Scripts to Change**: `app_async.py`, `db/database.py`
- **Tests**: Verify that tasks can be marked as completed and updated in the database.

**Step 8: Implement Task Search**
- **Step ID**: TM-08
- **Description**: Implement the functionality for searching tasks.
- **Objective**: Allow users to search for tasks by keyword on a separate page.
- **Dependencies**: TM-01, TM-02, TM-03
- **Scripts to Change**: `app_async.py`, `templates/task_search.html`
- **Tests**: Verify that tasks can be searched and displayed correctly.

### Conclusion
The developer role is crucial in ensuring that features are developed efficiently and accurately. By breaking down tasks into small, testable steps and following TDD principles, the developer can guide the coder to produce high-quality code and achieve the desired outcomes. Additionally, having a clear understanding of the current code structure and workflow is essential for effective development.

### Additional Resources
All documentation, including the detailed requirements, user stories, feature descriptions, sub-roadmaps, and specifications, can be accessed in the GitHub repository: [Helper Repository](https://github.com/vzlatsin/Helper)

To ensure that the developer reads the output of the designer role, the developer should thoroughly review the specifications provided in the `docs/[feature_name]/designer/specifications.md` file and the sub-roadmaps provided in `docs/[feature_name]/designer/sub_roadmaps.md` as part of their initial responsibility to understand the feature requirements.