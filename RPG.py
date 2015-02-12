# By Micah Belden (MR. B)
# Introducing: RPG Open Battle Scenario.

# Import Statements
import random
from tkinter import*
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

# Create a Window
root = Tk()
w = Label(root, text="RPG: Really Preposterous Game.")
w.pack()

# Character Creation
while True:

    messagebox.showinfo("Welcome to Your Doom", "Welcome to RPG Battle . You will be playing a text based battle scenario as our fateful hero, destined to " +
                        "fight evil as their birthright. You must make your way through many encounters, and come out alive at the end of the journey. The game will generate " +
                        "random stats for you and your characters, however all HP amounts are fixed.")

    messagebox.showinfo("Name", "What would you like to name your character?")

    name = simpledialog.askstring("Hero's Name", "Enter your name.")

    # Character stat modifiers, character variables and game command

    strength = random.randint(5,10)
    dexterity = random.randint(5,10)
    intelligence = random.randint(5,10)
    endurance = random.randint(5,10)
    luck = random.randint(5,10)

    weapon = (["sword", random.randint(5,15) + strength - 5],
                ["bow", random.randint(1,20) + dexterity - 5],
               ["staff", random.randint(1,20) + intelligence - 5],)
    critical = random.randint(1,10)

    equip = 0

    heroHP = 100

    potions = 5

    if endurance == 6:
        heroHP += 2
    elif endurance  == 7:
        heroHP += 4
    elif endurance  == 8:
        heroHP += 6
    elif endurance  == 9:
        heroHP += 8
    elif endurance  == 10:
        heroHP += 10



    messagebox.showinfo("Stats","Your stats are: HP = 100; Strength = " + str(strength) + "; Dexterity " + str(dexterity) + "; Intelligence = " + str(intelligence) + "; Endurance = " + str(endurance) +
                         " Luck = " + str(luck) + "")

    messagebox.showinfo("Intro", "You are born into the world of Morbon , your mother a poor vagabond who can barely afford the basic ammenities of life for herself. In her plight," +
                        "to ensure you have a more fulfilled life then she, she abandons you at the footsteps of a church: The Church of Venix. You never learn " +
                        "of your mothers identity, and are raised by a foster family who takes you in before you are able to even remember " +
                        " your unfortunate childhood. You are now 19 years old, and live in a shack house with your mother, father and sister. ")

    messagebox.showinfo("", "HEY! " + name + "! WAKE UP! Something grabbed daddy!....... You open your eyes to your little sister, tears in her eyes, your dark shack "
                        + "room dimly illuminated by a torch. Behind your sister you see a dark figure! You jump out of bed, and see three weapons on the rack above your" +
                        " head board. One is a sword, good for dealing constant high damage but with uncommon criticals, the second a bow, harder to use"
                        + " accounting for lower constant damage, but insures lethality when accuracy is achieved, and the third a staff, a magically imbued scepter with " +
                        " constant medium damage and often hits the enemies weak spots. Which do you take?")

    choice = simpledialog.askinteger("", "1 for sword, 2 for bow, 3 for staff.")

    if choice < 1 or choice > 3:
        messagebox.showinfo("", "You didn't grab a weapon, and the monster brutally eats you and your sister.")
        break

    else:
        equip = weapon[choice - 1][1]
        messagebox.showinfo("", "You grab the " + weapon[choice -1][0])



    messagebox.showinfo("", "Hey! " + name + "! Wake up! It's coming!")
    messagebox.showinfo("", "You stand with your " + str(weapon[choice -1][0]) + " at the ready, and the battle insues!")

    # First Battle/Enemy
    ehp_0 = 50

    round = 0

    herodamage = 0

    run = 0

    while ehp_0 > 0 and heroHP > 0 and run != 1:

        if round == 1:
            action = simpledialog.askinteger("Enemy HP: " + str(ehp_0) + ". Your HP: " +str(heroHP) + ".",  "Press 1 to attack, 2 to potion, or 3 to run like a wuss.")

            if action == 1:
                critical = random.randint(1,10) + luck
                if equip == 1:
                    herodamage = random.randint(5,15) + strength - 5
                    if critical >= 10:
                        herodamage = herodamage * 2
                    else:
                        herodamage = herodamage * 1

                elif equip == 2:
                    herodamage = random.randint(5,15) + strength - 5
                    if critical >= 8:
                        herodamage = herodamage * 2
                    else:
                        herodamage = herodamage * 1
                else:
                    herodamage = random.randint(5,15) + strength - 5
                    if critical >= 9:
                        herodamage = herodamage * 2
                    else:
                        herodamage = herodamage * 1

            ehp_0 = ehp_0 - herodamage
            messagebox.showinfo("", "You did " + str(herodamage) + " damage to the enemy.")
            round -=1

            if action == 2:
                potions -= 1
                heroHP += 30
                round -= 1

            if action == 3:
                messagebox.showinfo("", "You cowardly run from the dark figure, and your selfish actions gets your entire family eaten. You hear" +
                " your sister scream, and grotesque munching noises come from your room. Crimson now lines the hallway. The shadow then eats your parents" +
                " with a crunching *splorch*, and your entire family is now dead. All because of you. You even had 3 weapons at your disposal. right above your head.")
                break

        if round == 0:
            edamage = random.randint(2,8)
            heroHP = heroHP - edamage
            messagebox.showinfo("", "The ghostly figure does " + str(edamage) + " damage.")
            round += 1

    messagebox.showinfo("", "After destroying teh ghastly figure, you look at your sister, plated agaisnt the wall, ")

    decision = 0
    simpledialog.askinteger("", "Press 1 go search your parents room for survivors, or 2 to take your sister and run.")

    if decision == 1:
        messagebox.showinfo("", "You pick up your sister and carry her out of the house.... Where are we going, she asks, and that is a good question; where are you going?")
        simpledialog.askinteger("", "1 to go to the church to pray for help, 2 to go to the blacksmith for weapons, 3 to skip town, or 4 to search the town for help.")
    if decision == 2:
        messagebox.showinfo("", "You creep your way through the hallway with your " + str(weapon[choice -1][0]) + " clutched tight, heading for your parents room. " +
                            "An eerie noise echoes through the wooden walls... You approach the door to your parents room and look in, but there is no one around. " +
                            "As you look into the room, another shadow pops out from around the wall and grabs your head, then proceeds to promptly rip it off. Sad day.")
    break