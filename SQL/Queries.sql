SELECT e.emp_no, e.first_name, e.last_name, e.gender, s.salary
FROM employees e 
LEFT JOIN salaries s
ON s.emp_no_sal=e.emp_no;

SELECT * FROM employees
WHERE hire_date LIKE '1986%';


SELECT man.emp_no_man, d.department_no, d.dept_name, man.from_date, man.to_date, e.last_name, e.first_name
FROM dept_emp dept
LEFT JOIN departments d
ON d.department_no=dept.dept_no
LEFT JOIN employees e
ON e.emp_no=dept.emp_no
LEFT JOIN dept_manager man
ON man.dept_no=d.department_no

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM dept_emp dept
LEFT JOIN employees e
ON e.emp_no=dept.emp_no
LEFT JOIN departments d
ON d.department_no=dept.dept_no

SELECT * FROM employees
WHERE first_name LIKE 'Hercules' AND last_name LIKE 'B%';

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM dept_emp dept
LEFT JOIN employees e
ON e.emp_no=dept.emp_no
LEFT JOIN departments d
ON d.department_no=dept.dept_no
WHERE d.dept_name LIKE 'Sales'

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM dept_emp dept
LEFT JOIN employees e
ON e.emp_no=dept.emp_no
LEFT JOIN departments d
ON d.department_no=dept.dept_no
WHERE d.dept_name LIKE 'Sales' OR d.dept_name LIKE 'Development'

Select last_name, count(*)
From   employees
Group By last_name;