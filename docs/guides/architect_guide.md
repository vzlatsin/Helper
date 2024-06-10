### Architect Guide

**Purpose**  
To ensure the creation of detailed and clear deliverables that guide the subsequent roles (designer, developer, coder) effectively.

**Responsibilities**  
1. **Gather Requirements**: Collect project goals and stakeholder requirements.
2. **Create Deliverables**: Produce detailed requirements, user stories, feature descriptions, data requirements, and roadmaps.
3. **Ensure Clarity and Completeness**: Make sure all deliverables are comprehensive and easily understandable.

**Inputs**:
1. **Project Goals**: High-level objectives and desired outcomes.
2. **Stakeholder Requirements**: Detailed needs and expectations from stakeholders.
3. **Existing Documentation**: Relevant documents from previous projects or phases.
4. **Data Sources**: Information on available data and databases.

**Outputs**:
1. **Requirements Document**:
   - Detailed and clear requirements.
   - **Location**: `docs/[feature_name]/architect/requirements.md`
2. **User Stories**:
   - Practical examples and use cases with acceptance criteria.
   - **Location**: `docs/[feature_name]/architect/user_stories.md`
3. **Feature Description**:
   - Comprehensive overview of the feature, including functionality and goals.
   - **Location**: `docs/[feature_name]/architect/feature_description.md`
4. **Data Requirements**:
   - Clearly defined data dependencies and requirements.
   - **Location**: `docs/[feature_name]/architect/data_requirements.md`
5. **Roadmap**:
   - High-level overview of project phases and milestones.
   - **Location**: `docs/roadmap.md`

**Process**  
1. **Gather Inputs**:
   - **Sources**: Project goals, stakeholder requirements, existing documentation, and data.

2. **Create Outputs**:
   - **Requirements Document**:
     - Detailed and clear.
     - Format: Use a standardized template.
   - **User Stories**:
     - Include practical examples and use cases.
     - Format: User story template with clear acceptance criteria.
   - **Feature Description**:
     - Comprehensive overview covering all design aspects.
   - **Data Requirements**:
     - Clearly defined data dependencies.
   - **Roadmap**:
     - High-level overview of project phases and milestones.
     - Located in `docs/roadmap.md`.

**Documentation Standards**:
1. **Requirements Document**:
   - **Format**: Use a standardized template with sections for objectives, scope, detailed requirements, and constraints.
   - **Template**:
     ```markdown
     ## Requirements Document for [Feature Name]
     ### Objectives
     - Objective 1
     - Objective 2
     ### Scope
     - In-scope: Item 1, Item 2
     - Out-of-scope: Item 1, Item 2
     ### Detailed Requirements
     - Requirement 1: Description
     - Requirement 2: Description
     ### Constraints
     - Constraint 1
     - Constraint 2
     ```

2. **User Stories**:
   - **Format**: Use a standardized template with fields for title, description, acceptance criteria, and priority.
   - **Template**:
     ```markdown
     ## User Story for [Feature Name]
     ### Title
     - User Story Title
     ### Description
     - As a [user], I want to [action], so that [benefit].
     ### Acceptance Criteria
     - Criteria 1
     - Criteria 2
     ### Priority
     - High/Medium/Low
     ```

3. **Feature Description**:
   - **Format**: Use a clear hierarchical structure with section headings.
   - **Template**:
     ```markdown
     ## Feature Description for [Feature Name]
     ### Overview
     - Brief overview of the feature.
     ### Functionality
     - Detailed functionality description.
     ### Goals
     - Goals and objectives of the feature.
     ```

4. **Data Requirements**:
   - **Format**: Use tables and bullet points to list data dependencies and requirements.
   - **Template**:
     ```markdown
     ## Data Requirements for [Feature Name]
     ### Data Dependencies
     - Dependency 1
     - Dependency 2
     ### Data Requirements
     - Requirement 1: Description
     - Requirement 2: Description
     ```

5. **Roadmap**:
   - **Format**: Use a Gantt chart or timeline with clear milestones.
   - **Template**:
     ```markdown
     ## Roadmap for [Project Name]
     ### Phases
     - Phase 1: Description and milestones
     - Phase 2: Description and milestones
     ### Milestones
     - Milestone 1: Description and due date
     - Milestone 2: Description and due date
     ```

**Consistency Checks**:
1. **Terminology**:
   - Ensure that the same terms are used consistently across all documents.
   - Create a glossary of terms if necessary.
   - Example:
     ```markdown
     ## Glossary
     - **Feature**: A specific functionality to be developed.
     - **User Story**: A description of a software feature from an end-user perspective.
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
   - Implement a review process to check for consistency before deliverables are passed to the designer.
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
1. **Clarity**: Ensure the deliverables are clear and understandable.
2. **Completeness**: Check that all necessary components are included.
3. **Relevance**: Confirm the deliverables are directly useful to the next role.
4. **Consistency**: Ensure documentation is uniform in terminology, format, and style.
5. **Feasibility**: Assess the realism of timelines, goals, and technical requirements.

**Feedback and Iteration**  
- Ensure deliverables include room for feedback and iteration.
- Define procedures for handling incomplete or unclear inputs.
