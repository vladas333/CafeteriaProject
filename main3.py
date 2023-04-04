from abc import ABC, abstractmethod


class CafeteriaProject(ABC):
    pass
    @abstractmethod
    def new_reservation(self, people_at_table: int) -> str:
        pass

    @abstractmethod
    def new_reservation(self, people_at_table: int) -> str:
        pass


class TableReservation(CafeteriaProject):
    RESERVED_TABLES = {
            "Single1": { "name": "first_name", "surname": "sir_name"},
            "Single2": {"name": "first_name", "surname": "sir_name"},
            "Single3": {"name": "Petras", "surname": "Petraitis"},
            "Doble1": {"name": "first_name", "surname": "sir_name"},
            "Doble2": {"name": "Jonas", "surname": "Jonaitis"},
            "Doble3": {"name": "first_name", "surname": "sir_name"},
            "Family1": {"name": "Vladas", "surname": "Budvytis"},
            "Family2": {"name": "first_name", "surname": "sir_name"},
            "Family3": {"name": "first_name", "surname": "sir_name"},
        }

    def __init__(self) -> None:
        self.full_name: str = None

    def new_reservation(self, people_at_table: int) -> str:
        # with if select table and write reservation
        return print(f"works")

    def did_you_make_reservation(self, full_name: str) -> None:
        self.full_name = full_name
        splited_full_name: dict[0, 1] = full_name.split(" ")
        
        if splited_full_name[0] in self.RESERVED_TABLES["name"] and splited_full_name[1] in self.RESERVED_TABLES["surname"]:
            print(f"Your table is reserved {self.RESERVED_TABLES['table']}")
        # else: self.new_reservation(int(input(f"You are not reserved. Please select what size table do you want (1 - Single; 2 - Double; 3 - Family) ")))
            
        # return print(f"Your table is reserved3")
    
    


name1 = str(input("Enter your full name (ex.: Name Surname): "))
cafe_project = TableReservation()
cafe_project.did_you_make_reservation(full_name=name1)