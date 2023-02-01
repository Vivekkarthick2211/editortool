# import moviepy.editor as mp
# from pysrt.srtitem import SubRipItem
# from pysrt.srtfile import SubRipFile

# # Load the video file
# video = mp.VideoFileClip("happybirthday.mp4")

# # Create a new SubRipFile
# subs = SubRipFile()

# # Add a new SubRipItem
# item = SubRipItem()
# item.text = "This is some new text"
# item.start.seconds = 10
# item.end.seconds = 15
# subs.append(item)

# # Save the SubRipFile
# subs.save("subs.srt")

# print(subs)
# # Add the SubRipFile to the video file
# video_with_subs = video.set_sub(subs)

# # Save the new video file
# video_with_subs.write_videofile("video_with_subs.mp4")

# from moviepy.editor import VideoFileClip, TextClip

# # Load the video file
# video = VideoFileClip("happybirthday.mp4")

# text = TextClip("Hello, World!", fontsize=70, color='red')

# text = text.set_pos('center')

# text = text.set_duration(5)

# result = video.overlay(text)

# result.write_videofile("output.mp4")
from django.contrib.auth.models import User

# from users.models import UserHistory, myUser
# from users.serialisers import UserHistorySerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

from users.models import UserHistory
from users.serialisers import UserHistorySerializer
class processingvideo(APIView):
# Load the video file
    def post(self, request, format=None):
       
        video = VideoFileClip("C:\\Users\\VivekKarthickS\\python\\django-examples\\files\\WhatsApp.mp4")
        title=request.data['VideoTitle']
        # Create a TextClip with the text to add to the video
        text = TextClip(request.data['message'], font="Amiri-Bold", kerning = 5,fontsize=75, color='#006D5B')

        text1 = TextClip(request.data['sub_message'], font='SCRIPTIFY',fontsize=75, color='#FF1493')
        foraudioend=video.duration
        positionsarray=request.data['textposstartend'].split(",")
        # for k in positionsarray:
        print(positionsarray[0].split("-")[0])
        start_time=0
        start_time2 = positionsarray[0].split("-")[0]
        end_time = positionsarray[0].split("-")[1]
        star_another=positionsarray[1].split("-")[0]
        end_another=positionsarray[1].split("-")[1]
        text = text.set_start(start_time2).set_end(end_time).set_pos('center')
        text1=text1.set_start(star_another).set_end(end_another).set_pos('center')
        video_with_audio_bg = video.set_audio(AudioFileClip("C:\\Users\\VivekKarthickS\\python\\django-examples\\files\\audio.mpeg"))
        audio_1=video_with_audio_bg.subclip(start_time, start_time + foraudioend)
        video_with_text = CompositeVideoClip([video,audio_1])

        another_video=CompositeVideoClip([video_with_text,text,text1])
        # video_with_text = mp.CompositeVideoClip([video, text])
        # Save the new video file
        another_video.write_videofile("C:\\Users\\VivekKarthickS\\python\\django-examples\\editorTool\\output\\"+title+".mp4")
        dictnew={}
        # for key,val in request.data.items():
        #     if key=='video':
        #         fss = FileSystemStorage()
        #         file = fss.save("edit", video)
        #         file_url = fss.url(file)
        # serializer = UserHistorySerializer(data=snippets, many=True)
        return Response({"status":status.HTTP_200_OK,"Message":"Video Processed Successfully !"})
# import cv2
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
# # Open the video file
# video = cv2.VideoCapture("DADbday.mp4")

# # Set the start frame
# start_frame = 100
# video.set(1, start_frame)

# # Read the frame
# success, frame = video.read()

# # Check if the frame was read successfully
# if success:
#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Extract text from the image
#     text = pytesseract.image_to_string(gray)

# # Close the video file
# video.release()

# # Print the extracted text
# print(text)