level1 = "The way of darkness"

level2 = "The castle"

level3 = "Final - The demolisher"





class monster():

    def __init__(self,name,hp,armmor,attack_power,power):
        self.name = name
        self.hp = hp
        self.armmor = armmor
        self.attack_power = attack_power
        self.power = power

    def __str__ (self):

        return f" attack {self.attack} armmor {self.armmor} name {self.name} damage {self.attack_power} hp {self.hp} power {self.power}"

class mini_souls(monster):

    def alive(self):
        print("The mini souls are alive and sleeping !")

    def attacknpc(self):

        damged_main = self.attack_power - main_character.hp

        power_minus = 1 - self.power

        print(f"They attacked you ! dmg:{damged_main} your hp {main_character.hp}")

    def flee(self):

        print("they are 10 hp and fleeing ! ")

    def passive(self):

        pass

    def die(self):

        print(f"{mini_souls.name} is dead !")

class big_souls(monster):




    def alive(self):

        print("The mini souls are alive and sleeping !")



    def flee(self):

        pass

    def passive(self):

        pass


    def die(self):
        print(f"{big_souls.name} is dead !")

class main_character(monster):

    def __init__(self, name, hpm, attack_power, armmor, power):
        self.name= name
        self.hpm = hpm
        self.attack_power = attack_power
        self.armmor = armmor
        self.power = power

    def explore1(self):
        print ("exploring the level ! ")

        print (f"you found  mini souls , {mini_souls1.name}")

    def explore2(self):

        print ("exploring the level ! ")

        print (f"you found  mini souls , {mini_souls2.name}")

    def explore3(self):

        print ("exploring the level ! ")

    def attack(self):

        return f"You are attacking with: {self.attack_power}"  # ✅ Use return instead of print


    def die(self):
        print(f"{main_character.name} is dead !")

    def interact(self):
        while True :
            inter = input ("attack or walk away : atk or wlk")

            if inter == "atk":
                self.attack()
class xp():
    def __init__(self,xp):
        self.xp = xp






mini_souls1 = mini_souls("void_minions",200,20,25,10)

mini_souls2 = mini_souls("hell_hounds",250,20,30,15)

mini_souls3 = mini_souls("hell_roaches",250,20,30,15)

big_souls1 = big_souls("void_seekres",1200,100,75,100)

big_souls2 = big_souls("Laser_eyes",1200,100,75,100)

boss = big_souls("The demolisher",5000,520,100,4500)

main_characterf = main_character(input, 2500, 200, 500, 50)  # ✅ Now has 5 arguments

EXP = xp(100)

def attacknpc1():

    damged_main =  main_characterf.hpm - mini_souls1.attack_power

    power_minus = 50 - mini_souls1.power

    print(f"The monster  atk {mini_souls1.attack_power}")

    print(f"They attacked you ! your hp: {damged_main} / {main_characterf.hpm} soul power : {mini_souls1.power} ")

def attack_mainf1():

    main_did = mini_souls1.hp - main_characterf.attack_power

    power_minusM = main_characterf.power - 25

    print(f"you attacked ! soul hp: {main_did} / {mini_souls1.hp} hero power : {power_minusM} ")

    if main_did == 0 :

        print (f"EARNED  {EXP.xp}Xp ")

        main_character.explore2(main_characterf)

    else :
        pass

def attack_mode():

    while True :

        fiorwlk = input(f"Fight mode : Your HP : {main_characterf.hpm} / {main_characterf.hpm} do you want to fight or walk away explor more  ? fi | wlk ")

        if fiorwlk == "fi" :
            aaordd =input ("for attacking  : aa |||| for dodging : dd ")
            if aaordd == "aa" :
                attack_mainf1()
            else :
                attacknpc1()

            if aaordd == "dd" :
                print ("you dodged do you want to counter ?  for attacking  : aa ")
                cu =  input ()
                if cu == "aa" :
                   attack_mainf1()
        elif fiorwlk == "wlk" :
            explore2()

        else :
            attacknpc1()

def menulevels():

    while True :

        choosing_charachter = input ("Choose a chatachter : Fighter || rouge || Mage || Marks man ")

        if choosing_charachter == "Fighter" :

            print(f" YOUR NAME {main_characterf.name} THE Marks man HP  {main_characterf.hpm} THE Marks man POWER {main_characterf.power} THE Marks man DMG {main_characterf.attack_power} " )


        elif choosing_charachter == "rouge" :

            print(f" YOUR NAME {main_characterf.name} THE Marks man HP  {main_characterf.hpm} THE Marks man POWER {main_characterf.power} THE Marks man DMG {main_characterf.attack_power} " )


        elif choosing_charachter == "Mage" :

            print(f" YOUR NAME {main_characterf.name} THE Marks man HP  {main_characterf.hpm} THE Marks man POWER {main_characterf.power} THE Marks man DMG {main_characterf.attack_power} " )


        elif choosing_charachter == "Marks man" :

            print(f" YOUR NAME {main_characterf.name} THE Marks man HP  {main_characterf.hpm} THE Marks man POWER {main_characterf.power} THE Marks man DMG {main_characterf.attack_power} " )
        else :
            print ("invalid")

        choosing_level = input("Choose a battle : 1 | 2 | 3  ")

        if choosing_level == "1" :

            print (f"You are in {level1}")

            playing = input ("You are in a dark road do you want to explore it ? Y | N ")

            if playing == "y" or "Y":

                main_character.explore1(main_characterf)

                attack_mode()

                break
        elif choosing_level == "2" :

            print (f"You are in {level2}")

            playing = input ("You are in a dark road do you want to explore it ? Y | N ")

            if playing == "y" or "Y":

                main_character.explore1(main_characterf)

                attack_mode()

                break

        elif choosing_level == "3" :

            print (f"You are in {level3}")

            playing = input ("You are in a dark road do you want to explore it ? Y | N ")

            if playing == "y" or "Y":

                main_character.explore1(main_characterf)

                attack_mode()

                break

menulevels()

#print(mini_souls1.attack_power)
#print(main_characterf.hpm)

#attacknpc1()
#attack_mainf1()
