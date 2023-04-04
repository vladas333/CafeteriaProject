from abc import ABC, abstractmethod

RESERVED_TABLES = {
        "Single": {
            "table_one": {"name": "vacant", "surname": "vacant", "res_time": "vacant"},
            "table_two": {"name": "vacant", "surname": "vacant", "res_time": "vacant"},
            "table_three": {"name": "vacant", "surname": "vacant", "res_time": "vacant"},
        },
        "Double": {
            "table_one": {"name": "free", "surname": "free", "res_time": "free"},
            "table_two": {"name": "free", "surname": "free", "res_time": "free"},
            "table_three": {"name": "free", "surname": "free"},
        },
        "Family": {
            "table_one": {"name": "Vladas", "surname": "Budvytis", "res_time": "23-04-03 18:00"},
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

    def new_reservation(self, people_at_table: int) -> str:
        pass

    def did_you_make_reservation(self, full_name: str) -> None:
        # print(RESERVED_TABLES)
        self.full_name = full_name
        name, surname = map(str, full_name.split(' '))
        self.splited_full_name: dict[0, 1] = full_name.split(" ")

        for key, value in RESERVED_TABLES.items():
            for key1, value1 in value.items():
                for key2, value2 in value1 .items():
                    if value2 == name and surname:
                        print(f"Your table is reserved: {name} {surname}"
                              f"aa{RESERVED_TABLES.items(key)}")
                    break
                else:
                    print("work")
        # ):
        #     print(f"Your table is reserved {self.RESERVED_TABLES['table']}")
        # elif None:
        #     self.new_reservation(
        #         int(
        #             input(
        #                 f"You are not reserved. Please select what size table do you want (1 - Single; 2 - Double; 3 - Family) "
        #             )
        #         )
        #     )

        # # return print(f"Your table is reserved3")


name1 = str(input("Hello. Please, enter your full name (ex.: Name Surname): "))
cafe_project = TableReservation()
cafe_project.did_you_make_reservation(full_name=name1)
