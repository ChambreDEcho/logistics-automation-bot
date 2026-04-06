# Logistics Automation Bot

Python-based automation tool for monitoring logistics load boards in real time using Selenium.

## Overview
This project was developed to reduce repetitive manual monitoring of available freight loads. It automates the process of refreshing the platform, preparing the load view, reading route information, comparing it against configured origin and destination values, and triggering an alert when a match is found.

## Features
- Automated browser interaction with Selenium
- Repeated refresh of available load listings
- Dynamic detection of visible rows
- Origin and destination matching from a configuration file
- Logging of key events and errors
- Visual and sound alert when a matching route is detected

## Technologies
- Python
- Selenium
- Tkinter
- Browser automation
- Configuration-based route matching

## Workflow
1. Open the logistics platform
2. Wait for user login
3. Open the loads section
4. Adjust the visible load filter
5. Refresh results
6. Read available rows safely
7. Extract origin and destination information
8. Compare values against configured routes
9. Trigger an alert when a match is found

## Use Case
This tool is intended to support operational workflows by reducing the need for constant manual refresh and route checking in logistics environments.

## Notes
This repository is shared for educational and portfolio purposes. Sensitive credentials, production-specific data, private business information, and live operational details are intentionally excluded.

## Author and Date
ChambreDEcho  5th April 2026

Initial setup complete