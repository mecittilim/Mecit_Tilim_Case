
# Mecit Tilim Test Case Project

## Project Overview

This repository contains a small-scale automated UI testing project built with **Python** and **Selenium WebDriver**, designed following the **Page Object Model (POM)** architecture.  
The purpose of this project is to validate essential functionalities of a target web application — including navigation, filtering, and content verification — in a clean, maintainable, and scalable test structure.

The project is intentionally kept simple and focused, aiming to demonstrate proper test design, code organization, and best practices without unnecessary complexity.

---

## Technologies Used

- **Python 3.10+** – Core programming language  
- **Selenium WebDriver** – Browser automation framework  
- **unittest / pytest-like structure** – For organizing and executing test cases  
- **Page Object Model (POM)** – Design pattern for scalable test architecture

---

## Project Structure

```
Mecit_Tilim_Case/
├── fixtures/
│   ├── config.py           # Environment configurations (URLs, settings, etc.)
│   └── driver_setup.py     # WebDriver initialization and teardown
│
├── locators/
│   ├── base_locators.py    # Common locator definitions
│   ├── careers_locator.py  # Locators for Careers page
│   └── QA_locators.py      # Locators for QA page
│
├── pages/
│   ├── base_page.py        # Base page methods (click, wait, assertions, etc.)
│   ├── careers_page.py     # Actions and elements for the Careers page
│   └── QA_page.py          # Actions and elements for the QA page
│
├── tests/
│   └── test_ins_cases.py   # Main test cases verifying key features
│
└── README.md               # Project documentation (this file)
```

---

## Test Design & Approach

The project is designed based on the **Page Object Model (POM)** principles to ensure:

- **Maintainability:** Locators and UI actions are separated from test logic.  
- **Reusability:** Page methods can be reused across different test cases.  
- **Scalability:** New pages and features can be added with minimal changes.  

Each page is represented by a dedicated class within the `pages/` directory. Locators are centralized in the `locators/` directory to prevent duplication and simplify future maintenance.

---

## Test Lifecycle

The test lifecycle is managed using traditional **`setUp`** and **`tearDown`** methods. These handle essential pre- and post-test operations such as:

- Initializing the WebDriver  
- Navigating to the base URL before each test  
- Cleaning up resources and closing the browser after execution  

Since the project is intended to remain simple and lightweight, **`pytest` fixtures were intentionally not used**. This choice ensures the focus remains on the core testing flow and structure rather than framework-specific features.

---

## How to Run Tests

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Mecit_Tilim_Case.git
cd Mecit_Tilim_Case
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the tests

You can run the test suite with:

```bash
python -m unittest discover -s tests
```

Or, if using pytest:

```bash
pytest tests/
```

---

## Key Features

- Clean, maintainable test framework based on **Page Object Model**  
- Modular design: locators, page actions, and test logic are fully separated  
- Traditional **setup/teardown lifecycle** instead of fixtures  
- Easily extendable structure for future test scenarios  
- Lightweight and beginner-friendly design focused on clarity and best practices

  ## Report

  - https://mecittilim.github.io/Mecit_Tilim_Case/report.html

