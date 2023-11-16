import pygame
import sys
import random
import os

pygame.init()

WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

screen_width = 1060
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dracomania")
font = pygame.font.Font(None, 36)

diretorio_imagens = 'assents/cards/'
imagens_locais = [f for f in os.listdir(diretorio_imagens) if f.endswith(('.jpg', '.png', '.jpeg'))]

class Card:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (200, 250))

vida_jogador1 = 10
vida_jogador2 = 10
slots_jogador1 = [None, None, None, None, None]  # Slots para o jogador 1
slots_jogador2 = [None, None, None, None, None]  # Slots para o jogador 2

for i in range(5):
    imagem_escolhida = random.choice(imagens_locais)
    caminho_imagem = os.path.join(diretorio_imagens, imagem_escolhida)
    slots_jogador2[i] = Card(caminho_imagem)
    
for i in range(5):
    imagem_escolhida = random.choice(imagens_locais)
    caminho_imagem = os.path.join(diretorio_imagens, imagem_escolhida)
    slots_jogador1[i] = Card(caminho_imagem)
    
def draw_screen():
  screen.fill(WHITE)
  
  vida_jogador1_text = font.render(f"Jogador 1: {vida_jogador1} Vida", True, BLACK)
  vida_jogador2_text = font.render(f"Jogador 2: {vida_jogador2} Vida", True, BLACK)
  screen.blit(vida_jogador1_text, (20, 20))
  screen.blit(vida_jogador2_text, (20, screen_height - 30))

  for i in range(5):
    pygame.draw.rect(screen, BLACK, (10 + i * 210, 80, 200, 250), 2)
    if slots_jogador1[i] is not None:
      screen.blit(slots_jogador1[i].image, (10 + i * 210, 80))

  for i in range(5):
        pygame.draw.rect(screen, BLACK, (10 + i * 210, 80 + 120 + 120 + 60, 200, 250), 2)
        if slots_jogador2[i] is not None:
            screen.blit(slots_jogador2[i].image, (10 + i * 210, 80 + 120 + 90 + 90))
            
  pygame.display.flip()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_screen()
    pygame.display.flip()
    pygame.time.Clock().tick(30)
  
