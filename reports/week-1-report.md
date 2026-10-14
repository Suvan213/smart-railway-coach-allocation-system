# Week 1 Report: Project Setup and Database Design

## 1. Introduction

The Smart Railway Coach Allocation and Management System is designed to organize railway train and coach information using a structured database and a Python-based application.

Week 1 focuses on understanding the project requirements, preparing the development environment, identifying the main database entities, and designing the initial database schema.

## 2. Objectives

- Understand the requirements of the railway coach management system.
- Identify the main entities required for the project.
- Design the initial relational database schema.
- Define primary keys and foreign keys.
- Plan the relationships between trains, coaches, requirements, and allocations.

## 3. Project Requirements

The system requires a structured way to maintain:

- Train identification and route details.
- Coach numbers and coach types.
- Coach locations and maintenance status.
- Coach requirements associated with trains.
- Allocation records connecting trains and coaches.

## 4. Database Schema Design

The proposed database consists of four main tables.

### 4.1 Trains

Stores basic train information.

Fields:
- `id`
- `train_number`
- `train_name`
- `source_station`
- `destination_station`

### 4.2 Coaches

Stores information about individual railway coaches.

Fields:
- `id`
- `coach_number`
- `coach_type`
- `current_station`
- `status`

### 4.3 Requirements

Stores coach requirements associated with a train.

Fields:
- `id`
- `train_id`
- `coach_type`
- `quantity`

### 4.4 Allocations

Stores the relationship between trains and coaches.

Fields:
- `id`
- `train_id`
- `coach_id`
- `allocation_status`
- `allocated_at`

## 5. Primary Keys and Foreign Keys

A primary key uniquely identifies a record within a table.

Foreign keys connect related records across tables.

In the proposed design:
- The `train_id` field in Requirements refers to a record in Trains.
- The `train_id` field in Allocations refers to a record in Trains.
- The `coach_id` field in Allocations refers to a record in Coaches.

These relationships help maintain data consistency.

## 6. Development Environment

The planned development environment includes:

- Python for application logic.
- Flask for web application development.
- MySQL for relational data storage.
- SQLAlchemy for object-relational mapping.
- Visual Studio Code for coding.
- MySQL Workbench for database management.

## 7. Expected Deliverables

- Initial project structure.
- Identification of database entities.
- Initial relational schema design.
- Primary-key and foreign-key relationship plan.
- Preparation for database implementation in Week 2.



## 8. Challenges and Observations

The database design must keep train information, coach information, requirements, and allocation records organized separately. Relationships between these entities need to be defined carefully to avoid inconsistent records.

## 9. Conclusion

Week 1 establishes the foundation for the Smart Railway Coach Allocation and Management System. The identified entities and proposed database relationships will guide the database implementation and Python model development in Week 2.


