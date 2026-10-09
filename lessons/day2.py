
print("SAMPLE INVENTORY - LAB 201")

SID = input("SAMPLE ID: ")
STY = input("Sample type: ")
NSP = int(input("Number of Samples: "))
STP = float(input("Storage Temperature (in °C): "))

print("SAMPLE INFORMATION")
print(SID, STY, NSP, STP, sep="\n")

if NSP > 0:
    print("Sample count accepted")
    reagent_vol = 250
    total_vol = round(reagent_vol * NSP / 1000, 2)
    print(f"Total volume of reagent required is {total_vol:.2f} mL")
else:
    print("Invalid sample count")

if STP > 8:
    print("Check: temperature too high!")
elif STP == 0:
    print("Check storage protocol")
elif STP > 0:
    print("Refrigerated storage range")
else:
    print("Freezer storage range")



