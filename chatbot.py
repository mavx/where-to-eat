from telepot.loop import MessageLoop
from database import Query
import apiChat # This connects to api.ai
import telepot
import time
import sys

q = Query('dataset/df.csv')
print('Initialized dataset.')

TOKEN = sys.argv[1] # AVOID PUTTING TOKENS IN CODE
bot = telepot.Bot(TOKEN)
me = bot.getMe()
print('Initialized bot: {}'.format(me.get('username')))

def handle(msg):
    """Handle messages received by bot"""
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        # bot.sendMessage(chat_id, msg['text'])

        # Send request to API.AI
        response = apiChat.googleAPI(msg['text'])

        # Parse results
        req_name = response.get('name', '')
        req_rating = response.get('Ratings', '')

        if isinstance(req_name, list):
            req_name = ' '.join(req_name)
        
        if isinstance(req_rating, list):
            req_rating = min(req_rating)

        # Query database with structured params
        print(req_name, req_rating)
        bot.sendMessage(
            chat_id, 
            'Searching...{}'.format(','.join([req_name, req_rating]))
        )
        results = q.query(req_name, req_rating)

        # Return results to user
        if results:
            for item in results:
                bot.sendMessage(chat_id, str(item))
        else:
            bot.sendMessage(chat_id, 'No results :(')

def main():
    MessageLoop(bot, handle).run_as_thread()
    print('Listening...')

    while 1:
        time.sleep(10)
    print('I am done.')

if __name__ == '__main__':
    main()
