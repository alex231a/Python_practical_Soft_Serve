class Employee:
    def __init__(self, str_full_name, **kwargs):
        self.str_full_name = str_full_name
        self.list_full_name = self.str_full_name.split(' ')
        self.name = self.list_full_name[0]
        self.lastname = self.list_full_name[1]
        for k, v in kwargs.items():
            setattr(self, k, v)


john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
print(mary.lastname)
print(richard.height)
print(giancarlo.nationality)
print(john.name)