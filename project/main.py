mat = ["mat1", "Mat", 5000, 21, 0]
mobil = ["mobil1", "Mobil", 1, 19999, 0]
bil = ["bil1","Bil", 400, 500000, 0]
dator = ["Dator1", "Dator", 10000, 15000, 0]


def QuantityMat():
    print("Choose quantity:")
    quantity = input()
    if int(quantity) >= 0 and int(quantity) <= mat[2]:
        mat[4] = mat[4] + int(quantity)
        mat[2] = mat[2] - int(quantity)
        Shop()
    elif int(quantity) < 0:
        print("You can't buy less then 0!")
        QuantityMat()
    elif int(quantity) > mat[2]:
        print("We don't have that many!")
        QuantityMat()

def QuantityMobil():
    print("Choose quantity:")
    quantity = input()
    if int(quantity) >= 0 and int(quantity) <= mobil[2]:
        mobil[4] = mobil[4] + int(quantity)
        mobil[2] = mobil[2] - int(quantity)
        Shop()
    elif int(quantity) < 0:
        print("You can't buy less then 0!")
        QuantityMobil()
    elif int(quantity) > mobil[2]:
        print("We don't have that many!")
        QuantityMobil()

def QuantityBil():
    print("Choose quantity:")
    quantity = input()
    if int(quantity) >= 0 and int(quantity) <= bil[2]:
        bil[4] = bil[4] + int(quantity)
        bil[2] = bil[2] - int(quantity)
        Shop()
    elif int(quantity) < 0:
        print("You can't buy less then 0!")
        QuantityBil()
    elif int(quantity) > bil[2]:
        print("We don't have that many!")
        QuantityBil()

def QuantityDator():
    print("Choose quantity:")
    quantity = input()
    if int(quantity) >= 0 and int(quantity) <= dator[2]:
        dator[4] = dator[4] + int(quantity)
        dator[2] = dator[2] - int(quantity)
        Shop()
    elif int(quantity) < 0:
        print("You can't buy less then 0!")
        QuantityDator()
    elif int(quantity) > dator[2]:
        print("We don't have that many!")
        QuantityDator()

def Shelf():
    print(mat[1] + ": " + str(mat[3]) + "kr - " + str(mat[2]) + "st")
    print(mobil[1] + ": " + str(mobil[3]) + "kr - " + str(mobil[2]) + "st")   
    print(bil[1] + ": " + str(bil[3]) + "kr - " + str(bil[2]) + "st")
    print(dator[1] + ": " + str(dator[3]) + "kr - " + str(dator[2]) + "st")
    print("Choose product: ")
    product = input()
    if product == "Mat" or product == "mat":
        QuantityMat()
    elif product == "Mobil" or product == "mobil":
        QuantityMobil()
    elif product == "Bil" or product == "bil":
        QuantityBil()
    elif product == "Dator" or product == "dator":
        QuantityDator()
    else:
        print("We don't have that!")
        Shelf()

def Shop():
    print("Shop:")
    print("1.buy")
    print("0.back to menu")
    shop = input()
    if shop == "1":
        Shelf()
    elif shop == "0":
        Main()
    else:
        Shop()

def removeMat():
    print("Choose quantity:")
    quantity = input()
    if int(quantity) >= 0 and int(quantity) <= mat[4]:
        mat[4] = mat[4] - int(quantity)
        mat[2] = mat[2] + int(quantity)
        Basket()
    elif int(quantity) < 0:
        print("You can't remove less then 0!")
        removeMat()
    elif int(quantity) > mat[4]:
        print("We don't have that many in you'r basket!")
        removeMat()

def removeMobil():
    print("Choose quantity:")
    quantity = input()
    if int(quantity) >= 0 and int(quantity) <= mobil[4]:
        mobil[4] = mobil[4] - int(quantity)
        mobil[2] = mobil[2] + int(quantity)
        Basket()
    elif int(quantity) < 0:
        print("You can't remove less then 0!")
        removeMobil()
    elif int(quantity) > mobil[4]:
        print("We don't have that many in you'r basket!")
        removeMobil()

def removeBil():
    print("Choose quantity:")
    quantity = input()
    if int(quantity) >= 0 and int(quantity) <= bil[4]:
        bil[4] = bil[4] - int(quantity)
        bil[2] = bil[2] + int(quantity)
        Basket()
    elif int(quantity) < 0:
        print("You can't remove less then 0!")
        removeBil()
    elif int(quantity) > bil[4]:
        print("We don't have that many in you'r basket!")
        removeBil()

