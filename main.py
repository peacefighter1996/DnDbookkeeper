# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:25:07 2018

discord python discord bot. 

@author: Ian-A
"""
import os
import json
import discord
import asyncio
import pytz as timezone
from itertools import cycle
from discord.ext import commands



#globals
TOKEN = "NDg1NzgyNjg0NzMyMjI3NTk1.Dm2BWg.n2Vy6XF18PjG0S0ccUK7MrIbQPo"


try:
    client.logout()
    client.close()
except NameError:
    print("restart client")
    client = commands.Bot(command_prefix = 'b!')
class Person():
    def __init__(self,
                 server,
                 character
                 ):
        self.gamecounters = []
        self.characters = [character.ch_character_id]

class Character():
    def __init__(self,
                 chracter_name=None,
                 character_race=None,
                 character_class=None,
                 character_owner_name=None,
                 character_owner_id=None,
                 character_server_id=None,
                 character_id= None):
        self.title = ""
        self.chpicture = ""
        self.name = chracter_name
        self.race = character_race
        self.ch_class = [[character_class,3]]
        self.ch_owner = character_owner_name
        self.ch_owner_id = character_owner_id
        self.ch_server = character_server_id
        self.ch_character_id = character_id
        self.approved = False
        self.expriance = 0
        self.balance = 0
        self.items = []
        printstring = "owner = {}\nserver = {}\nname = {}\nrace = {}\nclass = {} lvl {}".format(self.ch_owner, self.ch_server,self.name, self.race, self.ch_class[0][1], self.ch_class[0][0])
        print (printstring)
        return
    def printembed(self):
        embed = discord.Embed(
                title = "{} {}".format(self.name, self.title),
                colour = discord.Colour.blue()
        )
        embed.description = "New player character created"
        if len(self.chpicture) >1:
            embed.set_image(url=self.chpicture)
        embed.set_footer(text = self.ch_owner)
        embed.add_field(name = 'Race:', value = self.race, inline = True)
        classestext =""
        for data in self.ch_class:
            classestext += "{} level {}\n".format(data[1],data[0])
        embed.add_field(name = 'Class:', value = classestext, inline = True)
        return embed

class Game_manager():
    def __init__(self,
                 gameID):
        self.gameID = gameID
        self.playeramount = [0,1]
        self.playerlevels = [3,20]
        self.gamedate = None
        self.players = [[],[],[]]
        self.gamestart = ""
        self.playerleft = []
class TTGame():
    def __init__(self):
        self.name
        self.discription
        self.gameLink
        self.ex_players

class ServerDatabase():
    def __init__(self,
                 server):
        self.server_id = server.id
        self.server_name = server.name
        self.character = []
        self.approvallist = []
        self.characters_count = 0
        return
    
    def addcharacter(self, character):
        counter = 0
        found = False
        for data in self.character:
            if data[0]==character.ch_owner_id:
                found = True
                break;
            counter += 1;
        if found:
            self.character[counter].append(character.name)
        else:
            self.character.append([character.ch_owner_id,character.ch_owner,character.name])
        self.approvallist.append([character.ch_owner_id,character.ch_owner,character.name])
        return
    def getapprovallist(self):
        approvaldata = discord.Embed(
            title = "approval list"
            )
        if (len(self.approvallist)>0):
            for data in self.approvallist:
                approvaldata.add_field(name="person", 
                                       value= data[1],
                                       inline = False)
                approvaldata.add_field(name="character",
                                       value= data[2],
                                       inline = True)
                approvaldata.add_field(name="command",
                                       value="{}s_approve {} {}".format(client.command_prefix,data[1],data[2]),
                                       inline = True)
        else:
            approvaldata.description = "No players are waiting for there characters to be approved"
        return approvaldata
        #print (approvaldata)

class DungeonMaster():
    def __init__(self):
        """
        game creation
        game start
        game stop for player
        game stop
        """
        self.gamecreation
        """
        charcter approve
        character unapprove
        """
        self.characterapproval


def serialize_json(instance=None, path=None):
    dt = instance.__dict__
    print(dt)
    with open(path, "w") as file:
        json.dump(dt, file, sort_keys=True, indent=4)

def deserialize_json(cls=None, path=None):
    def read_json(_path):
        with open(_path, "r") as file:
            return json.load(file)

    data = read_json(path)

    instance = object.__new__(cls)

    for key, value in data.items():
        setattr(instance, key, value)

    return instance

def WriteToDatabase(server,
                    person = None,
                    person_id = None,
                    character = None,
                    merchant = None,
                    game = None,
                    graveyard = None):
    #server setup
    serverpath = r'Database\{}'.format(server.server_id)
    serverjson = r"{}\server.json".format(serverpath)
    #gamepath = r"{}\games".format(serverpath)
    #merchantpath = r"{}\merchant".format(serverpath)
    #graveyardpath = r"{}\graveyard".format(serverpath)
    
    
    
    
    """
    if graveyard:
        graveyardpath = r'{}\{}.json'.format(graveyardpath,graveyard.name)
        if not os.path.exists(graveyardpath):
              os.makedirs(graveyardpath)
        serialize_json(graveyard, graveyardpath)
    """
    if person:
        personpath = r'{}\{}'.format(serverpath,person.id) 
        if not os.path.exists(personpath):
            os.makedirs(personpath)
        #personjsonpath = r"{}\person.json"
    elif person_id:
        personpath = r'{}\{}'.format(serverpath,person_id) 
    if character:
        chpath = r'{}\{}.json'.format(personpath,character.name)
        if not os.path.exists(chpath):
            serialize_json(character, chpath)
        else:
            print("character already exist")
    
    serialize_json(server,serverjson)

def GetCharacterData(ctx,character_name,person_id=None):
    if person_id:
        characterjson = r'Database\{}\{}\{}.json'.format(ctx.message.server.id,
                                   person_id,
                                   character_name)
    else:
        characterjson = r'Database\{}\{}\{}.json'.format(ctx.message.server.id,
                               ctx.message.author.id,
                               character_name)
    character = Character();
    character = deserialize_json(type(character),characterjson)
    return character
    


def GetServerData(ctx):
    serverpath = r'Database\{}'.format(ctx.message.server.id)
    serverjson = r"{}\server.json".format(serverpath)
    server = ServerDatabase(ctx.message.server)
    server= deserialize_json(type(server),serverjson)
    return server

"""
discord command list
"""
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="waiting on costumer"))
    print("Bot is ready to roll")

@client.event
async def on_message(message):
    
    serverpath = r'Database\{}'.format(message.server.id)
    if not os.path.exists(serverpath):
        os.makedirs(serverpath)
        serverjson = r"{}\server.json".format(serverpath)
        gamepath = r"{}\games".format(serverpath)
        merchantpath = r"{}\merchant".format(serverpath)
        graveyardpath = r"{}\graveyard".format(serverpath)
      
        if not os.path.exists(serverjson):
            server = ServerDatabase(message.server)
            WriteToDatabase(server)
        if not os.path.exists(gamepath):        os.makedirs(gamepath)
        if not os.path.exists(merchantpath):    os.makedirs(merchantpath) 
        if not os.path.exists(graveyardpath):   os.makedirs(graveyardpath)
   
    await client.change_presence(game=discord.Game(name="Working on your library"))


    # print("see message")
    await client. process_commands(message)

client.remove_command('ch_create')  
@client.command(pass_context = True,)
async def ch_create(ctx, ch_name, ch_race, ch_class):
    #print(ctx)
    server = GetServerData(ctx)
    author = ctx.message.author
    print ("server = {}\nauthor = {}".format(server.characters_count,author))
    newchar = Character(ch_name,ch_race,ch_class,author.name,author.id,server.server_id,server.characters_count)
    server.characters_count += 1
    server.addcharacter(newchar)
    WriteToDatabase(server,person = author, character = newchar)
    client.delete_message(ctx)
    await client.say(embed=newchar.printembed())

client.remove_command('embedhelp')      
@client.command(pass_context = True)
async def embedhelp(ctx):
    embed = discord.Embed(
            colour = discord.Colour.orange()
            )
    embed.set_author(name = "Help")
    embed.add_field(name = "b!chcreate <character name> <character race> <character class>",
                    value = """this command will create your character inside the discord server.
                    <character name> : name of your character
                    <character race> : race of your character
                    <character class>: beggining class
                    
                    on the background the following parameters will be set:
                    <character approval> = False: your character will be unaproved untill review and accepted by an admin
                
                    in development parts:
                    <title> = None : title that your chracter has earned during your endavour
                    <character image> = None : title that your chracter has earned during your endavour"""
                    )
    await client.say(embed = embed)


client.remove_command('s_approve_list')      
@client.command(pass_context = True)
async def s_approval_list(ctx):
    server = GetServerData(ctx)
    approvaldata = server.getapprovallist()
    await client.say(embed = approvaldata)

client.remove_command('s_approve_list')      
@client.command(pass_context = True)
async def s_approve_list(ctx):
    server = GetServerData(ctx)
    approvaldata = server.getapprovallist()
    await client.say(embed = approvaldata)

client.remove_command('s_approve')      
@client.command(pass_context = True) 
async def s_approve(ctx, person, character):
    server = GetServerData(ctx)
    counter = 0
    for data in server:
        for data in server.approvallist:
            if (data[1]==person and data[2]==character):
                character = GetCharacterData(ctx,data[2],data[0])
                character.approved = True
                del server.approvallist[counter]
                
                WriteToDatabase(server,person_id = data[0], character = character)
                
                await client.say("{}'s character {} has been approved and will now be able to join games".format(person, character.name))
                break;
            counter += 1
        break;
    
    

client.remove_command('stopbot')  
@client.command()
async def stopbot():
    print("stopbot")
    client.logout()
    client.close()

client.run(TOKEN)