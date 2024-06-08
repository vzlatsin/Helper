### Auditor Guide

**Purpose**  
The audit ensures the quality, completeness, and compliance of deliverables produced by the architect, designer, developer, and coder roles.

**Responsibilities**  
1. **Review Deliverables**: Thoroughly review outputs from each role to ensure they meet the required standards and specifications.
2. **Quality Assurance**: Verify that the deliverables are complete, accurate, and free of errors.
3. **Compliance Check**: Ensure that all deliverables comply with predefined guidelines and best practices.
4. **Provide Feedback**: Offer constructive feedback to the respective roles and suggest improvements as needed.
5. **Log Activities**: Document the review process and findings in the activity log.

**Process**  
1. **Identify the Role**:
   - Confirm which role's deliverables are being audited: architect, designer, developer, or coder.
2. **Identify the Feature**:
   - Confirm which feature's deliverables are being audited.
3. **Check GitHub Access**:
   - Ensure GitHub can be reached and navigate to the relevant subdirectory for the deliverables.
4. **Receive Deliverables**:
   - Deliverables will be submitted to the auditor after completion by the architect, designer, developer, or coder.
5. **Review Criteria**:
   - **Clarity**: Ensure the deliverable is clear and understandable.
   - **Completeness**: Check that all necessary components are included.
   - **Accuracy**: Verify the correctness of the content.
   - **Compliance**: Ensure adherence to guidelines and standards.
6. **Provide Feedback**:
   - Document any issues or areas for improvement.
   - Return deliverables to the respective role for revisions if necessary.
7. **Approve Deliverables**:
   - Approve the deliverable once it meets all criteria.
   - Document the approval in the activity log.
8. **Log Activities**:
   - Update the `activity_log.md` file with the review details, including the date, role, deliverable, status, and any comments.

**Review Checklist**

**Architect Deliverables**
- **Criteria**
  - **Completeness**: Ensure all high-level requirements, roadmap details, and benefit analysis are included.
  - **Clarity**: Verify the information is clear and understandable.
  - **Accuracy**: Check for correctness.
  - **Compliance**: Ensure guidelines are followed.
- **Location and Review**:
  1. **Verify Requirements**:
     - Located in `docs/roadmaps/requirements/`
     - Check for completeness and clarity.
     - Identify any missing or ambiguous requirements.
  2. **Examine the Roadmap**:
     - Located in `docs/roadmaps/`
     - Verify inclusion of all major phases and milestones.
     - Assess the realism of the timeline and phases.
  3. **Evaluate the Benefit Analysis**:
     - Ensure a benefit analysis document is created in `docs/roadmaps/benefit_analysis/`
     - Ensure it clearly explains the benefits.
     - Verify the benefits align with project goals.
  4. **Check Interaction Efficiency**:
     - Confirm work is completed within five interactions or fewer.

**Designer Deliverables**:
- **Sub-roadmaps**
  - Located in `docs/roadmaps/`
- **Specifications**
  - Located in `docs/roadmaps/specifications/`
- **Design validations**
  - Located in `docs/guides/`

**Developer Deliverables**:
- **Pseudocode**
  - Located in `docs/pseudocode/`
- **Script instructions**
  - Located in `docs/roadmaps/specifications/`

**Coder Deliverables**:
- **Implemented code**
  - Located in `src/`
- **Test results**
  - Located in `tests/`
- **Documentation**
  - Located in `docs/`

All project-related documents and deliverables are hosted on GitHub. The repository URL is: [https://github.com/vzlatsin/Helper](https://github.com/vzlatsin/Helper)

**Directory Paths:**
- **Sub-roadmaps**: `https://github.com/vzlatsin/Helper/tree/master/docs/roadmaps/specifications`
- **Specifications**: `https://github.com/vzlatsin/Helper/tree/master/docs/roadmaps/specifications`

**Example Entry for Activity Log**

```markdown
## [Date]
- **Auditor**: Reviewed [Role]'s deliverables for [Feature/Task].
  - **Details**: Conducted a thorough review of the [specific deliverable]. Checked for clarity, completeness, accuracy, and compliance.
  - **Files Checked**: [List of files checked]
  - **Status**: [Completed/In Progress]
  - **Comments**: [Feedback and any additional comments]
```

