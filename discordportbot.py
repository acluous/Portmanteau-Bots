# testbot.py
import os

import discord
import asyncio
from discord.ui import Button, View
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO

load_dotenv('discordportbot.env')
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)
import sys
mongendata = [[],[],[],[],[],[],[],[],[]]
montypedata = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
mongensizes = {
    0: 898,
    1: 151,
    2: 100,
    3: 135,
    4: 107,
    5: 156,
    6: 72,
    7: 88,
    8: 89
}
montypesizes = {
    "b": 86,
    "k": 69,
    "d": 63,
    "e": 65,
    "y": 61,
    "h": 68,
    "f": 78,
    "l": 110,
    "t": 60,
    "g": 111,
    "o": 74,
    "i": 54,
    "n": 119,
    "p": 76,
    "c": 102,
    "r": 70,
    "s": 66,
    "w": 146
}
def reformat(list):
    string = ""
    for i in list:
        string += i
        string += "\n"
    return string

async def fileprint(ctx,list):
    buffer = BytesIO(reformat(list).encode("utf8"))  # change encoding as necessary
    await ctx.send(file=discord.File(fp=buffer, filename="results.txt"))

def getdata():
    directory = "Data Files/"
    store = open(directory + 'allalphapy.txt','r');
    content = store.read()
    mongendata[0] = content.splitlines()
    store = open(directory + 'gen1alphapy.txt','r');
    content = store.read()
    mongendata[1] = content.splitlines()
    store = open(directory + 'gen2alphapy.txt','r');
    content = store.read()
    mongendata[2] = content.splitlines()
    store = open(directory + 'gen3alphapy.txt','r');
    content = store.read()
    mongendata[3] = content.splitlines()
    store = open(directory + 'gen4alphapy.txt','r');
    content = store.read()
    mongendata[4] = content.splitlines()
    store = open(directory + 'gen5alphapy.txt','r');
    content = store.read()
    mongendata[5] = content.splitlines()
    store = open(directory + 'gen6alphapy.txt','r');
    content = store.read()
    mongendata[6] = content.splitlines()
    store = open(directory + 'gen7alphapy.txt','r');
    content = store.read()
    mongendata[7] = content.splitlines()
    store = open(directory + 'gen8alphapy.txt','r');
    content = store.read()
    mongendata[8] = content.splitlines()
    store = open(directory + 'bugmonalphapy.txt','r');
    content = store.read()
    montypedata[0] = content.splitlines()
    store = open(directory + 'darkmonalphapy.txt','r');
    content = store.read()
    montypedata[1] = content.splitlines()
    store = open(directory + 'dragonmonalphapy.txt','r');
    content = store.read()
    montypedata[2] = content.splitlines()
    store = open(directory + 'electricmonalphapy.txt','r');
    content = store.read()
    montypedata[3] = content.splitlines()
    store = open(directory + 'fairymonalphapy.txt','r');
    content = store.read()
    montypedata[4] = content.splitlines()
    store = open(directory + 'fightingmonalphapy.txt','r');
    content = store.read()
    montypedata[5] = content.splitlines()
    store = open(directory + 'firemonalphapy.txt','r');
    content = store.read()
    montypedata[6] = content.splitlines()
    store = open(directory + 'flyingmonalphapy.txt','r');
    content = store.read()
    montypedata[7] = content.splitlines()
    store = open(directory + 'ghostmonalphapy.txt','r');
    content = store.read()
    montypedata[8] = content.splitlines()
    store = open(directory + 'grassmonalphapy.txt','r');
    content = store.read()
    montypedata[9] = content.splitlines()
    store = open(directory + 'groundmonalphapy.txt','r');
    content = store.read()
    montypedata[10] = content.splitlines()
    store = open(directory + 'icemonalphapy.txt','r');
    content = store.read()
    montypedata[11] = content.splitlines()
    store = open(directory + 'normalmonalphapy.txt','r');
    content = store.read()
    montypedata[12] = content.splitlines()
    store = open(directory + 'poisonmonalphapy.txt','r');
    content = store.read()
    montypedata[13] = content.splitlines()
    store = open(directory + 'psychicmonalphapy.txt','r');
    content = store.read()
    montypedata[14] = content.splitlines()
    store = open(directory + 'rockmonalphapy.txt','r');
    content = store.read()
    montypedata[15] = content.splitlines()
    store = open(directory + 'steelmonalphapy.txt','r');
    content = store.read()
    montypedata[16] = content.splitlines()
    store = open(directory + 'watermonalphapy.txt','r');
    content = store.read()
    montypedata[17] = content.splitlines()

