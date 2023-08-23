import telegram
import moviepy.editor as mp

bot = telegram.Bot(token='6035704347:AAFe3bk_NeimNu6jKp6GFANMxbx2vAg68PY')

def handle_message(message):
    # Get the text of the message
    text = message.text
    
    # Create a new video using MoviePy
    clip = mp.VideoFileClip("path/to/your/video.mp4")
    new_clip = clip.subclip(0, 5)
    
    # Save the new video to a file
    new_clip.write_videofile("path/to/your/new_video.mp4")
    
    # Send the new video back to the user
    bot.send_video(chat_id=message.chat_id, video=open("path/to/your/new_video.mp4", "rb"))


from telegram.ext import MessageHandler, Filters

message_handler = MessageHandler(Filters.text, handle_message)
bot.dispatcher.add_handler(message_handler)
