import os
from pyrogram import Client, filters

bot_token = os.environ["BOT_TOKEN"]
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

ChuPeepsBot = Client(
    "ChuPeepsBot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash
)

CHU_USERS = list(set(int(x) for x in os.environ.get("CHU_USERS", "").split()))
CHU_CHAT_ID = list(x for x in os.environ.get("CHU_CHAT_ID", "").replace("\n", " ").split(' '))


@Client.on_message(filters.chat(CHU_USERS) & ~filters.command("start"))
async def ChuPeepsForward(bot, update):
    if len(CHU_USERS) == 0 or len(CHU_CHAT_ID) == 0 or update.chat.id not in CHU_USERS:
        return
    try:
        for chat_id in CHU_CHAT_ID:
                await update.forward(chat_id=chat_id)
    except Exception as error:
        print(error)

ChuPeepsBot.run()