async def portcheck(a, b):
    longest = 0
    if len(a) < len(b):
        smollest = (0,len(a))
    elif len(a) > len(b):
        smollest = (1,len(b))
    else:
        smollest = (2,len(a))
    a = a.lower()
    b = b.lower()

    for i in range(1,smollest[1]+1):
        end = a[len(a)-i:len(a)]
        start = b[0:i]
        print("end is " + end)
        print("start is " + start)
        if end == start:
            longest = i
    #std::cout << a << " ? " << b << " ? " << longest << "\n";
    if longest < 2:
        return False;
    else:
        return True;

def dupSearch(a, b):
    none = True
    if a in b:
        none = False
    if b in a:
        none = False
    return none;
    
async def findports(a, b):
    portlist = []
    for i in range(len(a)):
        for j in range(len(b)):
            if await portcheck(a[i],b[j]):
                if dupSearch(a[i],b[j]):
                    ports = a[i] + ", " + b[j]
                    portlist.append(ports)
    return portlist

@bot.event
async def on_ready():
    getdata()
    print('Ready!')
    
@bot.command()
async def ping(ctx):
    await ctx.send("~~Pong!~~ Pang!")

@bot.command()
async def button(ctx):
    button1 = Button(label="Hi!",style=discord.ButtonStyle.gray)
    
    async def button_callback(interaction):
        await interaction.response.edit_message(content=f"Clicked!",view=None)
    
    button1.callback = button_callback
    
    view = View()
    view.add_item(button1)
    await ctx.send("~~Pong!~~ Pang!",view=view)

async def next(ctx,moreportlist,portnumber):
    interacted = False
    button = Button(label="Pokemon by Gen Number",style=discord.ButtonStyle.gray)
    button1 = Button(label="Pokemon by Type",style=discord.ButtonStyle.gray)
    async def button_callback(interaction):
        global interacted
        interacted = True
        await msg.delete()
        await pokegen(ctx,moreportlist,portnumber)
    async def button1_callback(interaction):
        global interacted
        interacted = True
        await msg.delete()
        await poketype(ctx,moreportlist,portnumber)
    button.callback = button_callback
    button1.callback = button1_callback
    view = View()
    view.add_item(button)
    view.add_item(button1)
    msg = await ctx.send("What is the type of your next parameter",view=view)
    await asyncio.sleep(10)
    if not interacted:
        await msg.edit(content="You didn't click a button in time, going back to sleep.",view=None)
        await asyncio.sleep(5)
        await msg.delete()
        
