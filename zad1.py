# Tutaj pisz swój kod, młody padawanie ;-)
print("Aby zakończyć działanie programu naciśnij klawisz ENTER bez wprowadzania komunikatu")


while True:
    x = input("Wprowadź dowolny komunikat: ")
    if x == '':
        print("Dziękuję za miło spędzony czas")
        break
    else:
        y = x[::-1]
        y = y.capitalize()
        print(y)



