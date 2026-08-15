class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, departmant):
        Employee.__init__(self,name, salary)
        self.departmant = departmant

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        self.programming_language = programming_language
        Employee.__init__(self, name, salary)


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, departmant, team_size, programming_language):
        Manager.__init__(self, name, salary, departmant)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def __str__(self):
        return (f"Name - {self.name}\nsalary - {self.salary}\ndepartmant - {self.departmant}\nteam_size - {self.team_size}\nprogramming_language - {self.programming_language} ")

User_1 = TeamLead("Igor", "1000$", "IT", 5, "Python")

print(User_1)