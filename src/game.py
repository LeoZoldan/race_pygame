import pygame
import random
import src.config as config
from src.car import Car
from src.functions import writeData, getData
import src.input_voice as iv


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode(config.game_resolution) 
pygame.display.set_caption("Jogo de Carro")


# icons
icon  = pygame.image.load("recursos/icon.png")
pygame.display.set_icon(icon)

## cars
red_car = Car("recursos/red_car.png", config.game_resolution)
purple_car = Car("recursos/purple_car.png", config.game_resolution)
yellow_car = Car("recursos/yellow_car.png", config.game_resolution)
blue_car = Car("recursos/blue_car.png", config.game_resolution)
enemy_cars = (purple_car, yellow_car, blue_car)


# backgrounds
home_background = pygame.transform.smoothscale(pygame.image.load("recursos/home_background.png"), config.game_resolution)
endgame_background = pygame.transform.smoothscale(pygame.image.load("recursos/car_crashed.png"), config.game_resolution)

road_background_1 = pygame.image.load("recursos/road_big.png")
road_background_2 = pygame.transform.rotate(pygame.image.load("recursos/road_big.png"), 180)


## sounds
pygame.mixer.music.load("recursos/nfs_theme.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.fadeout(3000)
pygame.mixer.music.play(-1, fade_ms=2000)

race_car_passing = pygame.mixer.Sound("recursos/race_car_passing.mp3")
race_car_passing.set_volume(0.05)

crashSound = pygame.mixer.Sound("recursos/crash.mp3")
crashSound.set_volume(0.2)


## fonts
font_small = pygame.font.SysFont("arial", 12)
font = pygame.font.SysFont("arial", 22)
font_big = pygame.font.SysFont("arial", 72)


## filters
filter = pygame.Surface(config.game_resolution, pygame.SRCALPHA)

filter_transparent = filter
filter_transparent.fill(config.black_transparent)

filter_transparent_2 = filter
filter_transparent.fill(config.black_transparent_2)

    

def start():
    menu(home_background)


def menu(background):    
    larguraButtonStart = 150
    alturaButtonStart  = 40
    larguraButtonQuit = 150
    alturaButtonQuit  = 40
    
    
    center_position_x_start = (config.game_resolution[0] - larguraButtonStart) / 2
    center_position_y_start = ((config.game_resolution[1] - alturaButtonStart) / 2) - 10


    center_position_x_quit = (config.game_resolution[0] - larguraButtonQuit) / 2
    center_position_y_quit = ((config.game_resolution[1] + alturaButtonQuit) / 2) + 10


    startTexto = font.render("Iniciar Game", True, config.black)
    start_text_width , start_text_height = startTexto.get_size()
    center_position_x_start_text = center_position_x_start + (larguraButtonStart - start_text_width) / 2
    center_position_y_start_text = center_position_y_start + (alturaButtonStart - start_text_height) / 2
    
    
    quitTexto = font.render("Sair do Game", True, config.black)
    quit_text_width , quit_text_height = quitTexto.get_size()
    center_position_x_quit_text = center_position_x_quit + (larguraButtonQuit - quit_text_width) / 2
    center_position_y_quit_text = center_position_y_quit + (alturaButtonQuit - quit_text_height) / 2


    
    while True:   
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35
                    
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 140
                    alturaButtonQuit  = 35

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 150
                    alturaButtonStart  = 40
                    welcome(colect_name())
                    
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 150
                    alturaButtonQuit  = 40
                    quit()
                    

        window.fill(config.white)
        window.blit(background, (0,0))
        window.blit(filter_transparent_2, (0, 0))

        startButton = pygame.draw.rect(window, config.white, (center_position_x_start, center_position_y_start, larguraButtonStart, alturaButtonStart), border_radius=15)
        window.blit(startTexto, (center_position_x_start_text, center_position_y_start_text))
        
        quitButton = pygame.draw.rect(window, config.white, (center_position_x_quit, center_position_y_quit, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        window.blit(quitTexto, (center_position_x_quit_text, center_position_y_quit_text))
        
        pygame.display.flip()
        clock.tick(60)
        

def welcome(nick_name):   
    text_spacing = 50
    
    box_center_x = config.game_resolution[0] / 2
    
    welcomeTxt = font.render(f"Seja bem vindo {nick_name}!!", True, config.white)
    welcomeTxt_width , welcomeTxt_height = welcomeTxt.get_size()
    welcomeTxt_center_x= box_center_x - (welcomeTxt_width / 2)
    welcomeTxt_center_y = (text_spacing * 4)
    
    loreTxt = font.render("Seu objetio é ultrapassar carros e evitar colisões, toda vez que fizer isso será adicinado um ponto ao placar.", True, config.white)
    loreTxt_width , loreTxt_height = loreTxt.get_size()
    loreTxt_center_x= box_center_x - (loreTxt_width / 2)
    loreTxt_center_y = welcomeTxt_center_y + text_spacing
    
    gameplayTxt = font.render("Você utilizará as setas ↑ (cima) ↓ (baixo) ← (esquerda) → (direita) do seu telado para se movimentar.", True, config.white)
    gameplay_width , gameplay_height = gameplayTxt.get_size()
    gameplay_center_x= box_center_x - (gameplay_width / 2)
    gameplay_center_y = loreTxt_center_y + text_spacing
    
    
    startTxt = font.render("Iniciar", True, config.black)
    startTxt_width , startTxt_height = startTxt.get_size()
    startTxt_center_x= box_center_x - (startTxt_width / 2)
    startTxt_center_y = gameplay_center_y + (text_spacing * 3)
    
    start_box_width = startTxt_width + 100
    start_box_height = startTxt_height + 20
    start_box_center_x = box_center_x - (start_box_width / 2)
    start_box_center_y = startTxt_center_y - 10
    
    start_button = None
    first_loop = True
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                
            if start_button != None:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(evento.pos):
                        start_box_width -= 10
                        start_box_height -= 5

                    
                elif evento.type == pygame.MOUSEBUTTONUP:
                    if start_button.collidepoint(evento.pos):
                        start_box_width += 10
                        start_box_height += 5
                        play(nick_name)
        
        window.fill(config.white)
        window.blit(home_background, (0,0))        
        for i in range(1, 5):
            window.blit(filter_transparent, (0, 0))
            
        window.blit(welcomeTxt, (welcomeTxt_center_x, welcomeTxt_center_y))
        window.blit(loreTxt, (loreTxt_center_x, loreTxt_center_y))
        window.blit(gameplayTxt, (gameplay_center_x, gameplay_center_y))
        start_button = pygame.draw.rect(window, config.white, (start_box_center_x, start_box_center_y, start_box_width, start_box_height), border_radius=15)
        window.blit(startTxt, (startTxt_center_x, startTxt_center_y))
        
        pygame.display.flip()
        
        if(first_loop):
            iv.engine.say(f"Seja bem vindo {nick_name}!")
            iv.engine.runAndWait()
            first_loop = False
        
        clock.tick(60)


def colect_name():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()

    
    text_spacing = 50
    
    box_center_x = config.game_resolution[0] / 2
    
    get_nick_txt = font.render("Fale seu nickname em voz alta!", True, config.white)
    get_nick_txt_width , get_nick_txt_height = get_nick_txt.get_size()
    get_nick_txt_center_x= box_center_x - (get_nick_txt_width / 2)
    get_nick_txt_y = (text_spacing * 4)
    
    confirm_txt = font.render(f"Se seu nickname estiver correto diga sim.", True, config.white)
    confirm_txt_width , confirm_txt_height = confirm_txt.get_size()
    confirm_txt_center_x= box_center_x - (confirm_txt_width / 2)
    
    nick_name = None
    nick_correct = None
    setp = 0

    while True:
        window.fill(config.white)
        window.blit(home_background, (0,0))        
        for i in range(1, 5):
            window.blit(filter_transparent, (0, 0))
            
        window.blit(get_nick_txt, (get_nick_txt_center_x, get_nick_txt_y))
        
        if (nick_name != None):
            setp = 1
            nick_txt = font.render(f"Você disse: {nick_name}.", True, config.white)
            nick_txt_width , nick_txt_height = nick_txt.get_size()
            nick_txt_center_x= box_center_x - (nick_txt_width / 2)
            nick_txt_y = get_nick_txt_y + text_spacing
            window.blit(nick_txt, (nick_txt_center_x, nick_txt_y))
            confirm_txt_y = nick_txt_y + text_spacing
            window.blit(confirm_txt, (confirm_txt_center_x, confirm_txt_y))
            
            if (nick_correct != None):
                setp = 2
                nick_correct_txt = font.render(f"Você disse: {nick_correct}", True, config.white)
                nick_correct_txt_width , nick_correct_txt_height = nick_txt.get_size()
                nick_correct_txt_center_x= box_center_x - (nick_correct_txt_width / 2)
                nick_correct_txt_y = confirm_txt_y + text_spacing
                window.blit(nick_correct_txt, (nick_correct_txt_center_x, nick_correct_txt_y))
        
        
        pygame.display.flip()            
        
        if setp == 0:
            iv.engine.say("Fale seu nickname em voz alta!")
            iv.engine.runAndWait()
            nick_name = iv.recognize()
        elif setp == 1:
            iv.engine.say(f"Você disse: {nick_name}? Se seu nickname estiver correto diga sim")
            iv.engine.runAndWait()
            nick_correct = iv.recognize()
        elif setp == 2:
            nick_correct == "sim"
            return nick_name
            
        clock.tick(60)
    

def play(nick_name):
    move_x_red_car  = 0
    move_y_red_car  = 0
    enemy_car = enemy_cars[random.randint(0, len(enemy_cars) - 1)] 
    
    position = random.randint(0, len(config.enemy_positions_x) - 1)
    if position % 2 == 0:
        enemy_car.setRotation("down")
    else:
        enemy_car.setRotation("up")
    enemy_car.x = config.enemy_positions_x[position]
    
    enemy_car.y = -100
    enemy_car.velocity = 5
    enemy_car_velocity = enemy_car.velocity
    pontos = 0
    count_cars = 0
    dificuldade  = 30
    
    is_paused = False
    pause = False
    
    while True:
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_RIGHT or evento.key == pygame.K_d):
                move_x_red_car = 15
            elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_LEFT or evento.key == pygame.K_a):
                move_x_red_car = -15
            elif evento.type == pygame.KEYUP and (evento.key == pygame.K_RIGHT or evento.key == pygame.K_d):
                move_x_red_car = 0
            elif evento.type == pygame.KEYUP and (evento.key == pygame.K_LEFT or evento.key == pygame.K_a):
                move_x_red_car = 0
            elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_UP or evento.key == pygame.K_w):
                move_y_red_car = -15
            elif evento.type == pygame.KEYDOWN and (evento.key == pygame.K_DOWN or evento.key == pygame.K_s):
                move_y_red_car = 15
            elif evento.type == pygame.KEYUP and evento.key == (pygame.K_UP or evento.key == pygame.K_w):
                move_y_red_car = 0
            elif evento.type == pygame.KEYUP and evento.key == (pygame.K_DOWN or evento.key == pygame.K_s):
                move_y_red_car = 0
            elif evento.type == pygame.KEYDOWN and evento.key == (pygame.K_SPACE):
                if is_paused:
                    is_paused = False
                    pause = False
                else:
                    is_paused = True
                    pause = True
                
                                
               
        if is_paused:
            if pause:  
                window.blit(filter_transparent, (0, 0))

                texto_pause = font_big.render("PAUSE", True, config.white)
                texto_rect = texto_pause.get_rect(center=(config.game_resolution[0] // 2, config.game_resolution[1] // 2))
                window.blit(texto_pause, texto_rect)
                
                pause = False
        
        
        else:    
            red_car.x = red_car.x + move_x_red_car            
            red_car.y = red_car.y + move_y_red_car
            enemy_car.y = enemy_car.y + enemy_car.velocity            
            
            
            if red_car.x < config.road_limit_x[0]:
                red_car.x = config.road_limit_x[0]
            elif red_car.x > config.road_limit_x[1]:
                red_car.x = config.road_limit_x[1]
                
                
            if red_car.y < 0 :
                red_car.y = 10
            elif red_car.y > 473:
                red_car.y = 463
                    

            config.map_velocity += 0.007
            config.map_1_postion_y += config.map_velocity
            config.map_2_postion_y += config.map_velocity
            
            
            if(config.map_1_postion_y >= config.game_resolution[1]):
                config.map_1_postion_y = config.map_2_postion_y-1390
                        
            if(config.map_2_postion_y >= config.game_resolution[1]):
                config.map_2_postion_y = config.map_1_postion_y-1390
            
            
            if enemy_car.y > red_car.y and count_cars == pontos:
                pontos += 1
                pygame.mixer.Sound.play(race_car_passing)
                
            
            if enemy_car.y > config.game_resolution[1]:
                count_cars += 1              
                enemy_car = enemy_cars[random.randint(0, len(enemy_cars) - 1)] 
                
                position = random.randint(0, len(config.enemy_positions_x) - 1)
                if position % 2 == 0:
                    enemy_car.setRotation("down")
                else:
                    enemy_car.setRotation("up")
                enemy_car.x = config.enemy_positions_x[position]
    
                enemy_car.y = int(enemy_car.resolution[1] * -1)
                enemy_car_velocity = enemy_car_velocity + 1
                enemy_car.velocity = enemy_car_velocity
            
            
            text_points = font.render("Pontos: " + str(pontos), True, config.white)
            text_points_width = (text_points.get_size()[0]) + 60
            
            text_pause = font_small.render("Press Space to Pause Game", True, config.white)
            text_pause_width = (text_points.get_size()[0])
            
            label_width = text_points_width + text_pause_width + 52
            label_point = pygame.Surface((label_width, 35), pygame.SRCALPHA)
            pygame.draw.rect(label_point, config.black_transparent_2, (0, 0, label_width, 35))
        
            
            red_car.colisor_x = list(range(red_car.x, red_car.x + red_car.width))
            red_car.colisor_y = list(range(red_car.y, red_car.y + red_car.height))
            enemy_car.colisor_x = list(range(enemy_car.x, enemy_car.x + enemy_car.width))
            enemy_car.colisor_y = list(range(enemy_car.y, enemy_car.y + enemy_car.height))
            
            
            if  len( list( set(enemy_car.colisor_y).intersection(set(red_car.colisor_y))) ) > dificuldade:
                if len( list( set(enemy_car.colisor_x).intersection(set(red_car.colisor_x))   ) )  > dificuldade:
                    pygame.mixer.Sound.play(crashSound)
                    writeData(nick_name, pontos)
                    game_over()           

            
            window.fill(config.white)    
            window.blit(road_background_1, (config.map_1_postion_x, config.map_1_postion_y))
            window.blit(road_background_2, (config.map_2_postion_x, config.map_2_postion_y))        
            window.blit(red_car.sprite, (red_car.x, red_car.y))
            window.blit(enemy_car.sprite, (enemy_car.x, enemy_car.y) )
            window.blit(label_point, (5, 11))
            window.blit(text_points, (15,15))
            window.blit(text_pause, (text_points_width, 25))
        
        
        pygame.display.flip()
        clock.tick(60)
        

def ajust_str(s, max_len, space):
    if (len(str(s)) < max_len):
        return str(s).ljust(max_len + space)
    else:
        return str(s)[:max_len].ljust(max_len + space)

        
def game_over():
    placar_font = pygame.font.SysFont("Courier New", 20)
    
    window.fill(config.white)  
    window.blit(endgame_background, (0, 0))
    
    for i in range(1, 5):
        window.blit(filter_transparent, (0, 0))
    
    
    box_center_x = config.game_resolution[0] / 2
    text_spacing = 50
    
    
    table = placar_font.render(f"Pontos    Nickname       Data                     ", True, config.white)
    table_width , table_height = table.get_size()
    table_x= box_center_x - (table_width / 2)
    table_y = text_spacing * 3
    window.blit(table, (table_x, table_y))
    
    
    data = getData()
    for i in range(0, 5):
        if len(data) >= i + 1:
            points = ajust_str(data[i][1], 5, 5)
            nick = ajust_str(data[i][0], 10, 5)
            date = ajust_str(data[i][2], 20, 5)
            
            regTxt = placar_font.render(f"{points}{nick}{date}", True, config.white)
            regTxt_x= table_x
            regTxt_y = (text_spacing * (i+1)) + table_y
            window.blit(regTxt, (regTxt_x, regTxt_y))

        
        
    goto_to_menu_txt = font.render("Voltar ao menu", True, config.black)
    goto_to_menu_width , goto_to_menu_height = goto_to_menu_txt.get_size()
    goto_to_menu_x = box_center_x - (goto_to_menu_width / 2)
    goto_to_menu_y = regTxt_y + (text_spacing * 3)
    
    goto_to_menu_box_width = goto_to_menu_width + 100
    goto_to_menu_box_height = goto_to_menu_height + 20
    goto_to_menu_box_x = box_center_x - (goto_to_menu_box_width / 2)
    goto_to_menu_boxr_y = goto_to_menu_y - 10

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if goto_menu_button.collidepoint(evento.pos):
                    goto_to_menu_box_width -= 10
                    goto_to_menu_box_height -= 5

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                if goto_menu_button.collidepoint(evento.pos):
                    goto_to_menu_box_width += 10
                    goto_to_menu_box_height += 5
                    menu(home_background)
        
        goto_menu_button = pygame.draw.rect(window, config.white, (goto_to_menu_box_x, goto_to_menu_boxr_y, goto_to_menu_box_width, goto_to_menu_box_height), border_radius=15)
        window.blit(goto_to_menu_txt, (goto_to_menu_x, goto_to_menu_y))
        
        pygame.display.flip()
       