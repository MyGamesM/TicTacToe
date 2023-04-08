import os, pygame

os.system("cls")

pygame.init()
pygame.display.set_caption("TicTacToe")

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running: bool = True
turn: bool = True
finished: bool = False
winner: bool = False
board: list[list[int]] = [[0 for _ in range(3)] for _ in range(3)]
GRAY: tuple[int, int, int] = (200, 200, 200)

def draw_board() -> None:
	a = 37
	for i in range(4):
		pygame.draw.line(screen, GRAY, (a + (175 * i), 25), (a + (175 * i), 575), 2)
		pygame.draw.line(screen, GRAY, (25, a + (175 * i)), (575, a + (175 * i)), 2)

	for i in range(len(board)):
		for j in range(len(board[i])):
			match board[j][i]:
				case 1:
					draw_x(i, j)
				case 2:
					draw_o(i, j)

def draw_x(x: int, y: int) -> None:
	x, y = x + 1, y + 1
	x = 48 + (x - 1) * 175
	y = 48 + (y - 1) * 175
	a = 150
	pygame.draw.line(screen, GRAY, (x, y), (x + a, y + a), 2)
	pygame.draw.line(screen, GRAY, (x + a, y), (x, y + a), 2)

def draw_o(x: int, y: int) -> None:
	x, y = x + 1, y + 1
	x, y = x + 123 + ((x - 1) * 175), y + 123 + ((y - 1) * 175)
	pygame.draw.circle(screen, GRAY, (x, y), 75, 2)

def draw_end_screen() -> None:
	x, y = 600, 600
	font = pygame.font.Font("font.ttf", 64)
	text = font.render(f"{'o' if winner else 'x'} won", True, GRAY)
	text_rect = text.get_rect()
	text_rect.center = (x // 2, y // 2)
	screen.blit(text, text_rect)

while running:
	screen.fill("black")

	if finished:
		draw_end_screen()
	else:
		for i in range(3):
			if board[i][0] != 0 and board[i][1] != 0 and board[i][2] != 0 and board[i][0] == board[i][1] == board[i][2]:
				finished = True
				winner = board[i][0] % 2 == 0

			if board[0][i] != 0 and board[1][i] != 0 and board[2][i] != 0 and board[0][i] == board[1][i] == board[2][i]:
				finished = True
				winner = board[0][i] % 2 == 0

		if board[0][0] != 0 and board[1][1] != 0 and board[2][2] != 0 and board[0][0] == board[1][1] == board[2][2]:
			finished = True
			winner = board[0][0] % 2 == 0

		if board[0][2] != 0 and board[1][1] != 0 and board[2][0] != 0 and board[0][2] == board[1][1] == board[2][0]:
			finished = True
			winner = board[0][0] % 2 == 0

		draw_board()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				x, y = pygame.mouse.get_pos()
				x, y = int((x - 40) / 170), int((y - 40) / 170)
				if x < 3 and y < 3 and board[y][x] == 0:
					if turn:
						board[y][x] = 1
						turn = False
					else:
						board[y][x] = 2
						turn = True

	pygame.display.flip()

	clock.tick(60)

pygame.quit()