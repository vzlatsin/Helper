# Project Updates/Status

This section provides an overview of recent changes, current challenges, immediate goals, and upcoming features for the project.

## Latest Version

- **Version:** 1.0.1 (Unreleased)
- **Last Updated:** 2024-03-26

## Recent Changes

### 2024-03-26

- Added WebSocket functionality for real-time TWS connectivity status updates.
- Began implementing the groundwork for live flex query processing.

## Current Challenges

- Exploring the best ways to optimize WebSocket communication for low-latency updates.
- Investigating intermittent connectivity issues reported by some users when using the real-time update feature.

## Questions and Assistance Needed

- Recommendations on improving WebSocket server stability under high load.
- Best practices for structuring flex query responses to minimize processing delay on the client side.

## Immediate Goals

- Finalize and test the WebSocket implementation for real-time updates.
- Start development on the tax reporting module with an aim to support pre-processing of flex queries.

### Planned Features

#### Real-Time Flex Query Processing Updates

- **Goal:** Implement WebSocket-based real-time updates for the flex query process.
- **Rationale:** To address user feedback regarding the lack of visibility into the process's progress, which can appear unresponsive during data retrieval and processing.
- **Implementation Steps:**
  1. **Server-Side Logic Enhancement:** Modify the backend to initiate a WebSocket connection when a flex query operation starts. Emit progress updates at key stages (e.g., connecting to IB, running the query, processing data, updating the database).
  2. **Client-Side Handling:** Update the frontend to listen for WebSocket messages and display these updates to the user in a meaningful way, enhancing the perception of responsiveness and engagement.

- **Expected Outcome:** Users will receive continuous feedback during the flex query operation, significantly improving the user interface's interactivity and responsiveness.

## Upcoming Features

- **Tax Reporting Module:** An extension aimed at automating tax return preparation, scheduled for the next minor release.
- **Investment Analysis Tools:** In planning, tools for analyzing portfolio performance and tax implications.

## Notes for Collaborators

- Please prioritize work on the WebSocket stability and client-side processing efficiency.
- Feedback on the current UI/UX of the real-time updates feature is highly appreciated.
