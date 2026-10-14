# Smart Railway Coach Allocation and Management System (Week 1 - Week 4)

**A Database-Driven Railway Coach Management Project Using Python, Flask, and MySQL**

## Table of Contents

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Project Objectives](#project-objectives)
4. [Proposed Solution](#proposed-solution)
5. [Project Scope](#project-scope)
6. [Technology Stack](#technology-stack)
7. [System Workflow](#system-workflow)
8. [Database Design](#database-design)
9. [Weekly Development Plan](#weekly-development-plan)
10. [Project Structure](#project-structure)
11. [Installation and Setup](#installation-and-setup)
12. [Application Usage](#application-usage)
13. [Rule-Based Coach Filtering](#rule-based-coach-filtering)
14. [Testing and Validation](#testing-and-validation)
15. [Current Limitations](#current-limitations)
16. [Future Enhancements](#future-enhancements)
17. [Resources and References](#resources-and-references)
18. [Author](#author)

---

## 1. Project Overview

The Smart Railway Coach Allocation and Management System is a software project designed to organize railway train and coach information using a structured database and a Python-based web application.

The system focuses on maintaining train records, coach details, coach types, current station information, maintenance status, and train-wise coach requirements. It also introduces rule-based filtering to identify coaches that may be suitable for a train based on predefined selection criteria.

The project is being developed in four stages, covering initial database design, database models and CRUD operations, train and coach management, and rule-based coach filtering.

The current project scope is limited to **Week 1 through Week 4**.

### Project Information

| Attribute | Details |
|---|---|
| Project Title | Smart Railway Coach Allocation and Management System |
| Project Category | Software Development / Database Management |
| Programming Language | Python |
| Web Framework | Flask |
| Database | MySQL |
| ORM | SQLAlchemy |
| Development Environment | Visual Studio Code |
| Database Tool | MySQL Workbench |
| Project Scope | Week 1–Week 4 |
| Author | Suvan Mahajan |

## 2. Problem Statement

Railway coach management involves maintaining information about coaches, their types, locations, availability, maintenance status, and allocation to trains.

When this information is maintained in disconnected records or managed manually, identifying suitable coaches for a train can become difficult. Coaches under maintenance should not be selected, and coaches already assigned to another train should not be considered available for a new allocation.

A structured system is therefore needed to store railway-related records, maintain relationships between database entities, update coach information, and filter coaches according to defined rules.

This project addresses these requirements through a database-driven application and rule-based selection logic.

## 3. Project Objectives

The primary objectives of the project are:

- To design a relational database for railway trains, coaches, requirements, and allocations.
- To establish primary-key and foreign-key relationships between database tables.
- To implement Python models for the required entities.
- To perform CRUD operations: Create, Read, Update, and Delete.
- To manage train information and coach records.
- To maintain coach type, current station, and maintenance status.
- To implement rule-based filtering for identifying potentially suitable coaches.
- To exclude coaches that are under maintenance or already allocated, according to the recorded data and implemented rules.
- To document development activities, implementation details, and test results separately for each week.

## 4. Proposed Solution

The proposed system uses Python and Flask for application logic, MySQL for persistent data storage, and SQLAlchemy for object-relational mapping.

The database stores train information, coach details, requirements, and allocation records in separate tables. Python models represent these database entities, while application routes provide access to the required operations.

The coach filtering component applies predefined conditions to identify coaches that match the requested coach type and satisfy the configured availability, location, maintenance, and allocation checks.

The project is intended as a foundational management system. It does not claim to be connected to the live Indian Railways reservation, train operations, or coach inventory systems.

## 5. Project Scope

The project is divided into four development stages.

### In Scope

- Development environment setup.
- Relational database schema design.
- MySQL table creation.
- Python database models.
- CRUD operations for required entities.
- Train and coach record management.
- Coach status management.
- API endpoints for relevant records.
- Rule-based coach filtering.
- Basic test cases and project documentation.

### Out of Scope for Weeks 1–4

- Integration with live railway operational databases.
- Real-time railway coach tracking.
- Automatic physical coach movement or dispatch.
- Production deployment and enterprise-scale operations.
- Advanced optimization algorithms beyond the defined rule-based filtering.

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Implements the application logic and filtering rules. |
| Flask | Provides the web application and HTTP routes. |
| MySQL | Stores train, coach, requirement, and allocation records. |
| SQLAlchemy | Maps Python classes to database tables and supports database operations. |
| MySQL Connector/Python | Connects Python application code to MySQL. |
| HTML | Structures web pages and forms. |
| CSS | Styles the user interface where used. |
| Visual Studio Code | Used for writing and managing project code. |
| MySQL Workbench | Used for database creation, queries, and schema inspection. |
| Git and GitHub | Used for source-code version control and project documentation. |

## 7. System Workflow

The intended workflow is:

1. Initialize the development environment.
2. Create the database and required tables.
3. Store train, coach, requirement, and allocation information.
4. Retrieve and update train and coach records.
5. Receive the coach requirements for a selected train.
6. Apply the configured coach-selection rules.
7. Exclude coaches that do not satisfy the required conditions.
8. Review the filtered results and validate them using test cases.

### High-Level Architecture

```text
User
 |
 v
Flask Application
 |
 v
Application Routes and Business Logic
 |
 v
Python Models / Database Operations
 |
 v
MySQL Database
 |
 v
Stored Train, Coach, Requirement
and Allocation Records
```

The exact application flow depends on the routes and database operations implemented in the project code.

## 8. Database Design

The database is organized around four primary entities.

### 8.1 Trains Table

The `trains` table stores basic train information.

| Field | Purpose |
|---|---|
| id | Primary key identifying a train record |
| train_number | Train identification number |
| train_name | Name of the train |
| source_station | Origin station |
| destination_station | Destination station |

### 8.2 Coaches Table

The `coaches` table stores coach details and current status.

| Field | Purpose |

| id | Primary key identifying a coach record |
| coach_number | Coach identification number |
| coach_type | Category of coach, such as AC or Sleeper |
| current_station | Station where the coach is recorded as available |
| status | Current status, including Available or Under Maintenance |

### 8.3 Requirements Table

The `requirements` table records the coach requirements associated with trains.

| Field | Purpose |

| id | Primary key identifying a requirement |
| train_id | Foreign key referring to a train |
| coach_type | Required category of coach |
| quantity | Number of coaches requested |

### 8.4 Allocations Table

The `allocations` table records the relationship between trains and coaches.

| Field | Purpose |
|---|---|
| id | Primary key identifying an allocation |
| train_id | Foreign key referring to a train |
| coach_id | Foreign key referring to a coach |
| allocation_status | Status of the allocation, such as Active or Released |
| allocated_at | Time at which the allocation was recorded |

### 8.5 Database Relationships

- A train can have multiple requirement records.
- A train can have multiple allocation records.
- A coach can be referenced by allocation records.
- Foreign keys connect requirement and allocation records to their corresponding train and coach records.

These relationships help maintain data consistency and support queries across related tables.

## 9. Weekly Development Plan

The project documentation is maintained in separate Markdown files.

| Week | Main Focus | Report |

| Week 1 | Environment setup and database schema design | [week 1 report](reports/week-1-report.md) |
| Week 2 | Database implementation, Python models, and CRUD operations | [week 2 project report](reports/week-2-project-report.md) |
| Week 3 | Train and coach management, status updates, and API endpoints | [week 3 project report](reports/week-3-project-report.md) |
| Week 4 | Rule-based coach filtering and validation | [week 4 project report](reports/week-4-project-report.md) |

Each report should document the objective, activities performed, implementation details, evidence, test results, and outcome of the corresponding week.

## 10. Project Structure

The intended repository structure is:

```text
smart-railway-coach-allocation-system/
|
|-- app.py
|-- database.py
|-- models.py
|-- schema.sql
|-- requirements.txt
|-- .env.example
|-- README.md
|
|-- templates/
|-- static/
|
|-- reports/
|   |-- week-1-report.md
|   |-- week-2-report.md
|   |-- week-3-report.md
|   |-- week-4-report.md
|
|-- .gitignore
```

The actual repository may contain additional required files. Keep the structure consistent with the files present in the project.

## 11. Installation and Setup

### Prerequisites

Install the following software:

- Python 3.10 or a compatible version supported by the project's dependencies.
- MySQL Server.
- MySQL Workbench.
- Visual Studio Code.
- Git, if using Git commands to upload or clone the repository.

### Step 1: Clone the Repository

Replace the placeholder URL with the HTTPS URL of the GitHub repository.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd smart-railway-coach-allocation-system
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure the Database

1. Start MySQL Server.
2. Open MySQL Workbench and connect to the local database server.
3. Open `schema.sql`.
4. Review the SQL commands and execute them to create the required database and tables.
5. Configure the application's local database credentials.

### Step 5: Configure Environment Variables

Create a local `.env` file using `.env.example` as a reference.

Set the required database host, username, password, database name, and connection URL according to the local MySQL configuration.

Do not upload `.env` or any file containing real passwords or secret keys to GitHub.

### Step 6: Create an Application Account

If the application requires login, follow the account-creation procedure included in the project, after ensuring that the required user table exists.

### Step 7: Run the Application

```bash
python app.py
```

If the application starts successfully, open the following address in a browser:

`http://127.0.0.1:5000`

The exact setup steps may vary according to the current project files and local configuration.

## 12. Application Usage

After completing setup:

1. Start the Flask application.
2. Sign in if authentication is enabled.
3. Add train records with their identification and route details.
4. Add coach records with their coach type, station, and status.
5. Update train and coach information when required.
6. Record coach requirements for the relevant train.
7. Apply the available coach filtering functionality.
8. Check the displayed records and compare the results with the expected selection rules.

The available screens and operations depend on the routes and templates included in the current application.

## 13. Rule-Based Coach Filtering

The Week 4 filtering component uses predefined rules to identify coaches that may satisfy a train's requirements.

### Selection Criteria

- **Coach type:** The coach must match the requested type.
- **Station:** The recorded current station should match the required station when station matching is enabled.
- **Maintenance status:** Coaches under maintenance must be excluded.
- **Allocation status:** Coaches with an active allocation must be excluded from new allocations where this rule is implemented.
- **Availability:** The coach must satisfy the application's availability conditions.

### Filtering Procedure

1. Read the selected train's requirements.
2. Identify the requested coach type and quantity.
3. Retrieve coaches matching the required type.
4. Apply station and availability conditions.
5. Exclude coaches under maintenance.
6. Exclude coaches already allocated, using recorded allocation data.
7. Return the coaches that satisfy all implemented conditions.

This is a rule-based selection process, not an advanced optimization algorithm. The filtering output should be tested against sample records before it is considered validated.

## 14. Testing and Validation

Testing should verify that database operations and coach-selection rules behave as expected.

| Test Case | Expected Behaviour |

| Add a valid train | Train record is stored |
| Retrieve train records | Existing train records are displayed or returned |
| Update train details | Changes are reflected in the database |
| Add a valid coach | Coach record is stored |
| Update coach status | Updated status is saved |
| Filter by coach type | Coaches of other types are excluded |
| Coach under maintenance | Coach is excluded from eligible results |
| Coach already allocated | Coach is excluded where active-allocation checking is implemented |
| Coach at the wrong station | Coach is excluded when station matching is required |

Test cases must be executed against the application. Record the actual result and pass/fail status in the relevant weekly report rather than assuming that every test has passed.

## 15. Current Limitations

- The system depends on the accuracy of the records stored in its database.
- It does not automatically receive live information from railway operational systems.
- Coach filtering depends on the selection rules implemented in the application.
- Incorrect or missing station, status, or allocation information can affect the selection result.
- The current scope is limited to the first four development weeks.
- Production readiness, performance under heavy load, and integration with external railway systems have not been established by this project documentation.

## 16. Future Enhancements

Possible extensions beyond the current four-week scope include:

- Improved validation and error handling.
- More detailed allocation conflict prevention.
- Search, sorting, and reporting features.
- Better monitoring of coach status and station-wise inventory.
- Additional automated test coverage.
- Deployment to a hosted server after appropriate security and testing work.

These are potential future enhancements and are not claimed as completed features.

## 17. Resources and References

The following official resources can be used to understand the technologies involved.

1. **Python Documentation:** https://docs.python.org/3/
2. **Flask Documentation:** https://flask.palletsprojects.com/
3. **MySQL Documentation:** https://dev.mysql.com/doc/
4. **MySQL Connector/Python:** https://dev.mysql.com/doc/connector-python/en/
5. **SQLAlchemy Documentation:** https://docs.sqlalchemy.org/
6. **Git Documentation:** https://git-scm.com/doc
7. **GitHub Documentation:** https://docs.github.com/
8. **Markdown Guide:** https://www.markdownguide.org/

These links provide reference material for programming, database design, application development, version control, and project documentation.

## 18. Author

**Suvan Mahajan**

B.Tech — Computer Science and Engineering

GitHub: https://github.com/suvan__213

## Conclusion

The Smart Railway Coach Allocation and Management System establishes a structured approach to railway train and coach record management. The four-week development scope focuses on database design, data operations, train and coach management, and rule-based coach filtering.

The repository documents the design, implementation, and validation of these components through the main README and four separate weekly reports.

The project documentation should be updated as development progresses so that the stated functionality, test results, and implementation status accurately reflect the actual code.
