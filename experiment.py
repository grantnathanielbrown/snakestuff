import random

# GLOBAL VARIABLES
user_hitpoints = 100
bear_hitpoints = 100
user_status = 'Healthy'

# FUNCTIONS / STAGES OF THE GAME
def initial_prompt():
    answer = input("""You arrive inside of the dungeon. Do you wish to:
1. Go down the spiral staircase.
2. Yell 'Hello?'.
3. Sift through your pockets.
""")
    if answer == '1':
        print('You fall, you fool. Suddenly, a bear appears!')
    elif answer == '2':
        print('No one is here, you fool. Suddenly, a bear appears!')
    elif answer == '3':
        print('You have no money, you fool. Suddenly, a bear appears!')
    else:
        print('Are you literate, you fool? Try selecting an option again.')
        initial_prompt()

def bear_attack():
    global user_hitpoints
    global user_status
    attack_result = random.randint(1,7)
    if attack_result == 1:
        swipe_result = random.randint(20,30)
        user_hitpoints -= swipe_result
        print(f'The bear swipes you with his claw! You just took {swipe_result} points of damage!')
        print(user_hitpoints)
    elif attack_result == 2:
        swipe_result = random.randint(20,30)
        user_hitpoints -= swipe_result
        user_status = "Bleeding"
        print(f'The bear stabbed you with a knife for some reason!!!(?) You just took {swipe_result} points of damage, and now you\'re bleeding!')
        print(user_hitpoints)
    else:
        print('The bear tries to swipe you with his claw, but he misses. This bear is really slow, so he will miss a lot. He is trying his best.')

def bear_fight():
    global user_hitpoints
    global user_status
    if user_hitpoints <= 0:
        print('Placeholder')
    if user_status == 'Bleeding':
        user_hitpoints -= 5
        print(f"You're bleeding, so now you only have {user_hitpoints} hitpoints. If only there was some way to stop the bleeding...")

    action_choice = input("""You are being attacked by a bear! Do you wish to:
1. Punch the bear!
2. Bandage yourself quickly!
3. Run away (there is only a 20 percent chance that this works!)
""")
    print()
    if action_choice == '1':
        global bear_hitpoints
        bear_hitpoints -= 10
        if bear_hitpoints <= 0:
            print('You finally beat the bear! He ran away, crying. You monster. How could you do that to the poor, innocent bear?')
        else:
            bear_attack()
            bear_fight()
    elif action_choice == '2':
        if user_status == 'Healthy':
            print('Why are you putting bandages on? The bear calls you an idiot.')
        else:
            user_status = 'Healthy'
            print('You stopped the bleeding. Nice job!')
        bear_attack()
        bear_fight()
    elif action_choice == '3':
        run_attempt = random.randint(1,5)
        if run_attempt == 1:
            print('You ran away from the bear! You are crying. You suck.')
        else:
            print('You tried to run away, but you failed, because the bear is using the Kage Bunshin no Jutsu! How the hell is he doing that?.')
            bear_attack()
            bear_fight()
    else:
        print('Are you literate, you fool? Try selecting an option again.')
        bear_fight()

# THE ACTUAL ADVENTURE
character_name = input('What is your name, adventurer? ')
print('Greetings, ' + character_name)
print()
initial_prompt()
print()
bear_fight()
print()
print('Now, you are just standing there lol')