def removeDator():
    print("Choose quantity:")
    quantity = input()
    if int(quantity) >= 0 and int(quantity) <= dator[4]:
        dator[4] = dator[4] - int(quantity)
        dator[2] = dator[2] + int(quantity)
        Basket()
    elif int(quantity) < 0:
        print("You can't remove less then 0!")
        removeDator()
    elif int(quantity) > dator[4]:
        print("We don't have that many in you'r basket!")
        removeDator()

def removeProduct():
    print("Choose product:")
    if mat[4] > 0:
        prisMat = int(mat[3])*int(mat[4])
        print("Mat: " + str(prisMat) + "kr - " + str(mat[4]) + "st")
    if mobil[4] > 0:
        prisMobil = int(mobil[3])*int(mobil[4])
        print("Mobil: " + str(prisMobil) + "kr - " + str(mobil[4]) + "st")
    if bil[4] > 0:
        prisBil = int(bil[3])*int(bil[4])
        print("Bil: " + str(prisBil) + "kr - " + str(bil[4]) + "st")
    if dator[4] > 0:
        prisDator = int(dator[3])*int(dator[4])
        print("Dator: " + str(prisDator) + "kr - " + str(dator[4]) + "st")
    remove = input()
    if mat[4] > 0 and remove == "Mat" or remove == "mat":
        removeMat()
    elif mobil[4] > 0 and remove == "Mobil" or remove == "mobil":
        removeMobil()
    elif bil[4] > 0 and remove == "Bil" or remove == "bil":
        removeBil()
    elif dator[4] > 0 and remove == "Dator" or remove == "dator":
        removeDator()
    else:
        print("You don't have one of those in you'r basket!")
        removeProduct()


def emptyBasket():
    mat[2] = 5000
    mat[4] = 0
    mobil[2] = 1
    mobil[4] = 0
    bil[2] = 400
    bil[4] = 0
    dator[2] = 10000
    dator[4] = 0
    Basket()

def Basket():
    if mat[4] == 0 and mobil[4] == 0 and bil[4] == 0 and dator[4] == 0:
        print("You'r Basket:")
        print("\"Empty\"")
        print("1. Remove Product")
        print("2. Empty basket")
        print("0. Back to menu")
        basket = input()
        if basket == "0":
            Main()
        else:
            Basket()
    else:
        print("You'r Basket:")
        if mat[4] > 0:
            prisMat = int(mat[3])*int(mat[4])
            print("Mat: " + str(prisMat) + "kr - " + str(mat[4]) + "st")
        if mobil[4] > 0:
            prisMobil = int(mobil[3])*int(mobil[4])
            print("Mobil: " + str(prisMobil) + "kr - " + str(mobil[4]) + "st")
        if bil[4] > 0:
            prisBil = int(bil[3])*int(bil[4])
            print("Bil: " + str(prisBil) + "kr - " + str(bil[4]) + "st")
        if dator[4] > 0:
            prisDator = int(dator[3])*int(dator[4])
            print("Dator: " + str(prisDator) + "kr - " + str(dator[4]) + "st")
        print("1. Remove Product")
        print("2. Empty basket")
        print("0. Back to menu")
        basket = input()
        if basket == "1":
            removeProduct()
        elif basket == "2":
            emptyBasket()
        elif basket == "0":
            Main()
        else:
            Basket()

def Restart():
    pris = mat[4] * mat[3] + mobil[4] * mobil[3] + bil[4] * bil[3] + dator[4] * dator[3]
    print("You paid: " + str(pris) + "kr")
    restart = input("Type: /Restart ")
    if restart == "/Restart" or restart == "/restart":
        mat[2] = 5000
        mat[4] = 0
        mobil[2] = 1
        mobil[4] = 0
        bil[2] = 400
        bil[4] = 0
        dator[2] = 10000
        dator[4] = 0
        Start()
    else:
        Restart()

def cacheOut():
    pris = mat[4] * mat[3] + mobil[4] * mobil[3] + bil[4] * bil[3] + dator[4] * dator[3]
    print("That will be:" + str(pris) + "kr")
    print("1. Pay")
    print("0. Back to menu")
    out = input()
    if out == "1":
        Restart()
    elif out == "0":
        Main()
    else:
        cacheOut()

def Main():
    print("1. Shop")
    print("2. Basket")
    print("3. Cache out")
    print("4. Exit")
    main = input()
    if main == "1":
        Shop()
    elif main == "2":
        Basket()
    elif main == "3":
        cacheOut()
    elif main == "4":
        Start()
    else:
        Main()

def Start():
    start = input("Type: /Start  ")
    if start == "/Start" or start == "/start":
        Main()
    elif start == "/Stop" or start == "/stop":
        import sys
        sys.exit()
    else:
        Start()


Start()
