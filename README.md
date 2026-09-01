# Bugzot Enterprise System

A Python-based enterprise training organisation management system developed for **Bugzot Training Organisation**. The application demonstrates object-oriented programming, software design patterns, concurrent processing, system monitoring, automated testing, application profiling, and a graphical user interface.

## 📌 Project Overview

The **Bugzot Enterprise System** is designed to support the management of a professional training and certification organisation.

The system provides functionality for:

* Learner registration and validation
* Course management
* Registration processing
* Support ticket management
* Assessment management
* Registration and performance reporting
* System logging and monitoring
* Concurrent registration processing
* Automated unit testing
* Application performance profiling
* Graphical user interface using Tkinter

The application uses an object-oriented design to represent learners, courses, registrations, assessments, and support tickets.

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – Graphical User Interface
* **Object-Oriented Programming (OOP)**
* **Abstract Base Classes**
* **Design Patterns**
* **Threading**
* **Logging**
* **Unit Testing**
* **cProfile**
* **pstats**

The project primarily uses Python's standard library modules, including `tkinter`, `unittest`, `logging`, `threading`, `cProfile`, and `pstats`.

---

## 🏗️ System Architecture & OOP

The system uses several domain classes to represent the organisation's core entities.

### Core Domain Classes

* `Learner`
* `Course`
* `Registration`
* `Assessment`
* `SupportTicket`

## The `Registration` and `Assessment` classes receive existing domain objects, demonstrating object relationships and aggregation.

## 🎨 Design Patterns

The project implements multiple software design patterns.

### Singleton Pattern

The `SingletonConfiguration` class provides a single configuration object for system settings such as:

* User settings
* Login configuration
* Course configuration
* Registration configuration

This ensures that only one configuration instance is created.

### Factory Pattern

The `SupportTicketFactory` creates different types of support tickets based on the requested ticket type.

Supported ticket types include:

* Course
* Assessment
* Registration

### Strategy Pattern

The assessment result calculation uses different strategies:

* `Average`
* `Percentage`
* `Classification`

The `Result` class allows the selected strategy to perform the calculation.

---

## ⚙️ Registration Processing Engine

The system includes a registration processing engine responsible for processing learner registrations.

The engine provides:

* Learner validation
* Course validation
* Duplicate registration detection
* Course capacity validation
* Successful registration storage
* Failed registration tracking
* Registration summaries
* Performance monitoring
* Concurrent request processing

## A `Lock` is used to protect shared registration resources during processing.

## 🧵 Concurrent Processing

The system demonstrates concurrent registration processing using Python threads.

Multiple registration requests can be processed through separate threads while the registration engine protects shared resources using a thread lock.

## This demonstrates the use of concurrency for handling multiple registration operations.

## 📊 Bugzot Monitoring & Logging

The application contains a monitoring subsystem called **Bugzot Monitoring**.

The logging system records:

* Normal system events
* Warnings
* Errors
* Registration processing events
* Registration success/failure information
* Performance information

Logs are written to:

```text
bugzot_log.txt
```

The system can also generate a performance report containing:

* Total successful registrations
* Total failed registrations
* Registration success rate

---

## 🖥️ Graphical User Interface

The application provides a desktop GUI built with **Tkinter**.

### Main Sections

#### Learner Registration

Allows users to enter:

* Name
* Surname
* Learner ID
* Email
* Phone number
* Course

Registered learners are displayed in a table.

#### Course Management

Allows users to create courses with:

* Course name
* Course ID
* Duration
* Course fee
* Instructor
* Capacity

#### Support Tickets

Users can create support tickets containing:

* Learner ID
* Description
* Date
* Status
* Ticket type

Supported ticket types include Course, Assessment, and Registration support.

#### Reports

The reporting interface provides:

* Registration Summary
* Performance Report
* System Log

---

## 🧪 Automated Testing

The project includes an automated test suite using Python's `unittest` framework.

Tests cover areas including:

* Learner validation
* Invalid email validation
* Invalid phone validation
* Course validation
* Invalid course fees
* Successful registration
* Duplicate registration
* Course capacity
* Average calculation
* Percentage calculation
* Classification
* Support ticket creation
* Invalid support ticket data

---

## 📈 Application Profiling

The project uses Python's `cProfile` and `pstats` modules to analyse application performance.

The profiling functionality:

1. Starts the profiler
2. Creates registration requests
3. Processes the requests
4. Collects profiling statistics
5. Sorts results by cumulative execution time
6. Displays function call statistics
7. Saves profiling results to a file

The generated profiling output is saved as:

```text
profiling_results.txt
```

---

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your computer.

Check your Python installation:

```bash
python --version
```

or:

```bash
py --version
```

### Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/bugzot_enterprise__system.git
```

Navigate into the project:

```bash
cd bugzot_enterprise__system
```

### Run the Application

```bash
python bugzot_enterprise_system.py
```

The Bugzot Enterprise System GUI will launch.

---

## 🧪 Running the Tests

The project contains a `unittest` test suite.

Tests can be executed through the application's test execution section.

The system reports:

* Number of tests executed
* Failures
* Errors
* Overall test success

---


## 📸 Screenshots

### Learner Registration


<img width="1836" height="946" alt="registration" src="https://github.com/user-attachments/assets/85e0a864-03bd-40cb-93de-3768767de0a9" />




### Course Management

<img width="1920" height="908" alt="course management" src="https://github.com/user-attachments/assets/a0b34349-604b-44ff-b4b2-aaad66dcab29" />


### Support Tickets

<img width="1920" height="896" alt="support ticket" src="https://github.com/user-attachments/assets/650cc723-521b-48c6-846f-9f7c76f3230b" />


### Reports

<img width="1920" height="887" alt="Report output" src="https://github.com/user-attachments/assets/2e910dfa-2e89-475f-b1e4-308795a8fc0e" />


## 🎯 Project Objectives

The project demonstrates practical implementation of:

* Object-oriented software development
* Domain modelling
* Object relationships and aggregation
* Software design patterns
* Enterprise-style registration processing
* Concurrent operations
* Error handling and validation
* Application monitoring
* Logging
* GUI development
* Automated testing
* Performance profiling

---

## 🔑 Key Learning Outcomes

Through this project, the following software engineering concepts were applied:

* Classes and objects
* Encapsulation
* Inheritance
* Abstraction
* Abstract base classes
* Object composition/aggregation
* Factory design pattern
* Singleton design pattern
* Strategy design pattern
* Threading and synchronization
* Exception handling
* Logging
* Unit testing
* Performance profiling
* GUI development

---

## 📄 Academic Project

This project was developed as part of an academic software engineering/enterprise programming assignment and demonstrates the application of software engineering principles to a practical enterprise management scenario.

---

## 👨‍💻 Author

**Gift Seilane**

Software Engineering Student

---

## ⭐ Project Status

**Completed / Academic Project**

The project demonstrates a functional enterprise training organisation management system with GUI functionality, registration processing, monitoring, testing, and performance profiling.
