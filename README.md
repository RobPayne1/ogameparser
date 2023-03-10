# ogameparser
This repository is for utilizing the ogame API.

## ✨ Features

- [x] Database Authentication
- [x] Players High-Level Information
- [x] Alliances High-Level Information
- [x] Player Total, Economy, Research, Military, Military Lost, Military Built, Military Destroyed, and Honor Points
- [x] Player Planets
- [x] Alliance Total, Economy, Research, Military, Military Lost, Military Built, Military Destroyed, and Honor Points
- [x] Number of Members Per Alliance
- [ ] UI to review data (Flutter project)

# Useful API Info
Information on [Players](https://s181-us.ogame.gameforge.com/api/players.xml) - Update interval 1 day

Information on [High Scores](https://s181-us.ogame.gameforge.com/api/highscore.xml?category=1&type=1) - Update interval 1 hour

___You can change the category and type for these by changing the values in the URL___
___Note: The Type values goes through 11, so the others 8-11 must be the lifeform stuff___
	
Category | Result
-- | --
1 | Player
2 | Alliance

Type | Result
-- | --
0 | Total
1 | Economy
2 |	Research
3 |	Military
4 |	Military Lost
5 |	Military Built
6 |	Military Destroyed
7 |	Honor 

Information on [Individual Players](https://s181-us.ogame.gameforge.com/api/playerData.xml?id=100262) - Update interval 1 week
	
___You can change the id in the URL to the Player ID from s181-us.ogame.gameforge.com/api/players.xml that you want to search for___

Information on [Alliances](https://s181-us.ogame.gameforge.com/api/alliances.xml) - Update interval 1 day

# Other API Links That Are Probably Useless
(https://s181-us.ogame.gameforge.com/api/localization.xml) - Static

(https://s181-us.ogame.gameforge.com/api/universes.xml) - Static

(https://s181-us.ogame.gameforge.com/api/universe.xml) - Updateinterval 1 week (has admin stuff)

(https://s181-us.ogame.gameforge.com/api/serverData.xml) - Static
 
# Setup
1. Install the requirements using pip with the following command:
```bash
pip install -r requirements.txt
```
2. Run the script
```bash
python3 main.py
```
