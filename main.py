# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 09:48:06 2018

@author: Ian-A
"""

import discord
import asyncio
import time
import threading
import logging
import json
from json import JSONEncoder


class serverdata():
    def __init__(self, client):
        self.client = client
                    

class serverjson(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj,serverdata):
            return super(serverdata, self).default(obj)
        return obj.__dict__
def ToJsonDatabase(folder,datalist):
    location=folder+name+'.json'
    with open(location, 'w') as outfile:
        json.dump(i,
                outfile,
                indent=4, 
                sort_keys=True, 
                separators=(',', ': '), 
                ensure_ascii=False, )

try:
    client.close()
except NameError:
    print("restart client")
    client = discord.Client()

logging.basicConfig(level=logging.ERROR,
                    format='(%(threadName)-10s) %(message)s',
                    )
status = None
stop = False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    data = serverdata(client)
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

@client.event
async def on_message(message):
    if message.content.startswith('b! message'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        print("messege-channel:",message)
        print("message:        ",message.channel)
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
            
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
        await client.delete_message(message)
    elif message.content.startswith('b! status.here'):
        await statusupdate(message)
    elif message.content.startswith('b! stop'):
        stop = True
        client.send_message(message.channel, 'stopping')
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')


async def statusupdate(status):
    tmptime= time.time()
    print(tmptime)
    counter = 1
    statusmessage = await client.send_message(status.channel, 'hello general \n status update will be here')
    while(1):
        if (status != None and (tmptime+100) <time.time()):
            print("hello, world")

            await client.edit_message(statusmessage, '100 sec eleapsed')
            print(status)
            tmptime= time.time()
        if (stop == True):
            client.close()
        if ((tmptime+10*counter) < time.time()):
            await client.edit_message(statusmessage, "{} sec eleapsed".format(10*counter))
            counter += 1
            print("plus counter")
            
        # do your stuff
        await asyncio.sleep(1)
"""
t = threading.Timer(1, hello)
t.start()
"""
"""
discord = Discordclient(client=client,token="NDg1NzgyNjg0NzMyMjI3NTk1.Dm2BWg.n2Vy6XF18PjG0S0ccUK7MrIbQPo")
discord.run()
"""
#client.loop.create_task(hello())
client.run("NDg1NzgyNjg0NzMyMjI3NTk1.Dm2BWg.n2Vy6XF18PjG0S0ccUK7MrIbQPo")
client.close()