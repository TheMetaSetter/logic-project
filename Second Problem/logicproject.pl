% Các đối tượng trong môi trường công ty
employee(john).
employee(susan).
employee(mike).
employee(anna).
employee(eric).
employee(lisa).
employee(steve).
employee(kate).
employee(peter).
employee(emily).

department(marketing).
department(hr).
department(tech).
department(accounting).
department(operations).
department(sales).
department(legal).
department(research).

manager(manager1).
manager(manager2).
manager(manager3).
manager(manager4).
manager(manager5).

project(project1).
project(project2).
project(project3).
project(project4).
project(project5).
project(project6).
project(project7).
project(project8).
project(project9).
project(project10).

task("Develop marketing strategy").
task("Hiring new employees").
task("Implement new technology").
task("Budget planning").
task("Performance evaluation").
task("Client acquisition").
task("Legal compliance").
task("Market research").
task("Product development").
task("Strategic planning").

% Quan hệ giữa nhân viên và phòng ban
works_in(john, marketing).
works_in(susan, hr).
works_in(mike, tech).
works_in(anna, accounting).
works_in(eric, operations).
works_in(lisa, sales).
works_in(steve, legal).
works_in(kate, research).
works_in(peter, marketing).
works_in(emily, tech).

% Quan hệ giữa phòng ban và quản lý
manager(marketing, manager1).
manager(hr, manager2).
manager(tech, manager3).
manager(accounting, manager4).
manager(operations, manager5).
manager(sales, manager1).
manager(legal, manager2).
manager(research, manager3).

% Quan hệ giữa quản lý và công việc quản lý
manages(manager1, project1).
manages(manager2, project2).
manages(manager3, project3).
manages(manager4, project4).
manages(manager5, project5).
manages(manager1, project6).
manages(manager2, project7).
manages(manager3, project8).
manages(manager4, project9).
manages(manager5, project10).

% Quan hệ giữa các dự án và công việc
task(project1, "Develop marketing strategy").
task(project2, "Hiring new employees").
task(project3, "Implement new technology").
task(project4, "Budget planning").
task(project5, "Performance evaluation").
task(project6, "Client acquisition").
task(project7, "Legal compliance").
task(project8, "Market research").
task(project9, "Product development").
task(project10, "Strategic planning").

% Quan hệ giữa nhân viên và quản lý trực tiếp
directly_managed_by(Employee, Manager) :-
    works_in(Employee, Department),
    manager(Department, Manager).

% Quan hệ giữa nhân viên và quản lý gián tiếp
indirectly_managed_by(Employee, Manager) :-
    directly_managed_by(Employee, Manager).
indirectly_managed_by(Employee, Manager) :-
    directly_managed_by(Employee, Intermediate),
    indirectly_managed_by(Intermediate, Manager).

% Quan hệ giữa các phòng ban và dự án
project_in_department(Project, Department) :-
    task(Project, _),
    works_in(_, Department),
    manages(Manager, Project),
    manager(Department, Manager).

% Quan hệ giữa các công việc và nhân viên thực hiện
task_assigned_to(Task, Employee) :-
    works_in(Employee, Department),
    project_in_department(Project, Department),
    task(Project, Task).

% Quan hệ giữa các nhân viên có cùng quản lý
colleagues(Employee1, Employee2) :-
    works_in(Employee1, Department),
    works_in(Employee2, Department),
    Employee1 \= Employee2,
    directly_managed_by(Employee1, Manager),
    directly_managed_by(Employee2, Manager).

% Quan hệ giữa các phòng ban cùng một quản lý
same_manager(Department1, Department2) :-
    manager(Department1, Manager),
    manager(Department2, Manager),
    Department1 \= Department2.

manages_projects(Manager, Projects) :-
    findall(Project, manages(Manager, Project), Projects).
