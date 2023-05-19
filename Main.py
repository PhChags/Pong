import random
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.collision import * 

#Inicialização
def ball_start(): #função inicia a bola
    global vBallX, vBallY;

    ball.set_position(screen.width/2 - ball.width/2, screen.height/2 - ball.height/2);

#função da IA do adversario
def opponent_Ai():
    if ball.x <= screen.width/2 and vBallX != 0 and vBallY != 0:
        if ball.y > opponent.y and opponent.y <= screen.height - opponent.height:
            opponent.y += padspeed * 1.25 * screen.delta_time();
        if ball.y < opponent.y and opponent.y >= 0:
            opponent.y -= padspeed * 1.25 * screen.delta_time();

screen = Window(800, 600);
screen.set_title("Pong");
keyboard = screen.get_keyboard();
points_player = 0;
points_opponent = 0;

#Game Objects
ball = Sprite("Assets/ball.png", 1);
player = Sprite("Assets/padwhite.png");
opponent = Sprite("Assets/padwhite.png");
memoria_pad = Sprite("Assets/padwhite.png");
background = GameImage("Assets/fundo.png");

#variaveis bola
ball.radius = ball.width/2;
vBallX = 0;
vBallY = 0;
ball_start();

#inicializações pads
player.set_position(screen.width - (player.width*2), screen.height/2 - player.height/2);
opponent.set_position(opponent.width, screen.height/2 - opponent.height/2);
padspeed = 250;
#padspeed1 = 250; #essas variáveis são utilizadas no modo sofre ponto tem seu pad diminuido 
#padspeed2 = 250;

#Game Loop
while(True):
    
    #entrada de dados 
    if(keyboard.key_pressed("ESC")):
        break;
    if keyboard.key_pressed("UP") and player.y >= 0:
        player.y -= padspeed * screen.delta_time();
    if keyboard.key_pressed("DOWN") and player.y <= screen.height - player.height:
        player.y += padspeed * screen.delta_time();
    if keyboard.key_pressed("SPACE"):
        vBallX = 175;
        vBallY = 175;
        vBallY *= random.choice((1,-1));
        vBallX *= random.choice((1,-1));
    
    #atualização de cena
    ball.move_x(vBallX * screen.delta_time());
    ball.move_y(vBallY * screen.delta_time());

    if ball.x > screen.width:
        points_opponent += 1;
        vBallY = 0;
        vBallX = 0;
        ball_start();
        #if player.height != memoria_pad.height/2: utilizadas no modo sofre ponto tem seu pad diminuido 
        #    player.height = memoria_pad.height/2;
        #    padspeed1 *= 1.2;
        #if opponent.height != memoria_pad.height:
        #    opponent.height = memoria_pad.height;
        #    padspeed2 = 250;
        player.set_position(screen.width - (player.width*2), screen.height/2 - player.height/2);
        opponent.set_position(opponent.width, screen.height/2 - opponent.height/2);

    elif ball.x < 0:
        points_player += 1;
        vBallY = 0;
        vBallX = 0;
        ball_start();
        #if opponent.height != memoria_pad.height/2: utilizadas no modo sofre ponto tem seu pad diminuido 
        #    padspeed2 *= 1.2;
        #    opponent.height = memoria_pad.height/2;
        #if player.height != memoria_pad.height:
        #    padspeed1 = 250;
        #    player.height = memoria_pad.height;
        player.set_position(screen.width - (player.width*2), screen.height/2 - player.height/2);
        opponent.set_position(opponent.width, screen.height/2 - opponent.height/2);

    if ball.y + ball.radius >= screen.height - ball.radius:
        vBallY *= -1.05;
        ball.move_y(vBallY * screen.delta_time());
    elif ball.y - ball.radius <= 0:
        vBallY *= -1.05;
        ball.move_y(vBallY * screen.delta_time());
    
    if opponent.collided(ball) or player.collided(ball):
        vBallX *= -1.05;
        ball.x += vBallX * screen.delta_time();
    
    opponent_Ai();       

    #desenhho da cena
    background.draw();
    screen.draw_text(f'{points_opponent}',screen.width/2 - screen.width/8, screen.height/16, 50, (255, 255, 255), "Arial", True, False);
    screen.draw_text(f'{points_player}', screen.width/2 + screen.width/8, screen.height/16, 50, (255, 255, 255), "Arial", True, False);
    ball.draw();
    player.draw();
    opponent.draw();
    screen.update();
