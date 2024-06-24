### Coder Guide

**Purpose**  
To ensure the creation of detailed and clear code based on the developer's instructions and specifications.

**Responsibilities**  
1. **Interpret Developer Deliverables**: Understand script instructions and data flow guidelines.
2. **Write Code**: Implement the code based on the provided specifications.
3. **Ensure Clarity and Completeness**: Make sure the code is well-documented and meets all specified requirements.

**Inputs**:
1. **Script Instructions**: Detailed instructions for coding.
2. **HTML Structure Plan**: Plan for the HTML structure and any changes needed.
3. **Code Changes**: Specific details on the changes to be made in the codebase.
4. **Data Flow and Interaction Guidelines**: Detailed guidelines on data flow and user interactions.

## Task Breakdown and Documentation Process

To maintain a structured and test-driven development approach, follow these steps for each feature:

1. **Create Detailed Task Documents**: For each feature, create a `.md` document with unique IDs for each task.
2. **Break Down Tasks**: Divide each feature into smaller, testable tasks.
3. **Follow TDD**: Write tests for each task before implementing it.
4. **Document Tests and Changes**: Ensure each task document includes descriptions, objectives, dependencies, scripts to change, and tests.
5. **Commit and Push**: Regularly commit changes and push to the repository.

Refer to `time_management_feature_tasks.md` for an example of task breakdown.

**Outputs**:
1. **Implemented Code**:
   - Code that follows the developer's specifications.
   - **Location**: `src/[feature_name]/`
2. **Test Results**:
   - Comprehensive testing results covering all use cases.
   - **Location**: `tests/[feature_name]/`
3. **Documentation**:
   - Detailed documentation of the implemented code and its usage.
   - **Location**: `docs/[feature_name]/coder/`

**Existing Project Structure**:

```
src/
├── components/
│   └── [ComponentName].js
├── tests/
│   └── [ComponentName].test.js
├── templates/
│   └── [TemplateName].html
```

**Process**  
1. **Gather Inputs**:
   - **Sources**: Script instructions, HTML structure plans, and data flow guidelines from the developer.

2. **Write Code**:
   - Implement the code following the provided instructions.
   - Ensure the code is clean, well-documented, and adheres to best practices.
   - Follow a TDD approach: write tests before implementing functionality.
   - Adhere to the philosophy of "test early, test often": make small incremental steps with early and frequent testing.

3. **Test and Validate**:
   - Conduct comprehensive testing covering all use cases.
   - Run tests using `run_tests.py`.
   - Document the test results and ensure all scenarios are covered.

4. **Document**:
   - Write detailed documentation explaining the code and its usage.
   - Ensure clarity and completeness in the documentation.

**Formatting, Style, and Review**:
1. **Formatting**:
   - Follow consistent formatting (e.g., headings, bullet points).
   - Use standardized templates for all documentation.
   - Example:
     ```markdown
     ## Formatting Guidelines
     - Use `#` for main headings.
     - Use `##` for subheadings.
     - Use `-` for bullet points.
     - Use `1.` for numbered lists.
     ```

2. **Style**:
   - Ensure a consistent writing style (e.g., tone, tense) across all documentation.
   - Follow a coding style guide to maintain uniformity.
   - Example:
     ```markdown
     ## Style Guide
     - Use meaningful variable names.
     - Write comments in the present tense.
     - Use clear and concise language.
     ```

3. **Review Process**:
   - Implement a review process to check for consistency before finalizing deliverables.
   - Have another team member or auditor review the code and documentation.
   - Example:
     ```markdown
     ## Review Checklist
     - Check for consistent terminology.
     - Verify formatting guidelines are followed.
     - Ensure the writing style is uniform.
     - Have code and documentation reviewed by a peer or auditor.
     ```

**Review Checklist for Auditor**  
1. **Clarity**: Ensure the code and documentation are clear and understandable.
2. **Completeness**: Check that all necessary components are included.
3. **Relevance**: Confirm the code meets the developer's specifications.
4. **Consistency**: Ensure the code and documentation are uniform in style and format.
5. **Functionality**: Assess the correctness and performance of the code.

**Feedback and Iteration**  
- Ensure deliverables include room for feedback and iteration.
- Define procedures for handling incomplete or unclear inputs.

### GitHub Repository
- All inputs and outputs should be stored in the GitHub repository.
- **Developer Deliverables**: Located in `docs/[feature_name]/developer/`
- **Implemented Code**: Located in `src/[feature_name]/`
- **Test Results**: Located in `tests/[feature_name]/`
- **Documentation**: Located in `docs/[feature_name]/coder/`

### Running Tests
- Use `run_tests.py` to execute all tests.
- Ensure the script is updated to include the new tests for the time management feature.

### Section for Continuity with ChatGPT
1. **Session Log**:
   - Maintain a session log documenting what was done and what needs to be done next.
   - Include the task name and ID in the session log.
   - Example:
     ```markdown
     ## Session Log
     ### Current Session:
     - Implemented initial time management feature.
     - Set up tests.

     ### Next Steps:
     1. Add form for time management tasks.
     2. Write tests for the form functionality.
     3. Implement the form in the frontend.
     ```

#### Example Task Document: `time_management_feature_tasks.md`

```markdown
# Time Management Feature

## TM-001-01: Task Creation for Time Management

**Description**: Design and implement the time tracking form.  
**Objective**: Allow users to log time.  
**Dependencies**: None  
**Scripts to Change**: `templates/time_form.html`  
**Tests**: Verify form display and input validation.

### Session Log

#### TM-001-01: Task Creation for Time Management

**Description**: Design and implement the time tracking form on a dedicated page.
**Objective**: Allow users to log time on a separate Time Management page.
**Dependencies**: None
**Scripts to Change**: `time_management.html`, `TimeManagement.js`, `index.js`
**Tests**: Verify form display and input validation.

### Implemented Steps:
1. **Create `time_management.html`**
   - Added the HTML structure for the Time Management page with the form.

2. **Write Initial Tests**
   - Ensured the form is displayed correctly in the browser.

3. **Implement the Form in React**
   - Added the form logic to `TimeManagement.js`.

4. **Render the Component**
   - Used `index.js` to render the `TimeManagement` component.

5. **Run Tests**
   - Verified the form's appearance and functionality.
```



**User Guide Updates**
- **Purpose**: Ensure the user guide remains up-to-date with application changes.
- **Steps**:
  1. **Review Changes**: After implementing new features or updates.
  2. **Update User Guide**: Add or modify relevant sections in the `user_guide.md`.
  3. **Include Examples**: Provide examples and usage instructions if applicable.
  4. **Verify Accuracy**: Ensure the information is accurate and clear.

**Task Management Documentation**
- **Ensure** all task-related changes are reflected in the documentation.
- **Maintain** consistency between the implementation and the documented features.

**Example Workflow**
1. **Implement Feature**: Complete the feature as per the task document.
2. **Update User Guide**: Reflect the changes in the user guide.
3. **Review Documentation**: Ensure all relevant documents are updated.

[View the full coder guide](https://github.com/vzlatsin/Helper/blob/master/docs/guides/coder_guide.md)