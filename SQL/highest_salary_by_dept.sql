-- Given tables
-- Employee
-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Henry | 80000  | 2            |
-- | 3  | Sam   | 60000  | 2            |
-- | 4  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+
-- and 
-- Department
-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+
-- Find the name and dept name of person from each dapt with highest salary
-- Author: John Feilmeier

SELECT Department.Name AS Department, Employee.Name AS Employee, Employee.Salary
  FROM Employee
  JOIN Department
    ON Employee.DepartmentId = Department.Id
  WHERE (DepartmentId, Salary)
    IN (SELECT DepartmentId, MAX(Salary)
       FROM Employee
       GROUP BY DepartmentId
       )
