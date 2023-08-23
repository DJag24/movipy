python
from telegram.ext import Updater, MessageHandler, Filters
from moviepy.editor import VideoFileClip, TextClip

python
def handle_message(update, context):
    # Get the received message
    message = update.message.text

    # Check if the message is a video file
    if update.message.video is not None:
        # Get the video file ID
        video_file_id = update.message.video.file_id

        # Download the video file
        video_file = context.bot.get_file(video_file_id)
        video_file.download('input_video.mp4')

        # Open the video file using MoviePy
        video = VideoFileClip('input_video.mp4')

        # Add text to the video
        text_clip = TextClip(message, fontsize=50, color='white')
        text_clip = text_clip.set_position('center').set_duration(video.duration)

        final_video = video.set_audio(None).set_duration(video.duration).set_fps(video.fps)
        final_video = final_video.set_mask(text_clip)

        # Save the modified video
        final_video.write_videofile('output_video.mp4', codec='libx264', audio_codec='aac')

        # Send the modified video back to the user
        context.bot.send_video(chat_id=update.effective_chat.id, video=open('output_video.mp4', 'rb'))


python
updater = Updater('6035704347:AAFe3bk_NeimNu6jKp6GFANMxbx2vAg68PY', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

python
updater.start_polling()