async def poketype(ctx,portlist,portnumber):
    interacted = False
    if len(portlist) > 30000:
        await ctx.send("Sorry, your query is too long (over 30k lines). Therefore, your query has ended.")
        return
    button = Button(label="All pokemon",style=discord.ButtonStyle.gray,emoji="♾️")
    button1 = Button(label="Bug Pokemon",style=discord.ButtonStyle.gray,emoji="🐛")
    button2 = Button(label="Dark Pokemon",style=discord.ButtonStyle.gray,emoji="🕶️")
    button3 = Button(label="Dragon Pokemon",style=discord.ButtonStyle.gray,emoji="🐉")
    button4 = Button(label="Electric Pokemon",style=discord.ButtonStyle.gray,emoji="⚡")
    button5 = Button(label="Fairy Pokemon",style=discord.ButtonStyle.gray,emoji="🧚")
    button6 = Button(label="Fighting Pokemon",style=discord.ButtonStyle.gray,emoji="🤜")
    button7 = Button(label="Fire Pokemon",style=discord.ButtonStyle.gray,emoji="🔥")
    button8 = Button(label="Flying Pokemon",style=discord.ButtonStyle.gray,emoji="🐦")
    button9 = Button(label="Ghost Pokemon",style=discord.ButtonStyle.gray,emoji="👻")
    button10 = Button(label="Grass Pokemon",style=discord.ButtonStyle.gray,emoji="🌱")
    button11 = Button(label="Ground Pokemon",style=discord.ButtonStyle.gray,emoji="🌎")
    button12 = Button(label="Ice Pokemon",style=discord.ButtonStyle.gray,emoji="🧊")
    button13 = Button(label="Normal Pokemon",style=discord.ButtonStyle.gray,emoji="😐")
    button14 = Button(label="Poison Pokemon",style=discord.ButtonStyle.gray,emoji="☠️")
    button15 = Button(label="Psychic Pokemon",style=discord.ButtonStyle.gray,emoji="🔮")
    button16 = Button(label="Rock Pokemon",style=discord.ButtonStyle.gray,emoji="🪨")
    button17 = Button(label="Steel Pokemon",style=discord.ButtonStyle.gray,emoji="🔩")
    button18 = Button(label="Water Pokemon",style=discord.ButtonStyle.gray,emoji="💧")
    button19 = Button(label="End Query",style=discord.ButtonStyle.danger)
    async def callbacks(number,interaction):
        global interacted
        interacted = True
        await interaction.response.defer(thinking=True)
        if number == 0:
            if portnumber == 1:
                moreportlist = mongendata[0]
            else:
                moreportlist = await findports(portlist,mongendata[0])
            if len(moreportlist) == 0:
                clear = await interaction.followup.send("Clearing thinking symbol")
                await clear.delete()
                msg2 = await ctx.send("It seems that there are no valid ports fitting your criteria. Therefore, your query has ended. Try selecting a different button!")
                await asyncio.sleep(5)
                await msg2.delete()
                return
            await fileprint(ctx,moreportlist)
            await msg.delete()
            clear = await interaction.followup.send("Clearing thinking symbol")
            await clear.delete()
            await next(ctx,moreportlist,2)
        else:
            if portnumber == 1:
                moreportlist = montypedata[number-1]
            else:
                moreportlist = await findports(portlist,montypedata[number-1])
            if len(moreportlist) == 0:
                clear = await interaction.followup.send("Clearing thinking symbol")
                await clear.delete()
                msg2 = await ctx.send("It seems that there are no valid ports fitting your criteria. Therefore, your query has ended. Try selecting a different button!")
                await asyncio.sleep(5)
                await msg2.delete()
                return
            await fileprint(ctx,moreportlist)
            await msg.delete()
            clear = await interaction.followup.send("Clearing thinking symbol")
            await clear.delete()
            await next(ctx,moreportlist,portnumber+1)
    
    async def button_callback(interaction):
        await callbacks(0,interaction)
    async def button1_callback(interaction):
        await callbacks(1,interaction)
    async def button2_callback(interaction):
        await callbacks(2,interaction)
    async def button3_callback(interaction):
        await callbacks(3,interaction)
    async def button4_callback(interaction):
        await callbacks(4,interaction)
    async def button5_callback(interaction):
        await callbacks(5,interaction)
    async def button6_callback(interaction):
        await callbacks(6,interaction)
    async def button7_callback(interaction):
        await callbacks(7,interaction)
    async def button8_callback(interaction):
        await callbacks(8,interaction)
    async def button9_callback(interaction):
        await callbacks(9,interaction)
    async def button10_callback(interaction):
        await callbacks(10,interaction)
    async def button11_callback(interaction):
        await callbacks(11,interaction)
    async def button12_callback(interaction):
        await callbacks(12,interaction)
    async def button13_callback(interaction):
        await callbacks(13,interaction)
    async def button14_callback(interaction):
        await callbacks(14,interaction)
    async def button15_callback(interaction):
        await callbacks(15,interaction)
    async def button16_callback(interaction):
        await callbacks(16,interaction)
    async def button17_callback(interaction):
        await callbacks(17,interaction)
    async def button18_callback(interaction):
        await callbacks(18,interaction)
    async def button19_callback(interaction):
        global interacted
        interacted = True
        await interaction.response.edit_message(content=f"Query Ended",view=None)
        await asyncio.sleep(5)
        await msg.delete()
    
    button.callback = button_callback
    button1.callback = button1_callback
    button2.callback = button2_callback
    button3.callback = button3_callback
    button4.callback = button4_callback
    button5.callback = button5_callback
    button6.callback = button6_callback
    button7.callback = button7_callback
    button8.callback = button8_callback
    button9.callback = button9_callback
    button10.callback = button10_callback
    button11.callback = button11_callback
    button12.callback = button12_callback
    button13.callback = button13_callback
    button14.callback = button14_callback
    button15.callback = button15_callback
    button16.callback = button16_callback
    button17.callback = button17_callback
    button18.callback = button18_callback
    button19.callback = button19_callback

    view = View()
    view.add_item(button)
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    view.add_item(button6)
    view.add_item(button7)
    view.add_item(button8)
    view.add_item(button9)
    view.add_item(button10)
    view.add_item(button11)
    view.add_item(button12)
    view.add_item(button13)
    view.add_item(button14)
    view.add_item(button15)
    view.add_item(button16)
    view.add_item(button17)
    view.add_item(button18)
    view.add_item(button19)
    
    msg = await ctx.send("Welcome to Make-a-Port! What will be your first port?",view=view)
    await asyncio.sleep(10)
    if not interacted:
        await msg.edit(content="You didn't click a button in time, going back to sleep.",view=None)
        await asyncio.sleep(5)
        await msg.delete()
        
