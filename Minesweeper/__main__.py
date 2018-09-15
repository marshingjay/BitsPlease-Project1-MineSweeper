import pygame
from enum import Enum
from Minesweeper.Minesweeper import Minesweeper
from Minesweeper.Minefield import Minefield
from Minesweeper.Graphics.StartScreen import StartScreen
from Minesweeper.Graphics.EndScreen import EndScreen

def main():	
	State = Enum('State','Start Minesweeper End Exit')
	currentState = State.Start
	startScreen = None
	minesweeper = None
	endScreen = None
	while currentState != State.Exit:
		if (currentState == State.Start):
			if startScreen is None:
				startScreen = StartScreen()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					currentState = State.Exit
			startScreen.render()
			startScreen.clock.tick(60)
			if startScreen.gameReady:
				currentState = State.Minesweeper
				minesweeper = Minesweeper(startScreen.x_size, startScreen.y_size, startScreen.numMines)
				startScreen = None

		elif currentState == State.Minesweeper:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					currentState = State.Exit
				elif event.type == pygame.MOUSEBUTTONDOWN:
					(end, win) = minesweeper.onClick(event)
					if end:
						if win == 'RESET':
							currentState = State.Start
						else:
							currentState = State.End
							if win:
								minesweeper.updateFlags()
							else:
								minesweeper.onLose()
							minesweeper.render()
							endScreen = EndScreen(win)

			minesweeper.updateFlags()
			minesweeper.render()
			minesweeper.window.clock.tick(60)

		elif currentState == State.End:
			endScreen.render()
			minesweeper.window.clock.tick(60)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					currentState = State.Exit
				elif event.type == pygame.MOUSEBUTTONDOWN:
					currentState = State.Start
					endScreen = None
			

main()