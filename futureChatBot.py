import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def future():
    import random
    import os
    input_data = random.randrange(1, 3235, 4)
    count = 0
    path = "C:\\Users\\Admin\\"
    result = []
    kieu_path = os.path.join(path, "BoiKieu.txt")
    with open(kieu_path, encoding ="UTF-8") as f:
        for line in f:
            if count > input_data - 4:
                result.append(line)
                if count == input_data:
                    break
            count +=1
    return ''.join(result)

presentation_text = """
Stay confident in your decisions with FutureBot. 
This chatbot will use a few random sentences from the story of Kieu to talk about the problem you are facing. Just think about it!
From The Tale of Kieu - Author: Nguyen Du
Bot Creator/Idea: Long Ngo Hai - from Pymi.Vn
If you have any idea. Free to ask me in Linked In

Type /xemboi to give an answer for your question
Type /info to give more information about this storyu
"""

info_text = """
The Vietnamese tradition of poetry and music captures the indomitable spirit of the people — a spirit that seems equal to any adversity. The quintessential example of this tradition — characterized by a complex blending of Chinese and Vietnamese elements — is an epic poem, "Truyên Kiêu," or the "Tale of Kiêu." This masterpiece, ranking with the greatest achievements of Asian and world literature, was written by Nguyen Du in the second decade of the nineteenth century. It is a creative transformation of an obscure Chinese story that has become a national classic — known and loved by all Vietnamese.
Kiêu, a young, newly betrothed woman, sells herself into prostitution to ransom her father from the clutches of a mandarin and a merchant who have conspired to ruin him. Having paid for her father's release, Kiêu endures a series of misfortunes, injustices, and degradations for the next fifteen years, before she is finally restored to her family. When her ordeal is over, she commits herself to a life of chastity. Her great talents as a lutenist and songstress sustain her spirits through a number of trials. Typically, Vietnamese editions of the epic poem show a young girl, cradling a lute, under a full moon. The moon symbolizes a mirror in which separated loved ones are able to see each other. Through these symbols — the chaste prostitute, the lute, and the full moon — the "Tale of Kiêu" expresses the determination to endure, to preserve a hardy and cul- tured humanity, and thereby to master even the cruelest destiny.
"""
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=presentation_text)
# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
async def xemboi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #text_caps = ' '.join(context.args).upper()
    text_caps = future()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = info_text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=info_text)

async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

if __name__ == '__main__':
    application = ApplicationBuilder().token('6206979072:AAGsMjLCpZS6vJ8VKiv_A_x3ec-auMvdI9k').build()

    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    start_handler = CommandHandler('start', start)
    # echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('xemboi', xemboi)
    info_handler = CommandHandler('info', info)

    inline_caps_handler = InlineQueryHandler(inline_caps)
    application.add_handler(inline_caps_handler)
    application.add_handler(start_handler)
    # application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(info_handler)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    application.run_polling()