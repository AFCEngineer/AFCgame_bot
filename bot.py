import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from utils.game_utils import generate_deck

from utils.redis_utils import save_game, load_game, delete_game


# Replace all `active_games[chat_id]` with:
game = load_game(chat_id)  # Load from Redis
save_game(chat_id, game)   # Save after updates
delete_game(chat_id)       # When game ends
# Initialize bot
app = Application.builder().token(os.getenv("BOT_TOKEN")).build()

# Add handlers (same as previous code snippets)
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("newgame", new_game))
app.add_handler(CommandHandler("join", join_game))
app.add_handler(CommandHandler("startgame", start_game))
app.add_handler(CallbackQueryHandler(play_card, pattern="^play_"))

if __name__ == "__main__":
    app.run_polling()
