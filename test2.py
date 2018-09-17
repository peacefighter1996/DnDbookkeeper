import discord, random, pygame, time, asyncio
import random # just for fun
from threading import Thread

### better to set them as a global variable
client = discord.Client()

pygame.init() # put these in the beginning
gameDisplay = pygame.display.set_mode((500, 500))
white = (255,255,255)
clock = pygame.time.Clock()
green = (0,255,0)
red   = (255,0,0)
black = (0,0,0)
###
#client.send_message()
@client.event
async def on_message(message):
    # do what you want to do...
    pass

async def send_message(msg):
    await client.send_message(client.get_channel('487557731625205780'), msg) # send a message, you can use channel id or any channel instance

def run_gui(): # for running the gui
    gameDisplay.fill(white) # initialize the screen white
    current_color = red 
    my_rect = pygame.draw.rect(gameDisplay, current_color, (50,50,50,50)) # draw a rect and save the rect
    while 1: # pygame mainloop
        pygame.display.update() # update the screen
        for event in pygame.event.get(): # proper way of retrieving events
            if event.type == pygame.MOUSEBUTTONDOWN: # check if the event is right clicked on mouse 
                mouse = pygame.mouse.get_pos()
                if my_rect.collidepoint(mouse): # see if it pressed the rect
                    # do stuff if the button is pressed...
                    current_color = red
                    # send a random message maybe?
                    choosen = random.choice(['hello','hi','I am a bot','wassup','I luv u <3'])
                    asyncio.ensure_future(send_message( msg=choosen)) # since discord.py uses asyncio

                else:
                    # do stuff if it's not pressed...
                    current_color = green
                # refill the screen white
                gameDisplay.fill(white)
                # redraw the rect
                my_rect = pygame.draw.rect(gameDisplay, current_color, (50,50,50,50)) 

        clock.tick(60) # 60 fps

def run_bot(): # for running the bot
    client.run("NDg1NzgyNjg0NzMyMjI3NTk1.Dm2BWg.n2Vy6XF18PjG0S0ccUK7MrIbQPo") # run the bot

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

Thread(target=run_bot).start() # start thread the run the bot
run_gui() # run the gui