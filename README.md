# CockroachDB Employee Management System

A Python-based employee and project management system built using CockroachDB Cloud.

## Features

- Python connection to CockroachDB Cloud
- Secure database credentials using environment variables
- Department and employee management
- Project management
- Employee-to-project mapping
- Primary and foreign key relationships
- UUID-based primary keys
- SQL JOIN queries
- Indexes for query performance
- Transaction handling
- TLS/SSL connection to CockroachDB

## Tech Stack

- Python
- CockroachDB Cloud
- Psycopg2
- SQL
- python-dotenv

## Database Tables

### departments
Stores department information.

### employees
Stores employee details and department relationships.

### projects
Stores project information.

### employee_projects
Many-to-many relationship between employees and projects.

## Project Structure

```text
cockroachdb-employee-management/
│
├── app.py
├── db.py
├── schema.sql
├── seed.py
├── queries.py
├── transactions.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md