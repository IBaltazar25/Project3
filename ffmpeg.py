##Irving Baltazar##Adrian Maritinez##Cristian Galvan##
##Project 3/CST 205##
##botton imports the command prompt##
import subprocess
##bottom imports the interface##
import Tkinter
##bottom imports messages##
import tkMessageBox
##class for the manipulation project##
class Manipulation:
    ##startup menu##
    def __init__(self):
        ##uses tkinterface##
        self.Menu = Tkinter.Tk()
        ##video buton opens video menu##
        self.Video = Tkinter.Button(self.Menu, text = "Video", command = self.Video)
        ##Audio button opens audio menu##
        self.Audio= Tkinter.Button(self.Menu, text = "Audio", command = self.Audio)
        ##merge button opens merge menu##
        self.MergeB = Tkinter.Button(self.Menu, text = "Merge both", command = self.Both)
        ##Shows video button##
        self.Video.pack()
        ##Shows audio button##
        self.Audio.pack()
        ##shows merge button##
        self.MergeB.pack()
        ##Creates the GUI##
        Tkinter.mainloop()
    ##Video menu##
    def Video(self):
        ##uses tkinterface##
        self.Video = Tkinter.Tk()
        ##Button for taking images from video##
        self.Take = Tkinter.Button(self.Video, text = "Take Images from Video", command = self.TakeI)
        ##shows the button##
        self.Take.pack()
        ##Button for cutting video into smaller time frames##
        self.Cut = Tkinter.Button(self.Video, text = "Cut Video", command = self.CutV)
        ##shows the button##
        self.Cut.pack()
        ##button for making video from images##
        self.Make = Tkinter.Button(self.Video, text = "Make Video from Images", command = self.MakeV)
        ##shows the button##
        self.Make.pack()
         ##button for splitting video in two parts##
        self.Split = Tkinter.Button(self.Video, text = "Split video in two", command = self.SplitV)
        ##shows the button##
        self.Split.pack()
        ##button for making image to video##
        self.Make1 = Tkinter.Button(self.Video, text = "Make image into a video", command = self.MakeI)
        ##shows the button##
        self.Make1.pack()
        ##button for speeding up or slowing down video##
        self.SV = Tkinter.Button(self.Video, text = "Speed or slow down video", command = self.SVideo)
        ##shows the button##
        self.SV.pack()
        ##button for making video into a gif##
        self.Make2 = Tkinter.Button(self.Video, text = "Make image into gif", command = self.MakeG)
        ##shows the button##
        self.Make2.pack()
    ##Audio menu##
    def Audio(self):
        ##uses tkinterface##
        self.Audio = Tkinter.Tk()
        ##button to take audio from video##
        self.Take = Tkinter.Button(self.Audio, text = "Take Audio from Video", command = self.TakeA)
        ##shows the button##
        self.Take.pack()
        ##button for muting audio from video##
        self.Mute = Tkinter.Button(self.Audio, text = "Mute audio from video", command = self.MuteA)
        ##shows the button##
        self.Mute.pack()
        ##button for speeding up or slowing down audio##
        self.SA = Tkinter.Button(self.Audio, text = "Speed up or slow down audio", command = self.SAudio)
        ##shows the button##
        self.SA.pack()
        ##button for adding image to audio file##
        self.Add = Tkinter.Button(self.Audio, text = "Add image to audio ", command = self.AddI)
        ##shows the button##
        self.Add.pack()
    ##Merge both audio and video menu##
    def Both(self):
        ##uses tkinterface##
        self.Both = Tkinter.Tk()
        ##button for merging both video and audio##
        self.Merge = Tkinter.Button(self.Both, text = "Merge", command = self.MergeF)
        ##shows the button##
        self.Merge.pack()
    ##Does the process of merging##
    def MergeF(self):
        ##goes to desktop##
        subprocess.call("cd Desktop", shell = True)
        ##gets video and audio##
        subprocess.call("ffmpeg -i audio.mp3 -i video.mp4 finale.mp4", shell = True)
    ##Takes an image from a video##
    def TakeI(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##at 15 seconds it takes the image from a video##
        subprocess.call("ffmpeg -ss 00:00:05 -i video.mp4 -vf scale=800:-1 -vframes 1 img.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:10 -i video.mp4 -vf scale=800:-1 -vframes 1 img1.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:12 -i video.mp4 -vf scale=800:-1 -vframes 1 img2.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:14 -i video.mp4 -vf scale=800:-1 -vframes 1 img3.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:16 -i video.mp4 -vf scale=800:-1 -vframes 1 img4.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:18 -i video.mp4 -vf scale=800:-1 -vframes 1 img5.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:20 -i video.mp4 -vf scale=800:-1 -vframes 1 img6.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:22 -i video.mp4 -vf scale=800:-1 -vframes 1 img7.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:24 -i video.mp4 -vf scale=800:-1 -vframes 1 img8.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:26 -i video.mp4 -vf scale=800:-1 -vframes 1 img9.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:30 -i video.mp4 -vf scale=800:-1 -vframes 1 img10.jpg", shell = True)
    ##Takes audio from a video##
    def TakeA(self):
        ##searches the desktop##
        subprocess.call("cd Desktop", shell = True)
        ##does the process##
        subprocess.call("ffmpeg -i video.mp4 -vn -ab 256 audio.mp3", shell = True)
    ##cuts video into smaller clips##
    def CutV(self):
        ##searches the desktop##
        subprocess.call("cd Desktop", shell = True)
        ##makes 50 second videos##
        subprocess.call("ffmpeg -i video.mp4 -ss 00:00:50.0 -codec copy -t 20 output.mp4", shell = True)
        ##mutes the audio from a video and makes new video
    def MuteA(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##extracts the audio
        subprocess.call("ffmpeg -i video.mp4 -an mutevideo.mp4", shell = True)
    ##Takes a video and makes smaller clips
    def SplitV(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##splits video in two parts
        subprocess.call("ffmpeg -i video1.mp4 -t 00:01:30 -c copy part1.mp4 -ss 00:01:30 -codec copy part2.mp4", shell = True)
    ##Make image to video
    def MakeI(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##takes the image and makes a video
        subprocess.call("ffmpeg -loop 1 -i img.jpg -c:v libx264 -t 30 -pix_fmt yuv420p video5.mp4", shell = True)
        ##Slows dow or speeds up audio
    def SAudio(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##speeds up or slows the duration
        subprocess.call("ffmpeg -i audio.mp3 -filter:a atempo=2.0 -vn output.mp3", shell = True)
        ##speeds or slows the video
    def SVideo(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##speeds up or slows down video time 
        subprocess.call("ffmpeg -i video.mp4 -filter:v setpts=0.125*PTS output1.mp4", shell = True)
        ##add poster image to audio
    def AddI(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##takes image and adds it to audio
        subprocess.call("ffmpeg -loop 1 -i img.jpg -i audio.mp3 -c:v libx264 -c:a aac -strict experimental -b:a 192k -shortest output2.mp4", shell = True)
        ##Makes image to animated GIF
    def MakeG(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##takes an image and creates a GIF
        subprocess.call("ffmpeg -i video3.mp4 -vf scale=500:-1 -t 10 -r 10 image.gif", shell = True)
    

##connects the gui and manipulation##
mygui = Manipulation()
