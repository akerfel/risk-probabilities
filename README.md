# risk-probabilities

Calculate probabilities for winning battles in the board game Risk. Made with Python.

This program determines the probability of victory for an attacker, given the number of troops on both sides. The attacker has a certain number of troops in a given region and is attempting to take over an enemy region with a specific number of defenders. The attacker is considered victorious if they are able to eliminate all of the defenders, while the defender wins if the number of attacking troops is reduced to just one (at which point the attack is no longer allowed to continue).

## Table

The following table was produced by this program (it has been visually enhanced using Google Sheets).

![chrome_idK8u9GTWH](https://user-images.githubusercontent.com/45148959/205713119-838f5062-4c24-4e08-b244-4a85a97bd2e6.png)

### Some general observations
- If the attacker has the same number of troops as the defender, the chance to win is ~15%.
- If the attacker has ~70% more troops than the defender, the chance of winning is ~50%.
- If the attacker has twice as many troops as the defender, the chance of winning is ~60%.
- If the attacker has four times as many troops as the defender, the chance of winning is ~90%.
