# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Clone Code Credit : YT - @Tech_VJ / TG - @VJ_Bots / GitHub - @VJBots

import os, string, logging, random, asyncio, time, datetime, re, sys, json, base64
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import *
from database.ia_filterdb import col, sec_col, get_file_details, unpack_new_file_id, get_bad_files
from database.users_chats_db import db
from CloneTechVJ.database.clone_bot_userdb import clonedb
from info import *
from shortzy import Shortzy
from utils import get_size, temp, get_seconds, get_clone_shortlink
logger = logging.getLogger(__name__)

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    me = await client.get_me()
    cd = await db.get_bot(me.id)
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [[
            InlineKeyboardButton('Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ', url=f'http://t.me/{me.username}?startgroup=true')
        ]]
        if cd["update_channel_link"] != None:
            up = cd["update_channel_link"]
            buttons.append([InlineKeyboardButton('⛔Jᴏɪɴ Mᴀɪɴ Cʜᴀɴɴᴇʟ⛔', url=up)])
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.CLONE_START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, me.username, me.first_name), reply_markup=reply_markup)
        return 
    if not await clonedb.is_user_exist(me.id, message.from_user.id):
        await clonedb.add_user(me.id, message.from_user.id)
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton('Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ', url=f'http://t.me/{me.username}?startgroup=true')
        ],[
            InlineKeyboardButton('☎️ Hᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('😎 Aʙᴏᴜᴛ', callback_data='about')
        ]]
        if cd["update_channel_link"] != None:
            up = cd["update_channel_link"]
            buttons.append([InlineKeyboardButton('⛔Jᴏɪɴ Mᴀɪɴ Cʜᴀɴɴᴇʟ⛔', url=up)])
        reply_markup = InlineKeyboardMarkup(buttons)
        m=await message.reply_sticker("CAACAgUAAxkBAAIFjWeSFVlDymtKrBDeXUCoPO_wOofHAAI7BAAC5I0IVOuQG158cYXwHgQ") 
        await asyncio.sleep(1)
        await m.delete()
        await message.reply_text(
            text=script.CLONE_START_TXT.format(message.from_user.mention, me.username, me.first_name),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    data = message.command[1]
    try:
        pre, file_id = data.split('_', 1)
    except:
        file_id = data
        pre = ""
    if data.startswith("sendfiles"):
        chat_id = int("-" + file_id.split("-")[1])
        userid = message.from_user.id if message.from_user else None
        g = await get_clone_shortlink(f"https://telegram.me/{me.username}?start=allfiles_{file_id}", cd["url"], cd["api"])
        t = cd["tutorial"]
        btn = [[
            InlineKeyboardButton('📂 Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ 📂', url=g)
        ],[
            InlineKeyboardButton('⁉️ Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ ⁉️', url=t)
        ]]
        k = await client.send_message(chat_id=message.from_user.id,text=f"<b>Gᴇᴛ Aʟʟ Fɪʟᴇs Iɴ A Sɪɴɢʟᴇ Cʟɪᴄᴋ!!!\n\n📂 Lɪɴᴋ ➠ : {g}\n\n<i>Nᴏᴛᴇ: Tʜɪs Mᴇssᴀɢᴇ Is Dᴇʟᴇᴛᴇᴅ Iɴ 5 Mɪɴs Tᴏ Avoid Cᴏᴘʏʀɪɢʜᴛs. Fᴏʀᴡᴀʀᴅ Tʜᴇ Lɪɴᴋs Iɴ Yᴏᴜʀ Sᴀᴠᴇᴅ Mᴇssᴀɢᴇs</i></b>", reply_markup=InlineKeyboardMarkup(btn))
        await asyncio.sleep(300)
        await k.edit("<b>Mᴇssᴀɢᴇ Is Sᴜᴄᴄᴇsғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ</b>")
        return
        
    
    elif data.startswith("short"):
        user = message.from_user.id
        files_ = await get_file_details(file_id)
        files = files_
        g = await get_clone_shortlink(f"https://telegram.me/{me.username}?start=file_{file_id}", cd["url"], cd["api"]) 
        t = cd["tutorial"]
        btn = [[
            InlineKeyboardButton('📂 Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ 📂', url=g)
        ],[
            InlineKeyboardButton('⁉️ Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ ⁉️', url=t)
        ]]
        k = await client.send_message(chat_id=user,text=f"<b>📕Nᴀᴍᴇ ➠ : <code>{files['file_name']}</code> \n\n🔗Sɪᴢᴇ ➠ : {get_size(files['file_size'])}\n\n📂Fɪʟᴇ ʟɪɴᴋ ➠ : {g}\n\n<i>Nᴏᴛᴇ: Tʜɪs Mᴇssᴀɢᴇ Is Dᴇʟᴇᴛᴇᴅ Iɴ 20 Mɪɴs Tᴏ Avoid Cᴏᴘʏʀɪɢʜᴛs. Fᴏʀᴡᴀʀᴅ Tʜᴇ Lɪɴᴋs Iɴ Yᴏᴜʀ Sᴀᴠᴇᴅ Mᴇssᴀɢᴇs</i></b>", reply_markup=InlineKeyboardMarkup(btn))
        await asyncio.sleep(1200)
        await k.edit("<b>Mᴇssᴀɢᴇ Is Sᴜᴄᴄᴇsғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ</b>")
        return
        
    elif data.startswith("all"):
        files = temp.GETALL.get(file_id)
        if not files:
            return await message.reply('<b><i>No such file exist.</b></i>')
        filesarr = []
        for file in files:
            vj_file_id = file['file_id']
            k = await temp.BOT.send_cached_media(chat_id=PUBLIC_FILE_CHANNEL, file_id=vj_file_id)
            vj = await client.get_messages(PUBLIC_FILE_CHANNEL, k.id)
            mg = getattr(vj, vj.media.value)
            file_id = mg.file_id
            files_ = await get_file_details(vj_file_id)
            files1 = files_
            title = ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files1['file_name'].split()))
            size=get_size(files1['file_size'])
            f_caption=files1['caption']
            if f_caption is None:
                f_caption = f"{' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files1['file_name'].split()))}"
            if cd["update_channel_link"] != None:
                up = cd["update_channel_link"]
                button = [[
                    InlineKeyboardButton('⛔Jᴏɪɴ Mᴀɪɴ Cʜᴀɴɴᴇʟ⛔', url=up)
                ]]
                reply_markup=InlineKeyboardMarkup(button)
            else:
                reply_markup=None
       
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file_id,
                caption=f_caption,
                protect_content=False,
                reply_markup=reply_markup
            )
            filesarr.append(msg)
        k = await client.send_message(chat_id = message.from_user.id, text=f"<b><u>❗️❗️❗️Iᴍᴘᴏʀᴛᴀɴᴛ❗️️❗️❗️</u></b>\n\nTʜɪs Mᴏᴠɪᴇ Fɪʟᴇs/Vɪᴅᴇᴏs Wɪʟʟ Bᴇ Dᴇʟᴇᴛᴇᴅ Iɴ <b><u>10 Mɪɴs</u> 🫥 <i></b>(Dᴜᴇ Tᴏ CᴏᴘʏRɪɢʜᴛ Issᴜᴇs)</i>.\n\n<b><i>Pʟᴇᴀsᴇ Fᴏʀᴡᴀʀᴅ Aʟʟ Fɪʟᴇs/Vɪᴅᴇᴏs To Yᴏᴜʀ Sᴀᴠᴇᴅ Mᴇssᴀɢᴇs Aɴᴅ Sᴛᴀʀᴛ Dᴏᴡɴʟᴏᴀᴅ Tʜᴇʀᴇ</i></b>")
        await asyncio.sleep(600)
        for x in filesarr:
            await x.delete()
        await k.edit_text("<b>Yᴏᴜʀ Aʟʟ Fɪʟᴇs/Vɪᴅᴇᴏs Is Sᴜᴄᴄᴇsғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ!!!</b>")
        return    
    elif data.startswith("files"):
        if cd['url']:
            files_ = await get_file_details(file_id)
            files = files_
            g = await get_clone_shortlink(f"https://telegram.me/{me.username}?start=file_{file_id}", cd["url"], cd["api"])
            t = cd["tutorial"]
            btn = [[
                InlineKeyboardButton('📂 Dᴏᴡɴʟᴏᴀᴅ Nᴏᴡ 📂', url=g)
            ],[
                InlineKeyboardButton('⁉️ Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ ⁉️', url=t)
            ]]
            k = await client.send_message(chat_id=message.from_user.id,text=f"<b>📕Nᴀᴍᴇ ➠ : <code>{files['file_name']}</code> \n\n🔗Sɪᴢᴇ ➠ : {get_size(files['file_size'])}\n\n📂Fɪʟᴇ ʟɪɴᴋ ➠ : {g}\n\n<i>Note: Tʜɪs Mᴇssᴀɢᴇ Is Dᴇʟᴇᴛᴇᴅ Iɴ 20 Mɪɴs Tᴏ Aᴠᴏɪᴅ CᴏᴘʏRɪɢʜᴛs. Sᴀᴠᴇ Tʜᴇ Lɪɴᴋs Tᴏ Sᴏᴍᴇᴡʜᴇʀᴇ Eʟsᴇ</i></b>", reply_markup=InlineKeyboardMarkup(btn))
            await asyncio.sleep(1200)
            await k.edit("<b>Mᴇssᴀɢᴇ Is sᴜᴄᴄᴇsғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ</b>")
            return
    user = message.from_user.id
    files_ = await get_file_details(file_id)           
    if not files_:
        return await message.reply('**Nᴏ Sᴜᴄʜ Fɪʟᴇ Exɪsᴛs.**')
    files = files_
    title = ' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files['file_name'].split()))
    size=get_size(files['file_size'])
    f_caption=files['caption']
    if f_caption is None:
        f_caption = f"{' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@'), files['file_name'].split()))}"
    if cd["update_channel_link"] != None:
        up = cd["update_channel_link"]
        button = [[
            InlineKeyboardButton('⛔Jᴏɪɴ Mᴀɪɴ Cʜᴀɴɴᴇʟ⛔', url=up)
        ]]
        reply_markup=InlineKeyboardMarkup(button)
    else:
        reply_markup=None
    k = await temp.BOT.send_cached_media(chat_id=PUBLIC_FILE_CHANNEL, file_id=file_id)
    vj = await client.get_messages(PUBLIC_FILE_CHANNEL, k.id)
    m = getattr(vj, vj.media.value)
    file_id = m.file_id
    msg = await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        protect_content=False,
        reply_markup=reply_markup
    )
    k = await msg.reply("<b><u>❗️❗️❗️Iᴍᴘᴏʀᴛᴀɴᴛ❗️️❗️❗️</u></b>\n\nTʜɪs Mᴏᴠɪᴇ Fɪʟᴇ/Vɪᴅᴇᴏ Wɪʟʟ Bᴇ Dᴇʟᴇᴛᴇᴅ Iɴ <b><u>10 Mɪɴs</u> 🫥 <i></b>(Dᴜᴇ Tᴏ CᴏᴘʏRɪɢʜᴛ Issᴜᴇs)</i>.\n\n<b><i>Pʟᴇᴀsᴇ Fᴏʀᴡᴀʀᴅ Tʜɪs Fɪʟᴇ/Vɪᴅᴇᴏ Tᴏ Yᴏᴜʀ Sᴀᴠᴇᴅ Mᴇssᴀɢᴇs Aɴᴅ Sᴛᴀʀᴛ Dᴏᴡɴʟᴏᴀᴅ Tʜᴇʀᴇ</i></b>",quote=True)
    await asyncio.sleep(600)
    await msg.delete()
    await k.edit_text("<b>Fɪʟᴇ/Vɪᴅᴇᴏ Is Sᴜᴄᴄᴇғᴜʟʟʏ Dᴇʟᴇᴛᴇᴅ!!!</b>")
    return   
  
