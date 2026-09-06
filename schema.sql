CREATE TABLE IF NOT EXISTS departments (
    department_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    department_name STRING NOT NULL UNIQUE,
    location STRING,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS employees (
    employee_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name STRING NOT NULL,
    last_name STRING NOT NULL,
    email STRING NOT NULL UNIQUE,
    job_title STRING NOT NULL,
    salary DECIMAL(12,2),
    department_id UUID,
    hired_date DATE DEFAULT current_date,
    created_at TIMESTAMPTZ DEFAULT now(),

    CONSTRAINT fk_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

CREATE TABLE IF NOT EXISTS projects (
    project_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_name STRING NOT NULL,
    project_status STRING NOT NULL DEFAULT 'ACTIVE',
    start_date DATE,
    end_date DATE,
    budget DECIMAL(14,2),
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS employee_projects (
    employee_id UUID NOT NULL,
    project_id UUID NOT NULL,
    assigned_at TIMESTAMPTZ DEFAULT now(),
    role_in_project STRING,

    PRIMARY KEY (employee_id, project_id),

    CONSTRAINT fk_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),

    CONSTRAINT fk_project
        FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
);

CREATE INDEX IF NOT EXISTS idx_employees_department
ON employees(department_id);

CREATE INDEX IF NOT EXISTS idx_employees_email
ON employees(email);

CREATE INDEX IF NOT EXISTS idx_projects_status
ON projects(project_status);