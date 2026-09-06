from db import get_connection


def seed_data():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO departments (department_name, location)
                VALUES
                    ('Engineering', 'Chennai'),
                    ('Data', 'Bangalore'),
                    ('HR', 'Hyderabad')
                ON CONFLICT (department_name) DO NOTHING;
            """)

            cursor.execute("""
                INSERT INTO employees
                    (first_name, last_name, email, job_title, salary, department_id)
                SELECT
                    'Arun',
                    'Kumar',
                    'arun.kumar@example.com',
                    'Data Engineer',
                    900000,
                    department_id
                FROM departments
                WHERE department_name = 'Data'
                ON CONFLICT (email) DO NOTHING;
            """)

            cursor.execute("""
                INSERT INTO employees
                    (first_name, last_name, email, job_title, salary, department_id)
                SELECT
                    'Meena',
                    'Ravi',
                    'meena.ravi@example.com',
                    'Backend Engineer',
                    850000,
                    department_id
                FROM departments
                WHERE department_name = 'Engineering'
                ON CONFLICT (email) DO NOTHING;
            """)

            cursor.execute("""
                INSERT INTO projects
                    (project_name, project_status, start_date, budget)
                VALUES
                    ('HR Analytics Platform', 'ACTIVE', current_date, 1500000),
                    ('Employee Portal', 'ACTIVE', current_date, 1000000);
            """)

        conn.commit()
        print("Sample data inserted successfully!")

    except Exception as e:
        conn.rollback()
        print("Data insert failed:")
        print(e)

    finally:
        conn.close()


if __name__ == "__main__":
    seed_data()