async def pokegen(ctx,portlist,portnumber):
    interacted = False
    if len(portlist) > 30000:
        await ctx.send("Sorry, your query is too long (over 30k lines). Therefore, your query has ended.")
        return
    button = Button(label="All pokemon",style=discord.ButtonStyle.gray,emoji="♾️")
    button1 = Button(label="Gen 1 Pokemon",style=discord.ButtonStyle.gray,emoji="1️⃣")
    button2 = Button(label="Gen 2 Pokemon",style=discord.ButtonStyle.gray,emoji="2️⃣")
    button3 = Button(label="Gen 3 Pokemon",style=discord.ButtonStyle.gray,emoji="3️⃣")
    button4 = Button(label="Gen 4 Pokemon",style=discord.ButtonStyle.gray,emoji="4️⃣")
    button5 = Button(label="Gen 5 Pokemon",style=discord.ButtonStyle.gray,emoji="5️⃣")
    button6 = Button(label="Gen 6 Pokemon",style=discord.ButtonStyle.gray,emoji="6️⃣")
    button7 = Button(label="Gen 7 Pokemon",style=discord.ButtonStyle.gray,emoji="7️⃣")
    button8 = Button(label="Gen 8 Pokemon",style=discord.ButtonStyle.gray,emoji="8️⃣")
    button9 = Button(label="End Query",style=discord.ButtonStyle.danger)
    async def callbacks(number,interaction):
        global interacted
        interacted = True
        await interaction.response.defer(thinking=True)
        if portnumber == 1:
            moreportlist = mongendata[number]
        else:
            moreportlist = await findports(portlist,mongendata[number])
        if len(moreportlist) == 0:
            clear = await interaction.followup.send("Clearing thinking symbol")
            await clear.delete()
            msg2 = await ctx.send("It seems that there are no valid ports fitting your criteria. Therefore, your query has ended. Try selecting a different button!")
            await asyncio.sleep(5)
            await msg2.delete()
            return
        await fileprint(ctx,moreportlist)
        await msg.delete()
        clear = await interaction.followup.send("Clearing thinking symbol")
        await clear.delete()
        await next(ctx,moreportlist,portnumber+1)
    
    async def button_callback(interaction):
        await callbacks(0,interaction)
    async def button1_callback(interaction):
        await callbacks(1,interaction)
    async def button2_callback(interaction):
        await callbacks(2,interaction)
    async def button3_callback(interaction):
        await callbacks(3,interaction)
    async def button4_callback(interaction):
        await callbacks(4,interaction)
    async def button5_callback(interaction):
        await callbacks(5,interaction)
    async def button6_callback(interaction):
        await callbacks(6,interaction)
    async def button7_callback(interaction):
        await callbacks(7,interaction)
    async def button8_callback(interaction):
        await callbacks(8,interaction)
    async def button9_callback(interaction):
        global interacted
        interacted = True
        await interaction.response.edit_message(content=f"Query Ended",view=None)
        await asyncio.sleep(5)
        await msg.delete()
    
    button.callback = button_callback
    button1.callback = button1_callback
    button2.callback = button2_callback
    button3.callback = button3_callback
    button4.callback = button4_callback
    button5.callback = button5_callback
    button6.callback = button6_callback
    button7.callback = button7_callback
    button8.callback = button8_callback
    button9.callback = button9_callback

    view = View()
    view.add_item(button)
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    view.add_item(button6)
    view.add_item(button7)
    view.add_item(button8)
    view.add_item(button9)
    if portnumber == 1:
        msg = await ctx.send("What will be your first port?",view=view)
    else:
        msg = await ctx.send("What will be your next port?",view=view)
    await asyncio.sleep(10)
    if not interacted:
        await msg.edit(content="You didn't click a button in time, going back to sleep.",view=None)
        await asyncio.sleep(5)
        await msg.delete()
@bot.command()
async def build(ctx):
    interacted = False
    button = Button(label="Pokemon by Gen Number",style=discord.ButtonStyle.gray)
    button1 = Button(label="Pokemon by Type",style=discord.ButtonStyle.gray)
    async def button_callback(interaction):
        global interacted
        interacted = True
        await msg.delete()
        await pokegen(ctx,[],1)
    async def button1_callback(interaction):
        global interacted
        interacted = True
        await msg.delete()
        await poketype(ctx,[],1)
    button.callback = button_callback
    button1.callback = button1_callback
    view = View()
    view.add_item(button)
    view.add_item(button1)
    msg = await ctx.send("Welcome to Make-a-Port! What type of parameter do you want?",view=view)
    await asyncio.sleep(10)
    if not interacted:
        await msg.edit(content="You didn't click a button in time, going back to sleep.",view=None)
        await asyncio.sleep(5)
        await msg.delete()

'''@bot.command()
async def port(ctx, arg,arg2):
    print("arg is " + arg)
    print("arg2 is " + arg2)
    if portcheck(arg,arg2) and arg != arg2:
        await ctx.send("True!")
    else:
        await ctx.send("False!")'''

'''@bot.command()
async def find(ctx):
    ports = await findports(mongendata[1],mongendata[2])
    buffer = BytesIO(reformat(ports).encode("utf8"))  # change encoding as necessary
    await ctx.send(file=discord.File(fp=buffer, filename="results.txt"))'''


'''@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.bot:
        return
    await message.channel.send('你好!')
    await bot.process_commands(message)'''
bot.run(TOKEN)
