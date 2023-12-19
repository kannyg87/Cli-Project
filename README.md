# Phase 3 CLI+ORM Project Template

## Learning Goals

- Understand the basic directory structure of a CLI+ORM application.
- Learn the initial steps in building a CLI application integrated with an ORM.

---

## Introduction

Welcome to the CLI+ORM project template! This is designed to help you create a Command Line Interface (CLI) application that interacts with a database using Object-Relational Mapping (ORM). Let's explore the project structure and get started.

### Project Structure

Your project is structured as follows:



```console

├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │       └── children.py
    |       └── parent.py
    |
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
```


---

## Setting Up Your Environment

The project comes with a Pipfile for managing dependencies:

1. To install dependencies, run:

    ```
    pipenv install
    ```

2. Activate the virtual environment with:

    ```
    pipenv shell
    ```

---

## Building Your CLI

Your CLI application will interact with users via the command line, executing operations based on their input.

### Getting Started with the CLI

The `lib/cli.py` file contains a basic structure for your CLI application:

```python
# lib/cli.py

# Import necessary functions
from helpers import exit_program, helper_1

def main():
    while True:
        menu()
        choice = input("> ")
        # Implement your CLI logic here

def menu():
    # Define your menu options here

if __name__ == "__main__":
    main()


Helper Functions
The lib/helpers.py file is where you can define functions that support your CLI operations:
# lib/helpers.py

def helper_1():
    # Implement a helper function

def exit_program():
    # Function to exit the program


Executing the CLI
Run your CLI application with:

python lib/cli.py


ORM Integration
In the lib/models directory, you'll find the ORM models children.py and parent.py. These models represent your database structure and are crucial for the ORM functionality of your application.

Model Examples
children.py: Manages child records in your database.
parent.py: Manages parent records in your database.


Database Management
Use lib/debug.py and lib/seed.py for database debugging and seeding respectively.

Customizing the README.md
Replace the contents of this README.md with details specific to your project. Describe key functionalities, how to run the application, and any important notes about your models and database structure.

Conclusion
This template is a starting point for your Phase 3 CLI+ORM project. Customize it according to your project requirements and have fun building a functional CLI application!

