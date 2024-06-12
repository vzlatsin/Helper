### Designer Guide

**Purpose**  
To ensure the creation of detailed and clear designs that guide the subsequent roles (developer, coder) effectively.

**Responsibilities**  
1. **Interpret Architect Deliverables**: Understand requirements, user stories, and feature descriptions.
2. **Create Design Deliverables**: Produce sub-roadmaps, specifications, and design validations.
3. **Ensure Clarity and Completeness**: Make sure all deliverables are comprehensive and easily understandable by the developer.

**Inputs**:
1. **Requirements Document**: Detailed requirements from the architect.
   - **Location**: `docs/[feature_name]/architect/requirements.md`
2. **User Stories**: Practical examples and use cases with acceptance criteria.
   - **Location**: `docs/[feature_name]/architect/user_stories.md`
3. **Feature Description**: Comprehensive overview of the feature.
   - **Location**: `docs/[feature_name]/architect/feature_description.md`
4. **Data Requirements**: Clearly defined data dependencies and requirements.
   - **Location**: `docs/[feature_name]/architect/data_requirements.md`
5. **Roadmap**: High-level overview of project phases and milestones.
   - **Location**: `docs/roadmap.md`

**Outputs**:
1. **Sub-roadmaps**:
   - Detailed plans breaking down the project phases.
   - **Location**: `docs/[feature_name]/designer/sub_roadmaps.md`
2. **Specifications**:
   - Detailed design specifications including all necessary design details.
   - **Location**: `docs/[feature_name]/designer/specifications.md`
3. **Design Validations**:
   - Validations ensuring the design meets requirements and is feasible.
   - **Location**: `docs/[feature_name]/designer/design_validations.md`

**Process**  
1. **Gather Inputs**:
   - **Sources**: Requirements document, user stories, feature descriptions, data requirements from the architect.

2. **Create Outputs**:
   - **Sub-roadmaps**:
     - Detailed plans breaking down the project phases.
     - Format: Use a standardized template.
   - **Specifications**:
     - Detailed design specifications including all necessary design details.
     - Format: Use clear and consistent language and diagrams.
   - **Design Validations**:
     - Validations ensuring the design meets requirements and is feasible.
     - Format: Validation documents with checklists and testing criteria.

**Documentation Standards**:
1. **Sub-roadmaps**:
   - **Format**: Use a standardized template with sections for phases, tasks, and milestones.
   - **Template**:
     ```markdown
     ## Sub-roadmap for [Feature Name]
     ### Phases
     - Phase 1: Description and tasks
     - Phase 2: Description and tasks
     ### Tasks
     - Task 1: Description
     - Task 2: Description
     ### Milestones
     - Milestone 1: Description and due date
     - Milestone 2: Description and due date
     ```

2. **Specifications**:
   - **Format**: Use a standardized template with sections for overview, design details, and diagrams.
   - **Template**:
     ```markdown
     ## Specifications for [Feature Name]
     ### Overview
     - Brief overview of the design.
     ### Design Details
     - Detail 1: Description
     - Detail 2: Description
     ### Diagrams
     - Diagram 1: Description
     - Diagram 2: Description
     ```

3. **Design Validations**:
   - **Format**: Use a standardized template with sections for validation criteria, test cases, and results.
   - **Template**:
     ```markdown
     ## Design Validations for [Feature Name]
     ### Validation Criteria
     - Criterion 1: Description
     - Criterion 2: Description
     ### Test Cases
     - Test Case 1: Description and expected result
     - Test Case 2: Description and expected result
     ### Results
     - Result 1: Description
     - Result 2: Description
     ```

**Consistency Checks**:
1. **Terminology**:
   - Ensure that the same terms are used consistently across all documents.
   - Create a glossary of terms if necessary.
   - Example:
     ```markdown
     ## Glossary
     - **Phase**: A stage in the project lifecycle.
     - **Milestone**: A significant point or event in the project timeline.
     ```

2. **Formatting**:
   - Verify that all documents follow the same formatting guidelines (e.g., headings, bullet points, numbering).
   - Use standardized templates for all documents.
   - Example:
     ```markdown
     ## Formatting Guidelines
     - Use `#` for main headings.
     - Use `##` for subheadings.
     - Use `-` for bullet points.
     - Use `1.` for numbered lists.
     ```

3. **Style**:
   - Ensure a consistent writing style (e.g., tone, tense) across all documents.
   - Follow a style guide to maintain uniformity.
   - Example:
     ```markdown
     ## Style Guide
     - Use active voice.
     - Write in the present tense.
     - Use clear and concise language.
     ```

4. **Review Process**:
   - Implement a review process to check for consistency before deliverables are passed to the developer.
   - Have another team member or auditor review the documents.
   - Example:
     ```markdown
     ## Review Checklist
     - Check for consistent terminology.
     - Verify formatting guidelines are followed.
     - Ensure the writing style is uniform.
     - Have documents reviewed by a peer or auditor.
     ```

**Review Checklist for Auditor**  
1. **Clarity**: Ensure the deliverables are clear and understandable for the developer.
2. **Completeness**: Check that all necessary components are included.
3. **Relevance**: Confirm the deliverables are directly useful to the developer.
4. **Consistency**: Ensure documentation is uniform in terminology, format, and style.
5. **Feasibility**: Assess the realism and technical feasibility of the design.

**Feedback and Iteration**  
- Ensure deliverables include room for feedback and iteration.
- Define procedures for handling incomplete or unclear inputs.
