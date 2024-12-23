class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Employee Name: {self.name}, ID: {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return f"{self.name} управляет проектом в отделе {self.department}."

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} проводит обслуживание в {self.specialization}."

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.subordinates = []

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        team_info = f"Команда, которой управляет {self.name}:\n"
        for employee in self.subordinates:
            team_info += employee.get_info() + "\n"
        return team_info

employee = Employee("Иван", 1010800)
manager = Manager("Артем", 1028765, "Айти")
technician = Technician("Антон", 1031236, "Разработка ИИ")
tech_manager = TechManager("Даниил", 1041278, "Проектирование", "Разработка приложений")

print(employee.get_info())
print(manager.get_info())
print(manager.manage_project())
print(technician.get_info())
print(technician.perform_maintenance())
print(tech_manager.get_info())
print(tech_manager.manage_project())
print(tech_manager.perform_maintenance())

tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print(tech_manager.get_team_info())