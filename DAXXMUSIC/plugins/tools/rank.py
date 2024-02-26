from pyrogram import filters
from pymongo import MongoClient
from DAXXMUSIC import app
from config import MONGO_DB
from pyrogram.types import *


# Connect to MongoDB
mongo_client = MongoClient("your_mongo_db_uri")
db = mongo_client["natu_rankings"]
collection = db["ranking"]

# Store today's and user data
today = {}
user_data = {}

# Default profile picture
pic = "https://telegra.ph/file/895fb19771f4c6bfc0607.jpg"


# Watcher functions
@app.on_message(filters.group & filters.group, group=6)
def today_watcher(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    today.setdefault(chat_id, {}).setdefault(user_id, {"total_messages": 0})
    today[chat_id][user_id]["total_messages"] += 1


@app.on_message(filters.group & filters.group, group=11)
def _watcher(_, message):
    user_id = message.from_user.id
    user_data.setdefault(user_id, {}).setdefault("total_messages", 0)
    user_data[user_id]["total_messages"] += 1
    collection.update_one({"_id": user_id}, {"$inc": {"total_messages": 1}}, upsert=True)


# Ranks functions
def get_top_users(chat_id, data, limit=10):
    users_data = [(user_id, user_data["total_messages"]) for user_id, user_data in data[chat_id].items()]
    sorted_users_data = sorted(users_data, key=lambda x: x[1], reverse=True)[:limit]
    return sorted_users_data


def get_user_link(user_id):
    try:
        user_name = app.get_users(user_id).first_name
        return f"[{user_name}](https://t.me/{user_name})"
    except:
        return "Unknown"


def generate_leaderboard_caption(title, data):
    response = f"**📈 LEADERBOARD {title}**\n"
    for idx, (user_id, total_messages) in enumerate(data, start=1):
        user_link = get_user_link(user_id)
        user_info = f"**{idx}**. {user_link} • {total_messages}\n"
        response += user_info
    return response


@app.on_message(filters.command("today"))
async def today_leaderboard(_, message):
    chat_id = message.chat.id
    if chat_id in today:
        sorted_users_data = get_top_users(chat_id, today)

        if sorted_users_data:
            response = generate_leaderboard_caption("TODAY", sorted_users_data)
            button = InlineKeyboardMarkup([[InlineKeyboardButton("OVERALL", callback_data="overall")]])
            await message.reply_photo(photo=pic, caption=response, reply_markup=button, parse_mode='markdown')
        else:
            await message.reply_text("No data available for today.")
    else:
        await message.reply_text("No data available for today.")


@app.on_message(filters.command("ranking"))
async def overall_leaderboard(_, message):
    top_members = collection.find().sort("total_messages", -1).limit(10)
    sorted_users_data = [(member["_id"], member["total_messages"]) for member in top_members]

    response = generate_leaderboard_caption("OVERALL", sorted_users_data)
    button = InlineKeyboardMarkup([[InlineKeyboardButton("TODAY", callback_data="today")]])
    await message.reply_photo(photo=pic, caption=response, reply_markup=button, parse_mode='markdown')


# Callback query functions
@app.on_callback_query(filters.regex("today"))
async def today_rank(_, query):
    chat_id = query.message.chat.id
    if chat_id in today:
        sorted_users_data = get_top_users(chat_id, today)

        if sorted_users_data:
            response = generate_leaderboard_caption("TODAY", sorted_users_data)
            button = InlineKeyboardMarkup([[InlineKeyboardButton("OVERALL", callback_data="overall")]])
            await query.message.edit_text(response, reply_markup=button, parse_mode='markdown')
        else:
            await query.answer("No data available for today.")
    else:
        await query.answer("No data available for today.")


@app.on_callback_query(filters.regex("overall"))
async def overall_rank(_, query):
    top_members = collection.find().sort("total_messages", -1).limit(10)
    sorted_users_data = [(member["_id"], member["total_messages"]) for member in top_members]

    response = generate_leaderboard_caption("OVERALL", sorted_users_data)
    button = InlineKeyboardMarkup([[InlineKeyboardButton("TODAY", callback_data="today")]])
    await query.message.edit_text(response, reply_markup=button, parse_mode='markdown')


# Run the app
