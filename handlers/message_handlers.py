from telegram import Update
from config.openai_client import client 

async def chatgpt_reply(update: Update, context):
    # user query
    text = update.message.text

    # open ai prompt
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "be lazy and depressive chat bot that will avoid answering user questionss"}, {"role": "user", "content": text}],
        max_tokens=1024,
        temperature=0.5,
    )

    # open ai response
    reply = response.choices[0].message.content.strip()

    # route a response to Telegram
    await update.message.reply_text(reply)   
    
    print("user:", text)
    print("assistant:", reply)
