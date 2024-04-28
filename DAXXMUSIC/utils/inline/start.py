from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, CallbackQuery
from pyrogram import filters

import config
from DAXXMUSIC import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"),
            InlineKeyboardButton(text=_["S_B_6"], callback_data="waifu"),     
        ],
    ]
    return buttons

@app.on_callback_query(filters.regex("waifu"))
async def waifu_callback(client: Client, callback_query: CallbackQuery):

    await callback_query.answer()

    # Send the help information for the "waifu" functionality
    help_text = """
    /guess: To Guess character (only works in group)
    /fav: Add Your fav
    /trade: To trade Characters
    /gift: Give any Character from Your Collection to another user.. (only works in groups)
    /collection: To see Your Collection
    /topgroups: See Top Groups.. Ppl Guesses Most in that Groups
    /top: Too See Top Users
    /ctop: Your ChatTop
    /changetime: Change Character appear time (only works in Groups)
    """
    await callback_query.message.reply_text(help_text)
