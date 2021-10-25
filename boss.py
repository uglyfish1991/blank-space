import time
import sys
import random
​
morale=10
​
health=10
​
karenhelath=10
​
​
​
def start_game():
    global morale
    morale=10
    global health
    health=10
    global karenhelath
    karenhelath=10
​
    print("Welcome to")
    time.sleep(0.1)
    print("""\033[3;33;41m 
        )                                      (                        
    ( /(                               (      )\ )        (            
    )\())        (        )        )   )\    (()/(   (    )\ )     (   
    ((_)\    (    )(      (      ( /(  ((_)    /(_))  )\  (()/(    ))\  
    _((_)   )\  (()\     )\  '  )(_))  _     (_))   ((_)  /(_))  /((_) 
    | \| |  ((_)  ((_)  _((_))  ((_)_  | |    | |     (_) (_) _| (_))   
    | .` | / _ \ | '_| | '  \() / _` | | |    | |__   | |  |  _| / -_)  
    |_|\_| \___/ |_|   |_|_|_|  \__,_| |_|    |____|  |_|  |_|   \___|  
                                                                        
                                                            
    \033[0;0m""")
    time.sleep(0.1)
    input("Press Enter to wake up")
    bed()
​
def stat_check():
    global morale
    if morale >0:
        return True
    else:
        game_over()
​
def demoralised():
    print("You have become utterly demoralised and given up for today, you crawl back to bed hoping tomorrow will be better")
    game_over()
​
def game_over():
    print("Game over")
    time.sleep(2)
    print("Would you like to play again?")
    answer=input("Type yes or no: \n")
    while "yes" in answer.lower():
        start_game()
    while "no" in answer.lower():
        sys.exit()
​
def bed():
    print("You are awake")
    time.sleep(0.1)
    print("Would you like to get out of bed?")
    time.sleep(0.1)
    answer=input("Type yes or no: \n")
    while "yes" in answer.lower():
        drink()
    while "no" in answer.lower():
        spider()
    else:
        bed()
​
def drink():
    global morale
    # print(f"Your morale is {morale}")
    print("You let out a large yawn...")
    time.sleep(0.1)
    print("stretch out your arms...")
    time.sleep(0.1)
    print("...and immediately knock over the glass of\033[2;33;40m Orange Juice\033[0;0m that was sitting on your bedside table...")
    time.sleep(0.1)
    print("Would you like to clean it up?")
    answer=input("Type yes or no? \n")
    while "yes" in answer.lower():
        print("What would you like to use to clean it up?")
        time.sleep(0.1)
        print("Towel?")
        time.sleep(0.1)
        answer=input("Or dog? \n")
        if "towel" in answer.lower():
            print("You mop up the \033[2;33;40m Orange Juice\033[0;0m with a nearby towel, congratulations, your towel now smells of carpet and\033[2;33;40m Orange Juice\033[0;0m")
            morale-=5
            toast()
        elif "dog" in answer.lower():
            print ("You use your dog to mop up the\033[2;33;40m Orange Juice\033[0;0m \n")
            time.sleep(0.1)
            print ("The dog deems this use of his temporary existence acceptable..")
            time.sleep(0.1)
            print ("..and wags his tail...joyfully...")
            morale+=5
            toast()
    while "no" in answer.lower():
        ants()
​
def spider():
    global morale
    print("You decide that staying in bed might be the wiser decision, on this particular day..")
    time.sleep(0.1)
    print("You rub your feet together under you duvet...let out a long yawn..")
    time.sleep(0.1)
    print("...and let out a long yawn...")
    time.sleep(0.1)
    print("A spider, promptly falls into your open mouth..")
    time.sleep(0.1)
    print("Spit it out?")
    answer=input("Or swallow it? \n")
    while "spit" in answer.lower():
        print("You spit the spider out in disgust")
        time.sleep(0.1)
        print("It runs under your duvet, freaking you out, and forcing you to evacuate your bed in such a way that you stub your toe on your bedside table.. ")
        time.sleep(0.1)
        morale-=5
        toast() 
    while "swallow" in answer.lower():
        print("You swallow the spider")
        time.sleep(0.1)
        print("Mmmmmm...")
        time.sleep(0.1)
        print("Chewy...")
        time.sleep(0.1)
        print("Poisonous...")
        time.sleep(0.1)
        print("You died as a result of spider venom")
        game_over()
