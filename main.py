import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from get_links import go_to_page
from private_info import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

WEB_SITE = 'https://youglish.com/'
NUMBER_OF_VIDEOS: int = 1


# def find_phrase(phrase: str):
#     lowercased_phrase = phrase.lower()
#     result = go_to_page(lowercased_phrase)
#
#     return result


# -- commands of the bot -- #######################################################################################

async def show_video_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return

    key_phrase = ' '.join(context.args)
    key_phrase.lower()
    await update.message.reply_text(f'Searching the links with phrase: "{key_phrase.upper()}"...')

    # тут перевірити, чи користувач ввів запит
    if len(context.args) == 0:
        await update.message.reply_text('Please enter a phrase: /phrase <your phrase>')
        return

    result = go_to_page(WEB_SITE, key_phrase, NUMBER_OF_VIDEOS)
    await update.message.reply_text(f'Here are the videos with your phrase "{key_phrase.upper()}"')
    await update.message.reply_text(result)


### --- MAIN --- #################################################################################################

def main():
    application = Application.builder().token(TOKEN).build()

    # commands
    application.add_handler(CommandHandler('phrase', show_video_link))

    print('Polling...')
    application.run_polling(poll_interval=2)


if __name__ == '__main__':
    main()
