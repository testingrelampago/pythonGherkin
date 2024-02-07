# PythonGherkin

This repository contains automated test cases for the [Testing Relampago](https://www.testingrelampago.com) website using Selenium, Gherkin, Behave in Python.

## Overview

The project aims to demonstrate automated testing practices for a web application using the Selenium WebDriver and Gherkin language for behavior-driven development (BDD) using Behave for Python.

## Features

- **Login Functionality**: Test cases for successful login and various login scenarios.
- **Search Services**: Test cases for searching services on the website.

## Getting Started

### Prerequisites

- Python 3.x
- Chrome or Firefox browser (depending on the WebDriver you choose. I'm using Chrome)

### Some commands

1. Clone the repository:

   ```bash
   git clone https://github.com/testingrelampago/pythonGherkin.git

2. Commands to install:

   ```bash
   pip install behave selenium webdriver_manager

3. Install python-dotenv to manage these files .env

   ```bash
   pip install python-dotenv

4. Execute test cases BDD

   ```bash
   behave --color
   behave --include login.feature