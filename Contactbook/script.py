import json

names = []

print("Hi how are you?")

nextstep = "Y"

while nextstep == "Y":

    name = {}

    choice = input("What do you want to do? LIST or ADD?")

    if choice == "LIST":
        with open("data.txt") as json_file:
            names = json.load(json_file)
            for name in names:
                print(str(name["Index"]) + " " + name["Vorname"] + " " + name["Nachname"])

    elif choice == "ADD":
        name["Vorname"] = input("Vorname: ")
        name["Nachname"] = input("Nachname: ")
        name["Index"] = len(names) + 1
        names.append(name)
        with open("data.txt", "w") as outfile:
            json.dump(names, outfile)
    else:
        print("Please choose LIST or ADD")

    nextstep = input("Do you want to continue (Y)? or close (C)?")
    if nextstep != "Y":
        print("Thanks: See you")
        break

