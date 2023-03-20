#simple weight converter code
Weight = input("Input your weight: ")
typeWeight = input ("(K)kg or (L)lbs: ")
if typeWeight == "K":
    lbsWeight = int(Weight) * 2.2
    print("Your weight in pounds is " + str(lbsWeight))
elif typeWeight == "L":
    kgWeight = int(Weight) / 2.2
    print("Your weight in kg is " + str(kgWeight))
else:
    print("Invalid Input. Retry")