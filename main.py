import sqlite3
import os
import time


class manager:
    def __init__(self):
        self.store = ""
        self.model = ""
        self.serial_number = ""

    def add(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

    def get_list(self):
        pass

    def terminate(self):
        pass

    def menu(self):
        os.system("cli")
        print("---------------MENU---------------")
        print("1 :) Add")
        print("1 :) Update")
        print("1 :) Remove")
        print("1 :) List")
        print("1 :) Terminate")

    def main(self):
        self.menu()


contacts_manager = manager()
contacts_manager.main()
