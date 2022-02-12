from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('Support', url='t.me/ENG_Bahaa_Mohammed'),
            InlineKeyboardButton('Source', url='github.com/')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Support', url='t.me/ENG_Bahaa_Mohammed'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
