# CockroachDB Employee Management System

A Python-based Employee and Project Management System built using **CockroachDB Cloud**.

This project demonstrates practical experience with CockroachDB, including database connectivity, relational schema design, SQL queries, transactions, indexing, and secure cloud database configuration.

## Tech Stack

- Python
- CockroachDB Cloud
- PostgreSQL-compatible SQL
- psycopg2
- python-dotenv
- Git & GitHub

## Features

- Connect Python applications to CockroachDB Cloud
- Employee management
- Department management
- Project management
- Employee-to-project relationships
- UUID-based primary keys
- Primary and foreign key relationships
- SQL JOIN queries
- Database indexing
- Transaction handling
- Seed/sample data
- Secure credential management using environment variables
- SSL-secured database connection

## Project Structure

```text
cockroachdb-employee-management/
│
├── app.py
├── db.py
├── main.py
├── queries.py
├── transactions.py
├── seed.py
├── schema.sql
├── requirements.txt
├── .gitignore
└── README.md
```

## CockroachDB Architecture

```text
Python Application
        |
        v
    psycopg2
        |
        v
Secure SSL Connection
        |
        v
CockroachDB Cloud
        |
        v
Employee / Department / Project Tables
```

## Database Design

The project uses relational tables for managing employees, departments, projects, and their relationships.

CockroachDB features demonstrated include:

- Distributed SQL database connectivity
- PostgreSQL-compatible SQL
- UUID primary keys
- Foreign key constraints
- Indexes
- JOIN operations
- ACID transactions

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd cockroachdb-employee-management
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file locally:

```text
DATABASE_URL=your_cockroachdb_connection_string
```

The `.env` file is excluded from Git using `.gitignore` so database credentials are not committed to the repository.

## Run the Project

Create the database schema:

```bash
python main.py
```

Load sample data:

```bash
python seed.py
```

Run SQL query examples:

```bash
python queries.py
```

Run transaction examples:

```bash
python transactions.py
```

## Example Operations

The project demonstrates common database operations such as:

- Creating employee records
- Retrieving employee information
- Joining employees with departments
- Managing projects
- Executing transactions
- Querying CockroachDB using Python

## Security

Database credentials are stored using environment variables and are not committed to source control.

CockroachDB Cloud connections use SSL/TLS certificate verification.

## Purpose

This project was created to demonstrate hands-on experience integrating Python applications with CockroachDB Cloud and implementing SQL database operations, relational data modeling, and transaction management.