@Client.on_message(filters.command("settings") & filters.private)
async def settings(client, message):
    me = await client.get_me()
    owner = await db.get_bot(me.id)
    if owner["user_id"] != message.from_user.id:
        return
    url = await client.ask(message.chat.id, "<b>Nᴏᴡ Sᴇɴᴅ Mᴇ Yᴏᴜʀ Sʜᴏʀᴛʟɪɴᴋ Dᴏᴍᴀɪɴ Wɪᴛʜᴏᴜᴛ https://</b>")
    api = await client.ask(message.chat.id, "<b>Nᴏᴡ Sᴇɴᴅ Yᴏᴜʀ Aᴘɪ</b>")
    try:
        shortzy = Shortzy(api_key=api.text, base_site=url.text)
        link = 'https://t.me/Cp_Flicks'
        await shortzy.convert(link)
    except Exception as e:
        await message.reply(f"**Eʀʀᴏʀ Iɴ Cᴏɴᴠᴇʀᴛɪɴɢ Lɪɴᴋ**\n\n<code>{e}</code>\n\n**Sᴛᴀʀᴛ Tʜᴇ Pʀᴏᴄᴇss Aɢᴀɪɴ Bʏ - /settings**", reply_markup=InlineKeyboardMarkup(btn))
        return
    tutorial = await client.ask(message.chat.id, "<b>Sᴇɴᴅ Mᴇ Yᴏᴜʀ Hᴏᴡ Tᴏ Oᴘᴇɴ Lɪɴᴋ/Tᴜᴛᴏʀɪᴀʟ Lɪɴᴋ.</b>")
    if not tutorial.text.startswith(('https://', 'http://')):
        await message.reply("**Iɴᴠᴀʟɪᴅ Lɪɴᴋs. Sᴛᴀʀᴛ Tʜᴇ Pʀᴏᴄᴇss Aɢᴀɪɴ Bʏ - /settings**")
        return 
    link = await client.ask(message.chat.id, "<b>Nᴏᴡ Sᴇɴᴅ Mᴇ Yᴏᴜʀ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Lɪɴᴋ Wʜɪᴄʜ Is Sʜᴏᴡɴ Iɴ Yᴏᴜʀ Sᴛᴀʀᴛ Bᴜᴛᴛᴏɴ Aɴᴅ Bᴇʟᴏᴡ Fɪʟᴇ Bᴜᴛᴛᴏɴ.</b>")
    if not link.text.startswith(('https://', 'http://')):
        await message.reply("**Iɴᴠᴀʟɪᴅ Lɪɴᴋ Sᴛᴀʀᴛ Tʜᴇ Pʀᴏᴄᴇss Aɢᴀɪɴ Bʏ - /settings**")
        return 
    data = {
        'url': url.text,
        'api': api.text,
        'tutorial': tutorial.text,
        'update_channel_link': link.text
    }
    await db.update_bot(me.id, data)
    await message.reply("**Sᴜᴄᴄᴇsғᴜʟʟʏ Aᴅᴅᴇᴅ Aʟʟ Sᴇᴛᴛɪɴɢs**")

@Client.on_message(filters.command("reset") & filters.private)
async def reset_settings(client, message):
    me = await client.get_me()
    owner = await db.get_bot(me.id)
    if owner["user_id"] != message.from_user.id:
        return
    if owner["url"] == None:
        await message.reply("**Nᴏ Sᴇᴛᴛɪɴɢs Fᴏᴜɴᴅ.**")
    else:
        data = {
            'url': None,
            'api': None,
            'tutorial': None,
            'update_channel_link': None
        }
        await db.update_bot(me.id, data)
        await message.reply("**Sᴜᴄᴄᴇsғᴜʟʟʏ Rᴇsᴇᴛ Aʟʟ Sᴇᴛᴛɪɴɢs Tᴏ Dᴇғᴀᴜʟᴛ**")

@Client.on_message(filters.command("stats") & filters.private)
async def stats(client, message):
    me = await client.get_me()
    total_users = await clonedb.total_users_count(me.id)
    filesp = col.count_documents({})
    totalsec = sec_col.count_documents({})
    total = int(filesp) + int(totalsec)
    await message.reply(f"**Tᴏᴛᴀʟ Fɪʟᴇs : {total}\n\nTᴏᴛᴀʟ Usᴇʀs : {total_users}**")
