import random

# The attacker wins if all defenders are eliminated.
# The defender wins if the number of attackers reaches 1.

simulations_per_scenario = 1000

max_num_attackers = 20
max_num_defenders = 20

# Print column headers
print("-\t", end="")
for i in range (2, max_num_attackers + 1):
    print("{}".format(i), end = "\t")
print("")

for initial_num_def in range (1, max_num_attackers + 1):
    print("{}".format(initial_num_def), end = "\t")
    for initial_num_att in range (2, max_num_defenders + 1):
        att_wins = 0
        def_wins = 0
        for i in range (simulations_per_scenario):
            num_att = initial_num_att
            num_def = initial_num_def

            # Kill troops until someone wins
            while(num_att > 1 and num_def > 0):
                # Determine number of dice
                att_dice = min(num_att - 1, 3)
                def_dice = min(num_def, 3)

                # Roll dice
                att_rolls = [random.randint(1,6) for i in range(att_dice)]
                def_rolls = [random.randint(1,6) for i in range(def_dice)]

                # Kill troops
                while (len(att_rolls) > 0 and len(def_rolls) > 0):
                    att_best_dice = att_rolls.pop(att_rolls.index(max(att_rolls)))
                    def_best_dice = def_rolls.pop(def_rolls.index(max(def_rolls)))
                    if att_best_dice > def_best_dice:
                        num_def -= 1
                    else:
                        num_att -= 1
            
            # Check who won
            if num_def == 0:
                att_wins += 1
            else:
                def_wins += 1
        
        # Print chance of winning
        chance_att_win = att_wins / simulations_per_scenario
        chance_att_win_prcnt = int(chance_att_win * 100)
        print("{}%".format(chance_att_win_prcnt), end = "\t")
    print("")