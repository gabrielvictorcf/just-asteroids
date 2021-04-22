# <p align="center"> <img src="https://i.imgur.com/xW65plv.png"> </p>

<img src="https://i.imgur.com/wjBAdaV.png" alt="img" align="right" width="400px">

Just asteroids is a clone of 'Atari Asteroids' rendered and played
entirely on the terminal. It was made out of curiosity on how a
computer draws lines or objects to the screen, and how those are
interactible.

With that in mind, what better way to learn that besides
making a small game!

Also, check out [Javidx9's](https://www.youtube.com/channel/UC-yuWVUplUJZvieEligKBkA) channel! My implementation
is inspired on his video on [asteroids](https://link).

## Installing
just-asteroids uses python's `keyboard` module, so although a regular
install will suffice on windows, linux needs a root install (sorry!)

### Pip install
	pip install git+https://github.com/gabrielvictorcf/just-asteroids#egg=just-asteroids

### Manual/Git install
	git clone https://github.com/gabrielvictorcf/just-asteroids
	cd just-asteroids
	pip3 install . # sudo pip3 install . if on Linux

## How to play
As of now, just-asteroids requires manual resizing of the terminal
window: 305 columns x 105 rows is enough. Also change font size to 6
and you're good to go!

## Controls
```
left-arrow: left rotate
right-arrow: right rotate
up: thrust
space: shoot
b: brake
```