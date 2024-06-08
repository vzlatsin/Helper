# Running the Application

## Overview
`run.py` serves as the entry point for running the Flask web application. It supports both synchronous and asynchronous modes, determined by command-line input.

## Prerequisites
- Python 3.6+
- Flask
- Dependencies from `requirements.txt`

## Configuration
The script uses the `MY_APP_ENV` environment variable to determine the application's configuration mode (`development`, `production`, etc.). Configurations are loaded from corresponding JSON files within the `config` directory.

## Logging
Logging is configured according to the loaded configuration, specifying log files, levels, and formats.

## Usage
To run the application:
- For synchronous mode: `python run.py`
- For asynchronous mode: `python run.py async`

## Environment Variables
- `MY_APP_ENV`: Determines the app's running environment.
- `APP_SETTINGS`: Set by the script to match `MY_APP_ENV`.

## Command-Line Arguments
- `async`: Specifies that the app should run in asynchronous mode.

## Code Snippets
(Provide relevant code snippets for configuration loading and app initialization)

## Troubleshooting
(Include common issues and resolutions)

