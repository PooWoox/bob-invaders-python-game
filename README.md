# bob-invaders-python-game
 A space invaders like game created with pygame on python.

There isn't much complexity on how the game works, for now there is a limited amount of enemies (6) that spawns on random places at the top of the screen and Bob, the ship, is on the bottom side. Enemies move from left to right and go down a few pixels when hitting sides. Bob can move from left to right and shoot one laser beam at a time. When an enemy is hit by the laser they "explode" and respawn again at the top of the screen, you get +1 score for that. If you are unable to shoot enemies and keep them distant from Bob, once they pass a certain line of proximity (very close to Bob), you lose. The code is based on functions inside a while loop that keeps it active until you lose.

Some of the concepts for the changes I put bellow are still vague on my mind so please don't hesitate to share your ideas with me. Also always open for suggestions on how to improve the already existend code, here to learn.

Planned improvements/changes for the game

- Background image will be replaced by a drawing;
- Golden enemies designed as a drawing;
- Sound effects will be replaced by my own voice recordings;
- Will add background music;
- Enemy speed increase on each kill so the game gets harder;
- Potential increase in number of enemies on a certain score;
- A buff that you can pick with Bob;
- Right now you're only able to shoot a new laser beam when the previous one is already out of the screen. Will try to make it possible to shoot more.
