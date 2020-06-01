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
        print("2 :) Update")
        print("3 :) Remove")
        print("4 :) List")
        print("5 :) Terminate")

        opt = input("Choose a option: ")
        if opt == 1:
            self.add()

        elif opt == 2:
            self.update()

        elif opt == 3:
            self.remove()

        elif opt == 4:
            self.list()

        elif opt == 5:
            self.terminate()

        else:
            opt > 5
            print("Type a number between 1 and 5")

    def main(self):
        os.system("cli")
        self.menu()


contacts_manager = manager()
contacts_manager.main()
