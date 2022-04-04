import random 

#assign the value for each specif attributes to calculate the modifier.
targets = 1
weather =1
badge = 1
critical = 1,2
crits = random.choice(critical)
factor= 0.85, 1
randomfactor = random.choice(factor)
stab =1
typeOfPokemon =0.5
burn=1
other=1
#calculating the modifer based on the given value above.
modifier = targets * weather * badge * crits  *randomfactor* stab * typeOfPokemon * burn * other
#assigning the value for specific attributes to calculate damage.
level = 90
power = 110
attacktype = 205
defense = 188
#calculating the damage 
damage = ((((((2*level)/5)+2)*(power*attacktype)/defense)/50)+2)*modifier 
#reducing decimal of damage by 2 decimal places.
print("----------------------------------------")
print("Press[1]: To compare the stat of Charizard(ATTACKER) and Feraligatr(TARGET)\nPress[2]: To Compute the damage")
userchoice=int(input("Type Here:"))
if userchoice == 1:
    print("----------------------------------------")
    print("Charizard\n Level: 90 \n Type: Fire/Flying \n Sp.Attack: 205")
    print("----------------------------------------")
    print("Feraligatr\n Level: 95 \n Type: Water \n Sp.Def: 188")
    print("--------Press [1] to compute the damage-----------")
    choice=int(input("type here:"))
    if choice == 1:
        print("A Lv.90 Charizard attack Lv.95 Feraligatr with fireblast\n a Fire type move with a power of 110")
        print("Attack Damage:",round(damage,2),"not very effective")

    else:
         print("wrong input")

elif userchoice == 2:
    print("A Lv.90 Charizard attack Lv.95 Feraligatr with fireblast\n a Fire type move with a power of 110")
    print("Attack Damage:",round(damage,2),"not very effective")
else:
    print("wrong input")
print("----------------------------------------")



