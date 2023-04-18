from abc import ABC, abstractmethod
from typing import List, Union



RESERVED_TABLES = {
        "Single": {
            "table_one": {"name": "Vladas", "surname": "Budvytis", "res_time": "23-04-17 19:00"},
            "table_two": {"name": "vacant", "surname": "vacant", "res_time": "vacant"},
            "table_three": {"name": "vacant", "surname": "vacant", "res_time": "vacant"},
        },
        "Double": {
            "table_one": {"name": "free", "surname": "free", "res_time": "free"},
            "table_two": {"name": "free", "surname": "free", "res_time": "free"},
            "table_three": {"name": "free", "surname": "free"},
        },
        "Family": {
            "table_one": {"name": "Vladasas", "surname": "Budvasytis", "res_time": "vacant"},
            "table_two": {"name": "free", "surname": "free", "res_time": "free"},
            "table_three": {"name": "free", "surname": "free", "res_time": "free"},
        },
    }
# class CafeteriaProject(ABC):
# pass

# @abstractmethod
# def new_reservation(self, people_at_table: int) -> str:
#     pass

# @abstractmethod
# def new_reservation(self, people_at_table: int) -> str:
#     pass


class TableReservation:
       
    def __init__(self) -> None:
        self.full_name: str = None
        self.splited_full_name: dict[0, 1] = None
        self.people_at_table: int = None

    def new_reservation(self, people_at_table: int) -> Union[bool, str]:
        self.people_at_table = people_at_table

        if people_at_table == 1:
            print("Single")

        elif people_at_table == 2:
            print("Double")
        
        elif people_at_table >= 3:
            print("Family")

        


        # myDict['student1']['name'] = 'GoLinuxCloud'

    @classmethod
    def get_table_info(cls, full_name: str) ->  str:
        full_name = full_name

        # maybe i should put in method <spliting_name> or just <make_full_name>
        name, surname = map(str, full_name.split(' '))
        splited_full_name: dict[0, 1] = full_name.split(" ")

        for key, value in RESERVED_TABLES.items():
            table_size = key
            for key1, value1 in value.items():
                table_number = key1
                for key2, value2 in value1 .items():
                    if value2 == name and surname:
                        # return string not print
                        print(f"Table info: {table_size} {table_number} "
                              f"{RESERVED_TABLES[key][key1]['res_time']}")

                        print(f"")     

    def did_you_make_reservation(self, full_name: str) -> Union[bool, str]:
        self.full_name = full_name
        name, surname = map(str, full_name.split(' '))

        for key, value in RESERVED_TABLES.items():
            for key1, value1 in value.items():
                for key2, value2 in value1 .items():
                    if value2 == name and surname:
                        # make return only string, not print
                        print(f"Your table is reserved: {name} {surname}")
                        print(f"{TableReservation.get_table_info(self.full_name)}")
                        return True
                    else:
                        return False
        

name1 = str(input("Hello. Please, enter your full name (ex.: Name Surname): "))
cafe_project = TableReservation()
# cafe_project.did_you_make_reservation(full_name=name1)
if cafe_project.did_you_make_reservation(full_name=name1) == True:
    print("You could take a menu")
    
else:
    people_input = int(input("Please. Write (in number), how many people sit at a table: "))
    cafe_project.new_reservation(people_at_table=people_input)

#print(TableReservation.get_table_info("Vladas Budvytis"))
# print(RESERVED_TABLES)
