from pyrogram import Client, filters
from DAXXMUSIC import app 

delete_links_enabled = False  # Variable to store the status of link deletion

@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_links(client, message):
    if delete_links_enabled and any(link in message.text for link in ["http", "https", "www."]):
        await message.delete()

@app.on_message(filters.command("linktoggle") & filters.me)
async def toggle_delete_links(client, message):
    global delete_links_enabled
    delete_links_enabled = not delete_links_enabled
    status = "on" if delete_links_enabled else "off"
    await message.reply(f"Link deletion is now {status}.")
