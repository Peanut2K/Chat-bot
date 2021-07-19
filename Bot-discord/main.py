import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='>')
@bot.event
async def on_ready() : 
    print("Bot Started!") 
@bot.event
async def on_message(message) :
    if message.content.startswith('>เว่น') : 
       await message.channel.send('โครตเหลี่ยม')
    elif message.content.startswith('>อย่างภาษาอังกฤษนี้ได้ไหม') :
        await message.channel.send('ก็พอได้นะ -3-')
    elif message.content.startswith('>อย่างสีเหลือง') :
        await message.channel.send('Yellow')
    elif message.content.startswith('>มะม่วง') :
        await message.channel.send('mango')
    elif message.content.startswith('>ไฟแช็ก') :
        await message.channel.send('Zippo')
    elif message.content.startswith('>อย่างสีเหลือง') :
        await message.channel.send('Yellow')
    elif message.content.startswith('>มีด') :
        await message.channel.send('อีโต้')
    elif message.content.startswith('>ชุดชั้นใน') :
        await message.channel.send('วาโก้')
    elif message.content.startswith('>เตา') :
        await message.channel.send('อั้งโล่')
    elif message.content.startswith('>เก่งอยู่นะเนี่ย') :
        await message.channel.send('///3/// พอตัว')
bot.run('ODY2NTIwNzE5ODM2MTg0NjM2.YPTwTg.VDYH0ZlPQpac8H0z_fm1hpV25w0')