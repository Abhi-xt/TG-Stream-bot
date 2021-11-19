# (c) Code-X-Mania

from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="𝐒𝐨𝐫𝐫𝐲 𝐒𝐢𝐫, 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞. 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐦𝐲 [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](http://t.me/StreamxtSupport). ",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>⭕ **Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ!** \n\n Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ! ⭕</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇ 🤖", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="☹️ Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ ☹️ Cᴏɴᴛᴀᴄᴛ ᴍʏ [Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ](http://t.me/StreamxtSupport).",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text='☀️ Yᴏᴜʀ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴇᴅ ☀️\n\n📂 **File Name:** `{}`\n\n 🚸 Nᴏᴛᴇ : Tʜɪs ᴘᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ, Nᴏᴛ Exᴘɪʀᴇᴅ',
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton(' 💠 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ 💠 ', url=f"https://t.me/{Var.OWNER_USERNAME}"),
                                                                                       InlineKeyboardButton('👨‍💻 Developer 👨‍💻', url='https://t.me/AbirHasan2005') ] ]  ) )
                                                                                       
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="𝐒𝐨𝐫𝐫𝐲 𝐒𝐢𝐫, 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞. 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐦𝐲 [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](http://t.me/StreamxtSupport).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="⭕ **Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ!** \n\n Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ! ⭕",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel 🤖", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh 🔄",
                                                     url=f"https://t.me/{Var.APP_NAME}.herokuapp.com/{usr_cmd}") # Chnage ur app name
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="☹️ Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ ☹️ Cᴏɴᴛᴀᴄᴛ ᴍʏ [Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ](http://t.me/StreamxtSupport).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = Var.URL + 'watch/' + str(log_msg.message_id)
        online_link = Var.URL + 'download/' + str(log_msg.message_id)

        msg_text ="""
<i><u> ☀️ Yᴏᴜʀ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴇᴅ ☀️</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b>`{}`\n
<b>🚸 Nᴏᴛᴇ : Tʜɪs ᴘᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ, Nᴏᴛ Exᴘɪʀᴇᴅ</b>\n
"""

        await m.reply_text(
            text=msg_text.format(file_name),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎥 𝗦𝘁𝗿𝗲𝗮𝗺 𝗡𝗼𝘄 🎥", url=stream_link), #Stream Link
                                                InlineKeyboardButton('📥 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗡𝗼𝘄 📥', url=online_link)]]) #Download Link
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="𝐒𝐨𝐫𝐫𝐲 𝐒𝐢𝐫, 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞. 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐦𝐲 [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](http://t.me/StreamxtSupport).",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="⭕ Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ! Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ! ⭕",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Join Updates Channel 🤖", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="☹️ Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ ☹️ Cᴏɴᴛᴀᴄᴛ ᴍʏ [Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ](http://t.me/StreamxtSupport).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="Sᴇɴᴅ ᴍᴇ ᴀɴʏ Fɪʟᴇ I ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ Exᴛᴇʀɴᴀʟ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ!\ɴ\ɴAʟsᴏ I ᴀᴍ Sᴜᴘᴘᴏʀᴛᴇᴅ ɪɴ Cʜᴀɴɴᴇʟs. Aᴅᴅ ᴍᴇ ᴛᴏ Cʜᴀɴɴᴇʟ ᴀs Aᴅᴍɪɴ ᴛᴏ Mᴀᴋᴇ Mᴇ Wᴏʀᴋᴀʙʟᴇ!",
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👨‍💻 DEVELOPER 👨‍💻", url="https://t.me/AbirHasan2005")],
                [InlineKeyboardButton("🔅 Support Group 🔅", url="http://t.me/StreamxtSupport")]
            ]
        )
    )
