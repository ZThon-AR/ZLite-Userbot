from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , InlineQuery ,Message, CallbackQuery, InlineQueryResultPhoto, User
from pyrogram import filters, Client
from pyrogram.types import Message
import re
from helpers.SQL.pmstuff import givepermit, checkpermit, blockuser, getwarns, allallowed, allblocked, inwarns, addwarns
from main import SUDO_USERS as Adminsettings, LOG_GROUP
from handlers.help import *
from main import ALIVE_PIC

Alive_msg = f"π©πππππΎπ πππΏππππ - π·π΄ πΊπ¬πͺπΌπΉπ°π»ππͺ\n"
Alive_msg = f"βββββββββπππΏβββββββββ\n"
Alive_msg += f"β **ΩΩΨ±Ψ­Ψ¨ΩΨ§Ω ΨΉΩΨ²ΩΩΨ²Ω**β\n\n"
Alive_msg += f"**β€Ά Ψ§ΩΨ§ ΩΨ΄ΨΊΩΩΩ Ψ­ΩΨ§ΩΩΨ§Ω ΩΨ§ ΨͺΩΩΩ Ψ¨Ψ§Ψ²ΨΉΩΨ§Ψ¬Ω ΩΨ§ΩΨ§ Ψ³ΩΩΩ ΩΨͺΩ Ψ­ΨΈΩΨ±Ω ΨͺΩΩΩΨ§Ψ¦ΩΨ§Ω.....**\n\n"
Alive_msg += f"**β€Ά ΩΩΨ· ΩΩ Ψ³Ψ¨Ψ¨ ΩΨ¬ΩΨ¦Ω ΩΨ§ΩΨͺΨΈΩΨ± Ψ§ΩΩΨ±Ψ― β³**\n\n"
Alive_msg += f"βββββββββπππΏβββββββββ\n\n"

@Client.on_message(~filters.me & filters.private & ~filters.bot & filters.incoming , group = 69)
async def alive(client: Client, e: Message):
  message = e
  if checkpermit(message.chat.id):
        print("sql is cringe here")
        return
  else:
    print("gotit")
    addwarns(message.chat.id)
    gw= getwarns(message.chat.id)
    teriu= message.from_user
    teriun= teriu.id
    teriuni= str(teriun)
    teriunia="aprv_"+teriuni
    teriunid="decine_"+teriuni
    ids = 0
  if isinstance(gw , str):
      sb= await client.get_me()
      un= LOG_GROUP
  else:
      keyboard= InlineKeyboardMarkup([  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Approve",
                        callback_data=teriunia
                    ),
                    InlineKeyboardButton(
                        "Decline",
                        callback_data=teriunid
                    ),
                ])
      await message.reply_photo(photo=ALIVE_PIC, caption=Alive_msg)
      if gw==3:
        await message.reply_text("**β€Ά ΩΩΩΨ― Ψ­ΩΨ°Ψ±ΨͺΩΩΪͺ ΩΩΨ³ΩΨ¨ΩΩΩΨ§Ω ΩΩΩ ΨͺΩΪͺΩΨ±Ψ§Ψ± Ψ§ΩΩΨ±Ψ³ΩΨ§Ψ¦ΩΩ ...**\n**β€Ά ΨͺΩΩ Ψ­ΩΨΈΩΨ±Ϊͺ ΨͺΩΩΩΨ§Ψ¦ΩΩΨ§Ω π·.** \n**β€Ά Ψ§ΩΩΩ Ψ§Ω ΩΩΨ§ΨͺΩΩ ΩΩΨ§ΩΩΪͺ Ψ§ΩΩΨ­ΩΨ³ΩΨ§Ψ¨ π**")
        await client.block_user(message.from_user.id)
        blockuser(message.from_user.id)
        return


@Client.on_message(filters.command(["Ψ³ΩΨ§Ψ­", "Ψ³", "ΩΨ¨ΩΩ"], ["."]) & filters.me & filters.private)
async def refet(client: Client, message: Message):
    givepermit(message.chat.id)
    await message.edit_text("**ββ?ΨͺΩΩ Ψ§ΩΨ³ΩΩΩΨ§Ψ­ ΩΩΩ Ψ¨ΩΨ₯Ψ±Ψ³ΩΨ§Ω Ψ§ΩΩΨ±Ψ³ΩΨ§Ψ¦ΩΩ ΩΩΩΨ§ π¬β**")
    
     
@Client.on_message(filters.command(["Ψ±ΩΨΆ", "dap", "Ψ±", "disapprove", "dp"], ["."]) & filters.me & filters.private)
async def refes(client: Client, message: Message):
    await message.edit_text("**ββ?ΨͺΩΩ Ψ±ΩΨΆΩΩ ΩΩΩ Ψ₯Ψ±Ψ³ΩΨ§Ω Ψ§ΩΩΨ±Ψ³ΩΨ§Ψ¦ΩΩ ΩΩΩΨ§ π¬β**")
    blockuser(message.chat.id)
    await client.block_user(message.chat.id)
    
@Client.on_message(filters.command(["allpermitted", "Ψ§ΩΩΩΨ¨ΩΩΩΩ"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = allallowed()
  strr ="**ββ?ΩΩΨ§Ψ¦ΩΩΨ© Ψ§ΩΨ³ΩΩΨ§Ψ­ :**"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)

@Client.on_message(filters.command(["Ψ§ΩΩΨ±ΩΩΨΆΩΩ"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = allblocked()
  strr ="**ββ?ΩΩΨ§Ψ¦ΩΩΨ© Ψ§ΩΩΨ±ΩΩΩΨΆΩΩ :**"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)

@Client.on_message(filters.command(["nonpermitted"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = inwarns()
  strr ="**ββ?ΩΩΨ§Ψ¦ΩΩΨ© Ψ§ΩΨΊΩΨ± ΩΨ±ΩΩΨΆΩΩ Ψ¨ΨΉΩΨ― :**"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)


add_command_help(
    "Ψ­ΩΨ§ΩΨ© Ψ§ΩΨ?Ψ§Ψ΅",
    [
        [
            ".ap",
            "To Approve A User in Your Pm",
        ],
        [
            ".dap",
            "To Disapprove/Block A User in Your Pm",
        ],
        [
            ".approvedlist",
            "Get approved Users list",
        ],
        [
            ".allblocked",
            "Get blocked list",
        ],
        [
            ".nonpermitted",
            "non permitted list",
        ],
    ],
)
