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
        self.Merge = Tkinter.Button(self.Menu, text = "Merge both", command = self.Both)
        ##Shows video button##
        self.Video.pack()
        ##Shows audio button##
        self.Audio.pack()
        ##shows merge button##
        self.Merge.pack()
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
    ##Audio menu##
    def Audio(self):
        ##uses tkinterface##
        self.Audio = Tkinter.Tk()
        ##button to take audio from video##
        self.Take = Tkinter.Button(self.Audio, text = "Take Audio from Video", command = self.TakeA)
        ##shows the button##
        self.Take.pack()
    ##Merge both audio and video menu##
    def Both(self):
        ##uses tkinterface##
        self.Both = Tkinter.Tk()
        ##button for merging both video and audio##
        self.Merge = Tkinter.Button(self.Both, text = "Merge", command = self.Merge)
        ##shows the button##
        self.Merge.pack()
    ##Does the process of merging##
    def Merge(self):
        ##goes to desktop##
        subprocess.call("cd Desktop", shell = True)
        ##gets video and audio##
        subprocess.call("ffmpeg -i son.wav -i video_origine.avi video_finale.mpg", shell = True)
    ##Takes an image from a video##
    def TakeI(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##at 15 seconds it takes the image from a video##
        subprocess.call("ffmpeg -ss 00:00:05 -i video2.mp4 -vf scale=800:-1 -vframes 1 img.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:10 -i video2.mp4 -vf scale=800:-1 -vframes 1 img1.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:12 -i video2.mp4 -vf scale=800:-1 -vframes 1 img2.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:14 -i video2.mp4 -vf scale=800:-1 -vframes 1 img3.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:16 -i video2.mp4 -vf scale=800:-1 -vframes 1 img4.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:18 -i video2.mp4 -vf scale=800:-1 -vframes 1 img5.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:20 -i video2.mp4 -vf scale=800:-1 -vframes 1 img6.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:22 -i video2.mp4 -vf scale=800:-1 -vframes 1 img7.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:24 -i video2.mp4 -vf scale=800:-1 -vframes 1 img8.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:26 -i video2.mp4 -vf scale=800:-1 -vframes 1 img9.jpg", shell = True)
        subprocess.call("ffmpeg -ss 00:00:28 -i video2.mp4 -vf scale=800:-1 -vframes 1 img10.jpg", shell = True)
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
    ##makes video from images##
    def MakeV(self):
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##takes images and makes video##
        subprocess.call("ffmpeg -f img, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10 -i image%d.jpg video.mpg", shell = True)
    

##connects the gui and manipulation##
mygui = Manipulation()
