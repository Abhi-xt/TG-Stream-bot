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
                        text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n @EverythingSuckz **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>[̲̅J][̲̅ᴏ][̲̅ɪ][̲̅ɴ]  [̲̅ᴍ][̲̅ʏ]   [̲̅ᴜ][̲̅ᴘ][̲̅ᴅ][̲̅ᴀ][̲̅ᴛ][̲̅ᴇ][̲̅S]  [̲̅ᴄ][̲̅ʜ][̲̅ᴀ][̲̅ɴ][̲̅ɴ][̲̅ᴇ][̲̅ʟ]  [̲̅ᴛ][̲̅ᴏ]  [̲̅ᴜ][̲̅s][̲̅ᴇ]  [̲̅ᴍ][̲̅ᴇ] 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>😞 𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐖𝐞𝐧𝐭 𝐖𝐫𝐨𝐧𝐠 😞</i> <b> <a href='https://t.me/EverythingSuckz'>CLICK HERE FOR SUPPORT </a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="""
<i>👋 Hᴇʏ, I'ᴍ Tᴇʟᴇɢʀᴀᴍ Fɪʟᴇs Sᴛʀᴇᴀᴍɪɴɢ Bᴏᴛ ᴀs ᴡᴇʟʟ Dɪʀᴇᴄᴛ Lɪɴᴋs Gᴇɴᴇʀᴀᴛᴇ</i>\n
<i>𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐠𝐞𝐭 𝐚𝐧 𝐢𝐧𝐬𝐭𝐚𝐧𝐭 𝐬𝐭𝐫𝐞𝐚𝐦 𝐥𝐢𝐧𝐤</i>\n
<i> 𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸 :- 🔞 Pʀᴏɴ ᴄᴏɴᴛᴇɴᴛꜱ ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ ʏᴏᴜ.</i>\n
<i><b>🍃 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :</b>@EverythingSuckz</i>""",
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton(' 👨‍💻 Owner 👨‍💻 ', url=f"https://t.me/{Var.OWNER_USERNAME}"),
                                                                                       InlineKeyboardButton('❤️ Follow Me ❤️', url='https://github.com/EverythingSuckz') ] ]  ) )
                                                                                       
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Qᴜɪᴄᴋʟʏ ᴄᴏɴᴛᴀᴄᴛ** @EverythingSuckz",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Pʟᴇᴀsᴇ Jᴏɪɴ  Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ**!\n\n**Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ**!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh / Try Again",
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
                    text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍᴇ** [Bot Dunia Support](https://t.me/BotDuniaSupport).",
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
<i><u> ☀️ 𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 ☀️</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>`{}`</i>\n
<i>🍃 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :</i> <b>~@EverythingSuckz</b>"""

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
                    text="<i>Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ FROM USING ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Pʟᴇᴀsᴇ Jᴏɪɴ  Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍᴇ",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""
<i>Sᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.</i>\n
<i>I ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴇxᴛᴇʀɴᴀʟ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ AND STREAM ʟɪɴᴋ !.</i>\n
<u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u>\n
<b> SPAM ʟᴇᴀᴅꜱ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ .</b>\n
<i>Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ (ᴏʀ) ʀᴇᴘᴏʀᴛ ʙᴜɢꜱ</i> <b>: <a href='https://t.me/BotDuniaSupport'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>""",
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🏵 DEVELOPER ", url="https://github.com/EverythingSuckz")],
                [InlineKeyboardButton("🍺 FOLLOW ME ", url="https://github.com/EverythingSuckz")]
            ]
        )
    )
