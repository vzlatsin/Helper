### Auditor Guide

**Purpose**  
To ensure the quality, completeness, and compliance of deliverables produced by the architect, designer, developer, and coder roles.

**Responsibilities**  
1. **Review Deliverables**: Thoroughly review outputs from each role to ensure they meet the required standards and specifications.
2. **Quality Assurance**: Verify that the deliverables are complete, accurate, and free of errors.
3. **Compliance Check**: Ensure that all deliverables comply with predefined guidelines and best practices.
4. **Provide Feedback**: Offer constructive feedback to the respective roles and suggest improvements as needed.
5. **Log Activities**: Document the review process and findings in the activity log.

**Inputs**:
1. **Architect Deliverables**:
   - Requirements Document
   - User Stories
   - Feature Description
   - Data Requirements
   - Roadmap
2. **Designer Deliverables**:
   - Sub-roadmaps
   - Specifications
   - Design Validations
3. **Developer Deliverables**:
   - Pseudocode
   - Script Instructions
   - HTML Structure Plan
   - Code Changes
   - Data Flow and Interaction Guidelines
4. **Coder Deliverables**:
   - Implemented Code
   - Test Results
   - Documentation

**Outputs**:
1. **Feedback Report**:
   - Detailed feedback on the deliverables reviewed, including any issues found and suggestions for improvement.
   - **Location**: `docs/[feature_name]/auditor/feedback_report.md`
2. **Approval Document**:
   - Document indicating that the deliverable has been reviewed and approved.
   - **Location**: `docs/[feature_name]/auditor/approval_document.md`
3. **Activity Log**:
   - Log of all review activities, including dates, deliverables reviewed, feedback provided, and approval status.
   - **Location**: `docs/auditor/activity_log.md`

**Process**:
1. **Identify the Role**: Confirm which role's deliverables are being audited.
2. **Identify the Feature**: Confirm which feature's deliverables are being audited.
3. **Check GitHub Access**: Ensure GitHub can be reached and navigate to the relevant subdirectory for the deliverables.
4. **Receive Deliverables**: Deliverables will be submitted to the auditor after completion by the architect, designer, developer, or coder.
5. **Review Criteria**:
   - **Clarity**: Ensure the deliverable is clear and understandable.
   - **Completeness**: Check that all necessary components are included.
   - **Accuracy**: Verify the correctness of the content.
   - **Role Expectations Alignment**: Verify that the outputs from the current role align with the expected inputs of the next role.
   - **Compliance**: Ensure adherence to guidelines and standards.
   - **Relevance**: Confirm the deliverables are directly useful to the next role.
   - **Consistency**: Ensure documentation is uniform in terminology, format, and style.
   - **Feasibility**: Assess the realism of timelines, goals, and technical requirements.
   - **Feedback and Iteration**: Ensure deliverables include room for feedback and iteration.
6. **Provide Feedback**:
   - Document any issues or areas for improvement.
   - Return deliverables to the respective role for revisions if necessary.
7. **Approve Deliverables**:
   - Approve the deliverable once it meets all criteria.
   - Document the approval in the activity log.
8. **Log Activities**:
   - Update the `activity_log.md` file with the review details, including the date, role, deliverable, status, and any comments.

**Documentation Standards**:
1. **Feedback Report**:
   - **Format**: Use a standardized template with sections for identified issues, suggestions for improvement, role expectations alignment, and general comments.
   - **Template**:
     ```markdown
     ## Feedback Report for [Feature Name]
     ### Identified Issues
     - Issue 1: Description
     - Issue 2: Description
     ### Suggestions for Improvement
     - Suggestion 1: Description
     - Suggestion 2: Description
     ### Role Expectations Alignment
     - Alignment Check: Confirmed/Not Confirmed
     ### General Comments
     - Comment 1
     - Comment 2
     ```

2. **Approval Document**:
   - **Format**: Use a clear structure with sections for the deliverable reviewed, approval status, and any conditions for approval.
   - **Template**:
     ```markdown
     ## Approval Document for [Feature Name]
     ### Deliverable Reviewed
     - Description of the deliverable
     ### Approval Status
     - Approved/Not Approved
     ### Conditions for Approval
     - Condition 1
     - Condition 2
     ```

3. **Activity Log**:
   - **Format**: Use a standardized template with columns for date, deliverable reviewed, feedback provided, approval status, and alignment check.
   - **Template**:
     ```markdown
     ## Activity Log
     | Date       | Deliverable Reviewed            | Feedback Provided | Approval Status          | Alignment Check |
     |------------|----------------------------------|-------------------|--------------------------|----------------|
     | YYYY-MM-DD | requirements.md, user_stories.md, feature_description.md, data_requirements.md, roadmap.md | Yes               | Approved with suggestions | Confirmed      |
     ```

**Consistency Checks**:
1. **Terminology**:
   - Ensure that the same terms are used consistently across all audit reports and logs.
   - Create a glossary of terms if necessary.
   - Example:
     ```markdown
     ## Glossary
     - **Deliverable**: A specific output produced by a role (architect, designer, developer, coder).
     - **Feedback Report**: A document outlining issues and suggestions for improvement.
     ```

2. **Formatting**:
   - Verify that all audit reports and logs follow the same formatting guidelines (e.g., headings, bullet points, tables).
   - Use standardized templates for all documentation.
   - Example:
     ```markdown
     ## Formatting Guidelines
     - Use `#` for main headings.
     - Use `##` for subheadings.
     - Use `-` for bullet points.
     - Use tables for logs and structured data.
     ```

3. **Style**:
   - Ensure a consistent writing style (e.g., tone, tense) across all audit documentation.
   - Follow a style guide to maintain uniformity.
   - Example:
     ```markdown
     ## Style Guide
     - Use active voice.
     - Write in the present tense.
     - Use clear and concise language.
     ```

4. **Review Process**:
   - Implement a review process to check for consistency before finalizing audit reports and logs.
   - Have another team member or lead auditor review the documentation.
   - Example:
     ```markdown
     ## Review Checklist
     - Check for consistent terminology.
     - Verify formatting guidelines are followed.
     - Ensure the writing style is uniform.
     - Have documents reviewed by a peer or lead auditor.
     ```

**Review Checklist for Auditor**  
1. **Clarity**: Ensure the deliverables are clear and understandable.
2. **Completeness**: Check that all necessary components are included.
3. **Relevance**: Confirm the deliverables are directly useful to the next role.
4. **Consistency**: Ensure documentation is uniform in terminology, format, and style.
5. **Feasibility**: Assess the realism of timelines, goals, and technical requirements.

