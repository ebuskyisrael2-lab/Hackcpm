import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 7449822610

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 Buy - Browse Sellers", callback_data="buy")],
        [InlineKeyboardButton("💰 Sell - Post Offer", callback_data="sell")],
        [InlineKeyboardButton("📊 My Deals", callback_data="mydeals")],
        [InlineKeyboardButton("🆘 Support", callback_data="support")]
    ]
    text = (
        "🚀 *Welcome to ELON CPM OPEN MARKET* 🚀\n\n"
        "The #1 Escrow Market for CPM Sellers & Buyers.\n\n"
        "✅ 100% Safe Escrow\n"
        "✅ Instant Settlement\n"
        "✅ No Scam\n\n"
        "Choose below:"
    )
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "buy":
        await query.edit_message_text("🛒 *Buy Section*\n\nSellers list coming soon. Type your budget: e.g `I need $500 Facebook CPM`", parse_mode="Markdown")
    elif query.data == "sell":
        await query.edit_message_text("💰 *Sell Section*\n\nPost your offer like this:\n`Platform: Facebook\nQuantity: $1000\nPrice: $50 per $100\nPayment: USDT`", parse_mode="Markdown")
    elif query.data == "mydeals":
        await query.edit_message_text("📊 You have no active deals yet.")
    else:
        await query.edit_message_text("🆘 Contact Admin @ElonCPM_Admin")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
