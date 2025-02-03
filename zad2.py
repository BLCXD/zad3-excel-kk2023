print("Witaj w programie do tworzenia Listy Zakupów Weekendowych!")
produkty = []
ilosc = []
while True:
    item = input("Podaj produkt lub wpisz 'koniec', aby zakończyć dodawanie produktów: ")

    #print(produkty)
    if item == 'koniec':
        print("twoja lista")
        for j in produkty:
          for i in ilosc:
              print(f'{j} - {i}szt.')
        break


    else:
        produkty.append(item)
        count = int(input("Podaj ilość: "))
        ilosc.append(count)
