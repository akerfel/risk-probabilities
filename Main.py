import random

# att = attackers
# def = defenders

num_simulations = 1000000
att_wins = 0
def_wins = 0
for i in range (num_simulations):
    num_att = 2
    num_def = 1
    while(num_att > 1 and num_def > 0):

        # Determine number of dice for attacker
        att_dices = num_att - 1
        if att_dices > 3:
            att_dices = 3
        
        # Determine number of dice for defender
        def_dices = num_def
        if def_dices > 3:
            def_dices = 3

        # Roll dice
        att_rolls = [random.randint(1,6) for i in range(att_dices)]
        def_rolls = [random.randint(1,6) for i in range(def_dices)]

        # Reduce number of troops depending on dice rolls
        while (len(att_rolls) > 0 and len(def_rolls) > 0):
            att_best_dice = att_rolls.pop(att_rolls.index(max(att_rolls)))
            def_best_dice = def_rolls.pop(def_rolls.index(max(def_rolls)))
            if att_best_dice > def_best_dice:
                num_def -= 1
            else:
                num_att -= 1
        
    if num_def == 0:
        att_wins += 1
    else:
        def_wins += 1

print("Attacker wins:", att_wins)
print("Defender wins:", def_wins)
chance_att_win = att_wins / num_simulations
print("Chance attacker wins:", chance_att_win)


"""
    for initial_num_att in range (2, 21):
        for initial_num_def in range (1, 21):


    if num_def == 0:
        print("Attacker wins!")
    else:
        print("Defender wins!")
            """