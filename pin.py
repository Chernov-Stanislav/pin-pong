from pygame import* 



win_width = 800
win_height = 500



window = display.set_mode((win_width,win_height))
fon = transform.scale(image.load("fon1.jpg"),(win_width,win_height))


FPS = 90
clock = time.Clock()

game = True
finish = False 

x1 = -40
y1 =250
x2 =748
y2 = 250



# keys_pressed = key.get_pressed()
#     if keys_pressed[K_w]:
#         y1 += 10 

#     if keys_pressed[K_s]:
#         y1 -= 10

#        if keys_pressed[K_UP]:
#         y2 += 10 

#     if keys_pressed[K_DOWN]:
#         y2 -= 10



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y, player_speed):
        super().__init__()
        self.image= transform.scale(image.load(player_image),(100,100))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x= player_x
        self.rect.y= player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class roketka(GameSprite):
	def update(self):
		
		keys = key.get_pressed()
		if keys[K_s] and self.rect.y >= 5:
			self.rect.y += self.speed
		elif keys[K_w] and self.rect.y <= win_height-80:
			self.rect.y -= self.speed
    def update2(self):
		
		keys = key.get_pressed()
		if keys[K_DOWN] and self.rect.y >= 5:
			self.rect.y += self.speed
		elif keys[K_UP] and self.rect.y <= win_height-80:
			self.rect.y -= self.speed

		




rok1 = roketka("rok1.png", x1, y1, 5)
rok2 = roketka("rok2.png", x2, y2, 5)

while game:
    for e in  event.get():
        if e.type ==QUIT:
            game = False

    if finish != True:
        window.blit(fon,(0,0))
        rok1.reset()
        rok1.update()
        rok2.reset()
        rok2.update()




    clock.tick(FPS)
    display.update()