​
def ants():
    print("You leave the juice soaking into the carpet")
    time.sleep(0.1)
    print("A large colony of Ants appear")
    time.sleep(0.1)
    print("They devour the juice before swarming over you")
    time.sleep(0.1)
    print("You are eaten alive")
    time.sleep(0.1)
    game_over()
​
def toast():
    print("You decide to make some breakfast")
    time.sleep(0.1)
    print("You put some bread into the toaster and turn the kettle on")
    time.sleep(0.1)
    answer=int(input("What setting would you like to put the toaster on? Enter a number from 1-6 \n"))
    while answer in range (1,3):
        good_toast()
    while answer in range (4,6):
        smoke_alarm()
​
def good_toast():
    global morale
    print("Congratulations!")
    time.sleep(0.1)
    print("The toast appears to be edible")
    morale+=5
    time.sleep(0.1)
    print(f"Your morale level is now {morale}")
    tea()
​
def smoke_alarm():
    global morale
    # print(f"Your morale is {morale}")
    print("Oh dear..")
    time.sleep(0.1)
    print("The toast has become stuck in the toaster, burnt and set off the smoke alarm")
    time.sleep(0.1)
    print("Would you like to try and remove the toast with a fork?  \n")
    answer=input("Type yes or no: \n")
    while "yes" in answer.lower():
        fork()
    while "no" in answer.lower():
        print("You leave the toast in the toaster and it, inevitably, ends up on fire, and burns your house down with you in it")
        game_over()
​
def fork():
    print("You jam a fork into the toaster in an attempt to remove the burning toast..")
    time.sleep(0.1)
    print("You roll the dice...")
    time.sleep(0.1)
    answer=random.randint(1,6)
    if answer in range (1,3):
        print("You live")
        tea()
    else: 
        answer in range (4,6)
        print("That was a really bad idea, because now, you have been electrocuted to death")
        game_over()
​
def tea():
    print("You go to make some tea")
    time.sleep(0.1)
    print("but, you don't have any milk")
    time.sleep(0.1)
    answer=input("Would you like to drink tea without milk? \n")
    while "yes" in answer.lower():
        blacktea()
    while "no" in answer.lower():
        pavement()
​
def blacktea():
    global morale
    print("You decide to drink the tea without milk")
    time.sleep(0.1)
    print("It's not very nice")
    morale-=5
    print("You decide to go to the shop anyway")
    time.sleep(0.1)
    pavement()
​
def dice_roll():
    num=random.randint(1,6)
    if num in range (1,3):
        print("You have succeeded in persuading the man to never come between a person and their milk.. ")
        shop()
    else:
        num in range (4,6)
        print("You have succumbed to the mans furious thrashing")
        game_over()
​
def fight_flight():
    answer=input("FIGHT or FLIGHT? \n")
    while "fight" in answer.lower():
        print("Your attempts to subdue the individual result in a dungeons and dragons style diceroll to decide whether you were successful or not.. ")
        time.sleep(0.1)
        print("You roll a d6...")
        dice_roll()
    while "flight" in answer.lower():
        print("You made the very wise decision to simply circumvent this particular obstacle, and make haste towards your original objective")
        shop()
