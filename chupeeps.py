import os
import asyncio
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_token = os.environ["BOT_TOKEN"]
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

ChuPeeps = Client(
    "ChuPeeps",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash
)

CHU_USERS = list(set(int(x) for x in os.environ.get("CHU_USERS", "").split()))
CHU_CHAT_ID = list(x for x in os.environ.get("CHU_CHAT_ID", "").replace("\n", " ").split(' '))


@ChuPeeps.on_message(filters.chat(CHU_USERS) & ~filters.command(["start", "help"]))
async def ChuPeepsForward(bot, update):
    if len(CHU_USERS) == 0 or len(CHU_CHAT_ID) == 0 or update.chat.id not in CHU_USERS:
        return
    try:
        for chat_id in CHU_CHAT_ID:
                await update.forward(chat_id=chat_id)
                await asyncio.sleep(15)
                await bot.send_sticker(chat_id=chat_id, CAACAgEAAx0ERyaUlQACRCdiWaamKvLC8nqECke4nVJ0S0tIPwACkQADizr_JDtGfCabJN7bHgQ)
    except Exception as error:
        print(error)

@ChuPeeps.on_message(filters.command("start"))
async def start(bot, update):
    await update.reply_text(
        text=JOIN_TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


WELCOME_ID = os.environ["WELCOME_ID"]

JOIN_TEXT = """Hello {} Welcome to ChuPeeps"""

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('ChuPeeps', url='https://telegram.me/ChuPeeps')]])


@ChuPeeps.on_message(filters.chat(WELCOME_ID) & filters.new_chat_members)
async def WelcometoChuPeeps(client, message):
    if message.from_user.is_bot:
        await chat.kick_member(message.from_user.id)
    else:
        await message.reply_text(
        text=JOIN_TEXT.format(message.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
        await asyncio.sleep(60)
        await message.delete()





ChuPeeps.run()
