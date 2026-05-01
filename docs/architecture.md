# Architecture

## Project Structure

text
main.py
platform_bot/
config.py
logger.py
alerts.py
browser.py
parser.py
monitor.py

Components

*main.py*

Application entry point.

*config.py*

Stores paths, selectors, platform URL, and configuration loading logic.

*logger.py*

Handles event logging.

*alerts.py*

Manages sound and visual alerts.

*browser.py*

Contains browser interaction helpers.

*parser.py*

Extracts route data from visible rows.

*monitor.py*

Coordinates the full monitoring process.

Design Goal

The project was refactored from a single automation script into a modular structure to improve maintainability, readability, and scalability