​
def pavement():
    print("As you walk along the pavement, towards the supermarket, you can see man approaching you in the distance..")
    time.sleep(0.1)
    print("He is 100m away")
    time.sleep(0.1)
    answer=input("In an attempt to avoid the man, would you like to move left or right? \n")
    while "left" in answer.lower():
        print("You move to the left.")
        time.sleep(0.1)
        print("The man moves to the right, he is now 50m away")
        print("In a further attempt to avoid the man, would you like to move back to your right? \n")
        answer=input("Yes or no? \n")
        while "yes" in answer.lower():
            print("You move back to the right")
            time.sleep(0.1)
            print("The man moves back to the left, he is now stood directly in your way, obstructing your path")
            time.sleep(0.1)
            print("Clearly, he's a rather obstinant individual who doesn't seem to want you to continue on your journey..")
            fight_flight()
        while "no" in answer.lower():
            print("You are resolute in your decision to continue moving forwards, hoping the oncoming individual will step aside and let you pass")
            time.sleep(0.1)
            print("He doesn't")
            time.sleep(0.1)
            fight_flight()
    while "right" in answer.lower():
        print("You move to the right.")
        time.sleep(0.1)
        print("The man moves to the left, he is now 50m away")
        print("In a further attempt to avoid the man, would you like to move back to your left? \n")
        answer=input("Yes or no? \n")
        while "yes" in answer.lower():
            print("You move back to the left")
            time.sleep(0.1)
            print("The man moves back to the right, he is now stood directly in your way, obstructing your path")
            time.sleep(0.1)
            print("Clearly, he's a rather obstinant individual who doesn't seem to want you to continue on your journey..")
            fight_flight()
        while "no" in answer.lower():
            print("You are resolute in your decision to continue moving forwards, hoping the oncoming individual will step aside and let you pass")
            time.sleep(0.1)
            print("He doesn't")
            time.sleep(0.1)
            fight_flight()
​
def shop():
    print("You enter shop, there doesn't seem to be a queue")
    time.sleep(0.1)
    print("You take some milk from the nearby fridge and head towards the checkout")
    time.sleep(0.1)
    print("A WILD KAREN HAS APPEARED!")
    time.sleep(0.1)
    print('Without hesistation or consideration, "Karen" interjects herself between you and the cashier')
    time.sleep(0.1)
    print("You realise she's trying to return an inflatable mattress she purchased several months ago..")
    time.sleep(0.1)
    print("and no...")
    time.sleep(0.1)
    print("she doesn't have a receipt..")
    time.sleep(0.1)
    print("...nor is the cashier convinced that they ever sold inflatable mattresses...")
    time.sleep(0.1)
    print('You politely interject yourself into the ensuing conversation and ask \Karen\'s if she wouldnt mind just letting you pay for your milk')
    time.sleep(0.1)
    print("You feel a sudden and, violent, rage begin to overwhelm you from within..")
    time.sleep(0.1)
    boss_fight()
​
def boss_fight():
    print("BOSS FIGHT")
    time.sleep(0.1)
    print("'Cue Music...'")
    start_game()
​
​
​
​
def start_game():
    basket = [
    "beans",
    "milk",
    "banna",
    "cheese"
    ]
    print("You look down at your beasket of items and choose one to throw at Karen")
    time.sleep(0.1)
    print("What item do you wnat to throw at Karen?")
    time.sleep(0.1)
    print("here is a list of the ietms you have in your basket")
    print(basket)
    answer=input("pick an item number to throw \n")
    if "beans" in answer.lower():
        print("you throw the tin of beeans at her") 
        remove_karen_helath()
    elif "milk" in answer.lower():
        print("you throw the milk at her") 
        remove_karen_helath()
    elif "banna" in answer.lower():
        print("you throw the banna at her") 
        remove_karen_helath()
    elif "cheese" in answer.lower():
        print("you throw the banna at her") 
        remove_karen_helath()
    
​
​
def stat_health():
    global health
    if health >0:
        return True
    else:
        game_over()
​
​
​
def karen_health_chack():
    global karenhelath
    if karenhelath >0:
        return True
            
    else:
        you_win()
​
​
​
def you_win():
    print("You have wone the game well done")
    time.sleep(2)
    print("Would you like to play again?")
    answer=input("Type yes or no: \n")
    while "yes" in answer.lower():
        start_game()
    while "no" in answer.lower():
        sys.exit()
    
​
​
def remove_karen_helath():
    global karenhelath
    print("your item hits karen and she falls to the floor in pain")
    karenhelath-=5
    karen_health_chack()
    karen_throw()
​
​
def remove_helath():
    global health
    print("karans itesm hits you")
    health-=10
    stat_health()
​
​
def karen_throw():
    print("karne picks up an ietm and throws it at you")
    remove_helath()
​
​
​
start_game()