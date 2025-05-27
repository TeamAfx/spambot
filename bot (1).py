import requests
import telebot

BOT_TOKEN = '7685990670:AAEtfFoetE7Fx37imh7AzHkak-attO6eGuc'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(msg):
    bot.reply_to(msg, """🔥 *WELCOME TO SPAM ZONE*  
Type: `/spam UID` to send ʀᴀᴘɪᴅ ꜱᴘᴀᴍ ʀᴇǫᴜᴇꜱᴛꜱ!

⚡ POWERED BY: *@TEAM AFX*  
👑 Created by: *@TEAM AFX OWNER*""", parse_mode="Markdown")

@bot.message_handler(commands=['spam'])
def spam_cmd(msg):
    try:
        args = msg.text.split()
        if len(args) != 2:
            bot.reply_to(msg, "⚠️ Correct format: `/spam UID`\nTry again, soldier of AFX.", parse_mode="Markdown")
            return
        
        uid = args[1]
        bot.reply_to(msg, f"⏳ Fetching data for UID: `{uid}`...\n\n🔥 Sit back, *TEAMAFX* in action!", parse_mode="Markdown")

        # PLAYER INFO
        info_api = f"https://dev-info-8kul.vercel.app/api/player-info?id={uid}&key=DEV007"
        info_res = requests.get(info_api)
        if info_res.status_code != 200 or info_res.json().get("status") != "success":
            bot.reply_to(msg, "❌ Info API failed. ALONE team will fix soon.", parse_mode="Markdown")
            return

        name = info_res.json()["data"]["basic_info"].get("name", "Unknown")

        # SPAM API
        spam_api = f"https://free-spam-dev-ayjm.vercel.app/send_requests?uid={uid}"
        spam_res = requests.get(spam_api)
        if spam_res.status_code != 200:
            bot.reply_to(msg, "❌ Spam API failed. Our server might be overloaded.", parse_mode="Markdown")
            return

        spam_data = spam_res.json()
        success = spam_data.get("success_count", 0)
        failed = spam_data.get("failed_count", 0)

        if success == 0:
            bot.reply_to(
                msg,
                f"🚫 *{name}*'s request list is already full!\n🆔 UID: `{uid}`\nTry again later soldier.",
                parse_mode="Markdown"
            )
        else:
            bot.reply_to(
                msg,
                f"✅ *{success}* Spam Requests Sent!\n❌ Failed: {failed}\n\n🎖️ Player: *{name}*\n🆔 UID: `{uid}`\n\n⚡ _POWERED BY DEV LEGEND NETWORK_",
                parse_mode="Markdown"
            )

    except Exception as e:
        bot.reply_to(msg, f"❌ Error:\n`{str(e)}`\n\n— Report to *@TEAMAFXOWNER*", parse_mode="Markdown")

print("🔥 AFX SPAM BOT ONLINE — POWERED BY @TEAMAFXOWNER")
bot.polling()