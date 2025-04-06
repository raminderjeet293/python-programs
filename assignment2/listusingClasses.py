class ListManager:
    def __init__(self):
        self.my_list = []

    def append_element(self, element):
        self.my_list.append(element)
        print(f"'{element}' added to the list.")

    def delete_element(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
            print(f"'{element}' removed from the list.")
        else:
            print("Element not found.")

    def display_elements(self):
        if self.my_list:
           print("List Elements:")
           for item in self.my_list:
               print(item)
        else:
            print("List is empty.")


lm = ListManager()

while True:
    print("\n==== List-Menu ====")
    print("1. Append Element")
    print("2. Delete Element")
    print("3. Display List")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        elem = input("Enter element to append: ")
        lm.append_element(elem)

    elif choice == "2":
        elem = input("Enter element to delete: ")
        lm.delete_element(elem)

    elif choice == "3":
        lm.display_elements()

    elif choice == "4":
        print("Exiting.")
        break

    else:
        print("Invalid choice.")
