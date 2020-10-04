import pygame
import random
import math

from pygame import mixer

pygame.init()

#Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

#Background
background = pygame.image.load('background.png')

#Player
playerImg = pygame.image.load('space-invaders.png')
playerX= 370
playerY = 480
player_change=0

#Enemy
enemyImg = []
enemyX  = []
enemyY = []
enemy_vel=3
enemy_change_X =[]
enemy_change_Y = []
n_enemies = 6

for i in range(n_enemies):
	enemyImg.append(pygame.image.load('alien.png'))
	enemyX.append(random.randint(0,735))
	enemyY.append(50)
	enemy_change_X.append(enemy_vel)
	enemy_change_Y.append(40)

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX= 0
bulletY = 480
bullet_change_X=0
bullet_change_Y = 20
bullet_state="ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX=10
textY=10

#GameOver
go_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over_text():
	g_over = go_font.render("GAME OVER", True, (255, 255, 255))
	screen.blit(g_over, (200,250))

def show_score(x,y):
	score = font.render("Score: " + str(score_value), True, (255, 255, 255))
	screen.blit(score, (x,y))

def player(x, y):
	screen.blit(playerImg, (x,y))

def enemy(x, y, i):
	screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state ="fire"
	screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt(((enemyX-bulletX)**2 )+ ((enemyY-bulletY)**2))
	if distance <=27:
		return True
	else:
		return False

#Game loop
running = True

while running:
	screen.fill((0,0,0))
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_change = -4
			if event.key == pygame.K_RIGHT:
				player_change = 4
			if event.key == pygame.K_SPACE:
				if bullet_state == "ready":
					bullet_sound = mixer.Sound("laser.wav")
					bullet_sound.play()
					bulletX = playerX
					fire_bullet(playerX, bulletY)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
				player_change=0
	#Boundaries for player			
	playerX+=player_change
	if playerX<=0:
		playerX=0
	elif playerX >=736:
		playerX=736

	#Enemy movement
	for i in range(n_enemies):
		if enemyY[i]>440:
			for j in range(n_enemies):
				enemyY[j]=2000
			game_over_text()
			break
		enemyX[i]+=enemy_change_X[i]
		if enemyX[i]<=0:
			enemy_change_X[i]=enemy_vel
			enemyY[i]+=enemy_change_Y[i]
		elif enemyX[i] >=736:
			enemy_change_X[i]=-enemy_vel
			enemyY[i]+=enemy_change_Y[i]
		#Collision
		collision= isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision:
			explosion = mixer.Sound("explosion.wav")
			explosion.play()
			bulletY=480
			bullet_state="ready"
			score_value+=2
			enemy_vel += 0.1
			enemyX[i]= random.randint(0,735)
			enemyY[i] = 50		
		enemy(enemyX[i], enemyY[i], i)

	#Bullet movement 
	if bulletY <=0:
		bulletY = 480
		bullet_state="ready"
	if bullet_state == "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bullet_change_Y

	
	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update()