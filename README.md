# bedwars-game-theory
some analysis on this quirky game called bedwars
## What do we want to do?
Determine the optimal economic strategies to win games in hypixel.net bedwars
## Plan of action
- genetic algorithm of strategies to see which ones lead to winning strategies
  - teams try different strategies and compete, winners move on
  - what parameters need to be controlled? do we manually decide them
    - some PvP ability which is influenced by the gear you have
    - bed defence / bed breaking ability
    - choice to go attack, stay and defend, time to attack
    - build speed
  - give teams iron/gold and let them do what they want, simulate entire games
  - each team is a neural network with different
- model map as a grid of islands and gaps, 7x7, teams can build and cross bridges
- Decisions possible:
  1. Buy
  2. Get emerald
  3. Get Diamond
  4. Move to block
  5. Fight
  6. Run
  7. Defend
  8. Bed Break

- ![[Pasted image 20230617121845.png]]

CALL initialize map

CALL game master

FUNCTION initialize map

  SET map array = [7 x 7]

  SET agent positions = [7 x 7 x 8]

RETURN map array, agent positions

FUNCTION engagement

FUNCTION game master
  
  GET agent positions

  WHEN agent positiony = positiony

  CALL engagement

  