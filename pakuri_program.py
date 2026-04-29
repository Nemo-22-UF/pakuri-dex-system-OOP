from pakudex import Pakudex
from pakuri import Pakuri

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity > 0:
                break
            else:
                print("Please enter a valid size.")
        except ValueError:
            print("Please enter a valid size.")

    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.")

    while True:
        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")
        choice = input("What would you like to do? ")

        if choice == "1":
            species = pakudex.get_species_array()
            if species:
                print("Pakuri In Pakudex:")
                for i, s in enumerate(species, 1):
                    print(f"{i}. {s}")
            else:
                print("No Pakuri in Pakudex yet!")

        elif choice == "2":
            species = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(species)
            if stats:
                print(f"Species: {species}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")
            else:
                print("Error: No such Pakuri!")

        elif choice == "3":
            species = input("Enter the name of the species to add: ")
            if pakudex.add_pakuri(species):
                print(f"Pakuri species {species} successfully added!")
            else:
                if pakudex.get_size() == pakudex.get_capacity():
                    print("Error: Pakudex is full!")
                else:
                    print("Error: Pakudex already contains this species!")

        elif choice == "4":
            species = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(species):
                print(f"{species} has evolved!")
            else:
                print("Error: No such Pakuri!")

        elif choice == "5":
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == "6":
            print("Thanks for using Pakudex! Bye!")
            break

        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()
