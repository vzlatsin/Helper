# Feature Development Guide

## Introduction
This document provides guidelines for adding or updating features in the "Home App." It aims to ensure that all developers have a clear understanding of the project requirements, architecture, and existing resources.

## Understanding Requirements

### Identifying Needs
- **Feature Requests**: Process for receiving and documenting new feature requests.
  - **Checklist for Handling New Feature Requests**:
    1. **Verify Roadmap Alignment**: Ensure the feature aligns with the main roadmap. Update the roadmap if necessary.
    2. **Check for Sub-Roadmap**: Ensure a sub-roadmap exists; create one if necessary.
    3. **Specification Review**: Check for existing specifications; draft new ones if none exist.
    4. **Cross-Verification with Specifications**: Ensure the feature is reflected in both general and detailed specifications.
    5. **Stakeholder Confirmation**: Obtain approval from stakeholders, document feedback.
    6. **Resource Assessment**: Evaluate existing resources for reuse and identify needs for new resources.
    7. **Update Documentation**: Update all related documentation to reflect the new feature.
    8. **Developer Briefing**: Hold a briefing session to review the checklist and specifications.
    9. **Feedback Loop Setup**: Establish a feedback mechanism for ongoing communication.
- **Requirement Gathering**: Techniques for detailed requirement gathering, including stakeholder interviews and user stories.

### Documentation
- **Spec Writing**: Guidelines for writing clear and detailed specifications.
- **Change Logs**: Maintaining logs of changes for feature updates.

## Project Structure

### Overview


The web application is structured to handle various tasks efficiently through distinct components, each serving a specific function. At the core, there's a user interface (UI) that users interact with. This UI is designed to be intuitive and provides forms and dashboards for users to input data and view information. Behind the scenes, there’s a server or an API that processes all the requests from the UI. It acts as the central command, managing interactions between the user interface, the database, and external services.

The database is a crucial component, storing all the necessary data such as trade details, dividend information, and user settings. It is set up to interact seamlessly with the server, ensuring that data is retrieved, stored, and updated efficiently as users interact with the application.

For fetching financial data, the application integrates with external services like Interactive Brokers through a feature known as Flex Query. This integration helps in pulling detailed financial reports directly into the app. Additionally, the application can connect to Gmail to automatically read and process emails, which is particularly useful for receiving notifications and updates directly through email.


For a clear and organized directory structure of your web application, let’s break down the purpose of each directory under the root directory. This structure ensures that each type of file and component of your application is logically organized, which can help in both development and maintenance:

1. **src/**: This directory contains all the Python scripts that make up the core logic of your application. It’s where you'll find modules for handling database interactions, server-side logic, and any utilities that support the main functions of your app. Organizing all your source code in this directory keeps your application's logic centralized and easily accessible for development and debugging.

2. **templates/**: Here, you’ll store all your HTML files. These templates define the structure and layout of the web pages that users interact with. By separating these HTML files into their own directory, you maintain a clean separation between the application's front-end presentation and its back-end logic, which is good practice in web development.

3. **tests/**: This directory is dedicated to holding test scripts and data. Including a separate tests directory encourages the practice of writing and maintaining unit tests and integration tests. These tests are crucial for verifying that the different parts of your application work as expected and continue to do so as changes are made.

4. **config/**: Configuration files that the application needs to run in different environments (like development, testing, and production) are stored here. These files might include settings for database connections, external API keys, or application-specific options that could change based on the environment the application is running in.

5. **credentials/**: It is essential to store sensitive information such as API keys, database passwords, or OAuth tokens securely. This directory should be properly secured and excluded from version control systems to prevent sensitive data exposure. Managing credentials in a dedicated directory helps in maintaining security best practices.

6. **docs/**: Documentation files are stored in this directory. This can include your application’s architecture documentation, API usage guides, and user manuals. Keeping comprehensive documentation in a dedicated directory ensures that information is easily accessible to developers, users, or new team members who need to understand or work with the application.

By maintaining this directory structure, your web application will be well-organized, making it easier for any developer to understand and navigate the project, thereby enhancing maintainability and scalability.

### Codebase
- **Main Modules**: Description of main modules and their functionality.
app_async.py

### Main Modules

#### 1. **Flask Application Setup**
   - **Description**: This module initializes the Flask application and configures it to handle web requests. It also sets up middleware like CORS to manage cross-origin requests and integrates Flask-SocketIO for real-time browser-server communication.
   - **Functionality**:
     - Initialize the Flask application.
     - Configure middleware for security and compatibility.
     - Set up Flask-SocketIO for handling real-time events.

#### 2. **Database Interaction**
   - **Description**: Manages all interactions with the database, facilitating data retrieval and manipulation. This module uses functions to connect to the database, fetch data, and perform updates or inserts.
   - **Functionality**:
     - Connect to the database using `create_connection`.
     - Fetch and insert dividend data.
     - Query and manage trades and dividends information.

#### 3. **Data Fetching and Processing**
   - **Description**: Responsible for fetching data from external sources like Interactive Brokers and processing it for use in the application. It includes functionality to initiate and download reports via Flex Query.
   - **Functionality**:
     - Use `fetch_dividends_from_ib` and `fetch_trades_from_ib` to gather financial data.
     - Initiate and manage Flex Query reports.
     - Process and organize data received from external sources.

#### 4. **Real-Time Data Synchronization**
   - **Description**: This module compares local data with newly fetched data to identify and synchronize changes. It ensures that the data presented to the user is current and accurate.
   - **Functionality**:
     - Compare newly fetched dividend data with existing data.
     - Update the local database with new entries if discrepancies are found.

#### 5. **Utility Operations**
   - **Description**: Includes additional utility functions that support the main operations of the application, such as file operations and trade data processing.
   - **Functionality**:
     - Write transaction data to files.
     - Generate descriptions for trade entries and organize them for better readability and analysis.

#### 6. **Routing and Event Handling**
   - **Description**: Defines routes and event handlers that manage the flow of data in response to user actions and requests. This module handles both HTTP requests and real-time events triggered through SocketIO.
   - **Functionality**:
     - Define endpoints for fetching financial data and interacting with the user interface.
     - Handle SocketIO events to push real-time updates to the client.


- **Utility Scripts**: Information on utility scripts and how they interact with the main application.

## Reusing Existing Code

### Code Review
- **Existing Functions**: Catalog of existing functions and their purposes.
- **Reusable Components**: List of reusable code components and HTML templates.

### Best Practices
- **Code Modularity**: Best practices for writing modular code that can be easily reused.
- **Template Usage**: Guidelines on how to utilize existing HTML templates for new features.

## Implementation Process

### Development
- **Coding Standards**: Standards and conventions to follow during development.
- **Version Control**: Best practices for using version control systems.

### Testing
- **Unit Tests**: Guidelines for writing and running unit tests.
- **Integration Testing**: Process for conducting integration tests to ensure feature compatibility.

## Deployment

### Staging
- **Staging Environment**: Description of the staging environment setup.
- **Feature Rollout**: Steps for rolling out new features in the staging environment.

### Production
- **Deployment Checklist**: Checklist to ensure all aspects of the feature are ready for production.
- **Monitoring and Feedback**: Methods for monitoring the features post-deployment and gathering user feedback.