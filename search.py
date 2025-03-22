import csv

def search(document):
    searching = True
    while searching:
        value = input("What criteria do you want to search?")
        match(value):
            case "name":
                search_by_name(document)
            case "color":
                search_by_color(document)
            case "back":
                searching = False

def search_by_name(document):
    card_name = input("Type in the name of the card: ")
    with open(document, 'r') as document:
        reader = csv.reader(document)
        for row in reader:
            if card_name.lower() in row[0].lower():
                print(row)

def search_by_color(document):
     card_color = input("Type in the mana color you want: ")
     with open(document, 'r') as document:
          reader = csv.reader(document)
          for row in reader:
               if card_color.lower() in row[1].lower():
                    print(row[0], row[1])