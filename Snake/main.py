import pygame
import random

global game_over, game_score
game_over=False
game_score = 0
class Cube:
	def __init__(self,posX, posY,dirX, dirY, color=(255,0,0)):
		self.color = color
		self.posX = posX
		self.posY = posY
		self.dirX = dirX
		self.dirY = dirY
	def draw(self, surface,x, y, size):
		pygame.draw.rect(surface, self.color, (x, y ,size,size))
	def move(self, dirX, dirY):
		self.dirX = dirX
		self.dirY = dirY
		x_move = 2 * dirX
		y_move = 2 * dirY
		self.posX+=x_move
		self.posY +=y_move

class Snake:
	
	def __init__(self, posX, posY,dirX=-1, dirY=0):
		self.head = Cube(posX, posY, dirX, dirY)
		self.posX =posX
		self.posY = posY
		self.dirX = dirX
		self.dirY = dirY
		self.body = [self.head]
		self.turns = {}
	def draw_snake(self, surface, size =20):
		for i in range(len(self.body)):
			self.body[i].draw(surface,self.body[i].posX, self.body[i].posY,size)
	def append_cube(self):
		initial_dir_x= self.body[-1].dirX
		initial_dir_y = self.body[-1].dirY
		initial_pos_x = self.body[-1].posX + (20*-initial_dir_x)
		initial_pos_y = self.body[-1].posY +(20*-initial_dir_y)
		self.body.append(Cube(initial_pos_x, initial_pos_y, initial_dir_x, initial_dir_y))
	def move(self):
		global game_over, game_score
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()	
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if self.head.dirX != -1 and self.head.dirY != 0:
						self.turns[(self.head.posX, self.head.posY)]= (-1,0)
				if event.key == pygame.K_RIGHT:
					if self.head.dirX != 1 and self.head.dirY != 0:
						self.turns[(self.head.posX, self.head.posY)]= (1,0)
				if event.key == pygame.K_UP:
					if self.head.dirX != 0 and self.head.dirY != -1:
						self.turns[(self.head.posX, self.head.posY)]= (0,-1)
				if event.key == pygame.K_DOWN:
					if self.head.dirX !=0 and self.head.dirY != 1:
						self.turns[(self.head.posX, self.head.posY)]= (0,1)

		for i in range(len(self.body)):
			if i != 0 and ((self.head.posX <= self.body[i].posX +10  and self.head.posX>=self.body[i].posX-10) and (self.head.posY <= self.body[i].posY +10  and self.head.posY>=self.body[i].posY-10)):
				game_over = True
				game_score = len(self.body)
				self.body=[]
				break
			pos = (self.body[i].posX, self.body[i].posY)
			if pos in self.turns:
				self.body[i].move(self.turns[pos][0],self.turns[pos][1] )
				if i == len(self.body)-1:
					self.turns.pop(pos)
			else:
				if self.body[i].posX >500:
					self.body[i].posX=0
				elif self.body[i].posX<0:
					self.body[i].posX = 500
				elif self.body[i].posY >500:
					self.body[i].posY = 0
				elif self.body[i].posY < 0:
					self.body[i].posY=500
				else:
					self.body[i].move(self.body[i].dirX, self.body[i].dirY)
			
		
def update_screen(surface, w, s):
	global game_over, game_score
	surface.fill((0,0,0))
	if game_over:
		game_over_text(surface)
		show_score(surface, game_score)
		pygame.display.update()
	else:
		s.draw_snake(surface)	
		add_random_snack(surface,snack_pos_x, snack_pos_y)	
		pygame.display.update()

def add_random_snack(surface, x,y):
	pygame.draw.rect(screen, (0,255,0), (x, y, 20, 20))

def game_over_text(surface):
	font = pygame.font.Font('freesansbold.ttf', 40)
	g_over = font.render("GAME OVER", True, (255, 255, 255))
	surface.blit(g_over, (125,200))
def show_score(surface,final_score):
	font = pygame.font.Font('freesansbold.ttf', 35)
	score = font.render(f"Score : {final_score}",True, (255, 255, 255))
	surface.blit(score, (175,250))

pygame.init()
width =500
screen = pygame.display.set_mode((width,width))
pygame.display.set_caption("Snake")
s=Snake(100,100)
snack_pos_x=random.randint(0,470)
snack_pos_y=random.randint(0,470)
clock = pygame.time.Clock()
count =0 
playing = True

while playing:
	pygame.time.delay(10)
	clock.tick(110)
	s.move()
	if (s.head.posX <= snack_pos_x + 20 and s.head.posX >= snack_pos_x - 20) and (s.head.posY <= snack_pos_y + 20 and s.head.posY >= snack_pos_y-20):
		snack_pos_x = random.randint(0,470)
		snack_pos_y = random.randint(0,470)
		s.append_cube()  


	update_screen(screen, width,s)	
	


	

