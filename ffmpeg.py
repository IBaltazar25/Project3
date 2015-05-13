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
        oldtitle = self.Menu.title()
        ##this gives a title to the window##
        self.Menu.title('V.A.M')
        ##this this changes the size and spawn location of the window##
        self.Menu.geometry('200x150-850+400')
        ##video buton opens video menu##
        self.Video = Tkinter.Button(self.Menu, text = "Video", fg="yellow", bg="black", pady=10,padx=46, command = self.Video)
        ##Audio button opens audio menu##
        self.Audio= Tkinter.Button(self.Menu, text = "Audio", fg="yellow", bg="black", pady=10, padx=45, command = self.Audio)
        ##merge button opens merge menu##
        self.MergeB = Tkinter.Button(self.Menu, text = "Merge both", fg="yellow", bg="black", pady=10, padx=30, command = self.Both)
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
        ##this gives a title to the window##
        self.Video.title('V.A.M')
        ##this this changes the size and spawn location of the window##
        self.Video.geometry('260x290-550+400')
        ##Button for taking images from video##
        self.Take = Tkinter.Button(self.Video, text = "Take Images from Video",  fg="red", bg="green", pady=10, padx=25, command = self.TakeI)
        ##shows the button##
        self.Take.pack()
        ##Button for cutting video into smaller time frames##
        self.Cut = Tkinter.Button(self.Video, text = "Cut Video", fg="red", bg="green", pady=10, padx=63, command = self.CutV)
        ##shows the button##
        self.Cut.pack()
         ##button for splitting video in two parts##
        self.Split = Tkinter.Button(self.Video, text = "Split video in two", fg="red", bg="green", pady=10, padx=43.50, command = self.SplitV)
        ##shows the button##
        self.Split.pack()
        ##button for making image to video##
        self.Make1 = Tkinter.Button(self.Video, text = "Make image into a video", fg="red", bg="green", pady=10, padx=24, command = self.MakeI)
        ##shows the button##
        self.Make1.pack()
        ##button for speeding up or slowing down video##
        self.SV = Tkinter.Button(self.Video, text = "Speed up a video", fg="red", bg="green", pady=10, padx=45, command = self.SVideo)
        ##shows the button##
        self.SV.pack()
        ##button for making video into a gif##
        self.Make2 = Tkinter.Button(self.Video, text = "Make image into gif", fg="red", bg="green", pady=10, padx=36, command = self.MakeG)
        ##shows the button##
        self.Make2.pack()
    ##Audio menu##
    def Audio(self):
        ##uses tkinterface##
        self.Audio = Tkinter.Tk()
        ##this gives a title to the window##
        self.Audio.title('V.A.M')
        ##this this changes the size and spawn location of the window##
        self.Audio.geometry('300x200-1100+400')
        ##button to take audio from video##
        self.Take = Tkinter.Button(self.Audio, text = "Take Audio from Video",  fg="yellow", bg="red", pady=10, padx=45, command = self.TakeA)
        ##shows the button##
        self.Take.pack()
        ##button for muting audio from video##
        self.Mute = Tkinter.Button(self.Audio, text = "Mute audio from Video", fg="yellow", bg="red", pady=10, padx=45, command = self.MuteA)
        ##shows the button##
        self.Mute.pack()
        ##button for speeding up or slowing down audio##
        self.SA = Tkinter.Button(self.Audio, text = "Speed up an audio", fg="yellow", bg="red", pady=10, padx=56, command = self.SAudio)
        ##shows the button##
        self.SA.pack()
        ##button for adding image to audio file##
        self.Add = Tkinter.Button(self.Audio, text = "Add image to audio ", fg="yellow", bg="red", pady=10, padx=52, command = self.AddI)
        ##shows the button##
        self.Add.pack()
    ##Merge both audio and video menu##
    def Both(self):
        ##uses tkinterface##
        self.Both = Tkinter.Tk()
        ##this gives a title to the window##
        self.Both.title('V.A.M')
        ##this this changes the size and spawn location of the window##
        self.Both.geometry('200x70-850+270')
        ##button for merging both video and audio##
        self.Merge = Tkinter.Button(self.Both, text = "Merge", fg="blue", bg="white", pady=10, padx=45, command = self.MergeF)
        ##shows the button##
        self.Merge.pack()
    ##Does the process of merging##
    def MergeF(self):
        self.MergeFwindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.MergeFwindow.title('Merge')
        ##this changes the spawn location of the window##
        self.MergeFwindow.geometry('-780+150')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelMergeF = Tkinter.Label(self.MergeFwindow, text = "Choose a time to display an image from a video. (i.e. 00:00:01)")
        self.labelMergeF.pack()
        self.textEntryMergeF = Tkinter.Entry(self.MergeFwindow, width = 50)
        self.textEntryMergeF.pack()
        self.MergeFbutton = Tkinter.Button(self.MergeFwindow, text = "Enter", command = self.MergeFcommands)
        self.MergeFbutton.pack()
    def MergeFcommands(self):
        mergef = self.textEntry.get()
        ##goes to desktop##
        subprocess.call("cd Desktop", shell = True)
        ##gets video and audio##
        subprocess.call("ffmpeg -i audio.mp3 -i video.mp4 " + mergef + ".mp4", shell = True)
    ##Takes an image from a video##
    def TakeI(self):
        #creates new window##
        self.TakeIwindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.TakeIwindow.title('Take Image from Video')
        ##this changes the spawn location of the window##
        self.TakeIwindow.geometry('-175+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelTakeI = Tkinter.Label(self.TakeIwindow, text = "Choose a time to display an image from a video. (i.e. 00:00:01)")
        self.labelTakeI.pack()
        self.textEntryTakeI = Tkinter.Entry(self.TakeIwindow, width = 50)
        self.textEntryTakeI.pack()
        self.TakeIbutton = Tkinter.Button(self.TakeIwindow, text = "Enter", command = self.TakeIcommands)
        self.TakeIbutton.pack()
    ##Takes audio from a video##
    def TakeIcommands(self):
        takei = self.textEntryTakeI.get()
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##at 15 seconds it takes the image from a video##
        subprocess.call("ffmpeg -ss " + takei + " -i video.mp4 -vf scale=800:-1 -vframes 1 TakeI.jpg", shell = True)
    def TakeA(self):
        ##creates new window##
        self.TakeAwindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.TakeAwindow.title('Take Audio from Video')
        ##this changes the spawn location of the window##
        self.TakeAwindow.geometry('-1450+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelTakeA = Tkinter.Label(self.TakeAwindow, text = "Please enter the output file name.")
        self.labelTakeA.pack()
        self.textEntryTakeA = Tkinter.Entry(self.TakeAwindow, width = 50)
        self.textEntryTakeA.pack()
        self.TakeAbutton = Tkinter.Button(self.TakeAwindow, text = "Enter", command = self.TakeAcommands)
        self.TakeAbutton.pack()
    def TakeAcommands(self):
        takea = self.textEntryTakeA.get()
        ##searches the desktop##
        subprocess.call("cd Desktop", shell = True)
        ##does the process##
        subprocess.call("ffmpeg -i video.mp4 -vn -ab 256 " + takea + ".mp3", shell = True)
    ##cuts video into smaller clips##
    def CutV(self):
        ##creates new window##
        self.CutVwindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.CutVwindow.title('Cut Video')
        ##this changes the spawn location of the window##
        self.CutVwindow.geometry('-175+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelCutV = Tkinter.Label(self.CutVwindow, text = "Where do you wish to cut the video? (i.e. 00:02:50)")
        self.labelCutV.pack()
        self.textEntryCutV = Tkinter.Entry(self.CutVwindow, width = 50)
        self.textEntryCutV.pack()
        self.CutVbutton = Tkinter.Button(self.CutVwindow, text = "Enter", command = self.CutVcommands)
        self.CutVbutton.pack()
    def CutVcommands(self):
        cutv = self.textEntryCutV.get()
        ##searches the desktop##
        subprocess.call("cd Desktop", shell = True)
        ##makes 20 second videos##
        subprocess.call("ffmpeg -i video.mp4 -ss " + cutv + " -codec copy -t 20 CutV.mp4", shell = True)
        ##mutes the audio from a video and makes new video##
    def MuteA(self):
        ##creates new window##
        self.MuteAwindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.MuteAwindow.title('Mute Audio from video')
        ##this changes the spawn location of the window##
        self.MuteAwindow.geometry('-1450+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelMuteA = Tkinter.Label(self.MuteAwindow, text = "Please enter the output file name.")
        self.labelMuteA.pack()
        self.textEntryMuteA = Tkinter.Entry(self.MuteAwindow, width = 50)
        self.textEntryMuteA.pack()
        self.MuteAbutton = Tkinter.Button(self.MuteAwindow, text = "Enter", command = self.MuteAcommands)
        self.MuteAbutton.pack()
    def MuteAcommands(self):
        mutea = self.textEntryMuteA.get()
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##extracts the audio##
        subprocess.call("ffmpeg -i video.mp4 -an " + mutea + ".mp4", shell = True)
    ##Takes a video and makes smaller clips##
    def SplitV(self):
        ##creates new window##
        self.SplitVwindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.SplitVwindow.title('Split Video in two')
        ##this changes the spawn location of the window##
        self.SplitVwindow.geometry('-175+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelSplitV = Tkinter.Label(self.SplitVwindow, text = "Where do you wish to cut the video? (i.e. 00:02:50)")
        self.labelSplitV.pack()
        self.textEntrySplitV = Tkinter.Entry(self.SplitVwindow, width = 50)
        self.textEntrySplitV.pack()
        self.SplitVbutton = Tkinter.Button(self.SplitVwindow, text = "Enter", command = self.SplitVcommands)
        self.SplitVbutton.pack()
    def SplitVcommands(self):
        splitv = self.textEntrySplitV.get()
        splitv2 = self.textEntrySplitV.get()
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##splits video in two parts##
        subprocess.call("ffmpeg -i video.mp4 -t " + splitv + " -c copy splitvpart1.mp4 -ss " + splitv2 + " -codec copy splitvpart2.mp4", shell = True)
    ##Make image to video##
    def MakeI(self):
        ##creates new window##
        self.MakeIwindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.MakeIwindow.title('Make image into a video')
        ##this changes the spawn location of the window##
        self.MakeIwindow.geometry('-175+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelMakeI = Tkinter.Label(self.MakeIwindow, text = "Please enter the output file name.")
        self.labelMakeI.pack()
        self.textEntryMakeI = Tkinter.Entry(self.MakeIwindow, width = 50)
        self.textEntryMakeI.pack()
        self.MakeIbutton = Tkinter.Button(self.MakeIwindow, text = "Enter", command = self.MakeIcommands)
        self.MakeIbutton.pack()
    def MakeIcommands(self):
        makei = self.textEntryMakeI.get()
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##takes the image and makes a video##
        subprocess.call("ffmpeg -loop 1 -i img.jpg -c:v libx264 -t 30 -pix_fmt yuv420p " + makei + ".mp4", shell = True)
        ##Slows down or speeds up audio
    def SAudio(self):
        ##creates a new window##
        self.SAudiowindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.SAudiowindow.title('Speed up audio')
        ##this changes the spawn location of the window##
        self.SAudiowindow.geometry('-1450+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelSAudio = Tkinter.Label(self.SAudiowindow, text = "Please enter the output file name.")
        self.labelSAudio.pack()
        self.textEntrySAudio = Tkinter.Entry(self.SAudiowindow, width = 50)
        self.textEntrySAudio.pack()
        self.SAudiobutton = Tkinter.Button(self.SAudiowindow, text = "Enter", command = self.SAudiocommands)
        self.SAudiobutton.pack()
    def SAudiocommands(self):
        saudio = self.textEntrySAudio.get()
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##speeds up or slows the duration##
        subprocess.call("ffmpeg -i audio.mp3 -filter:a atempo=2.0 -vn " + saudio + ".mp3", shell = True)
        ##speeds or slows the video
    def SVideo(self):
        ##creates a new window##
        self.SVideowindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.SVideowindow.title('Speed up video')
        ##this changes the spawn location of the window##
        self.SVideowindow.geometry('-175+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelSVideo = Tkinter.Label(self.SVideowindow, text = "Please enter the output file name.")
        self.labelSVideo.pack()
        self.textEntrySVideo = Tkinter.Entry(self.SVideowindow, width = 50)
        self.textEntrySVideo.pack()
        self.SVideobutton = Tkinter.Button(self.SVideowindow, text = "Enter", command = self.SVideocommands)
        self.SVideobutton.pack()
    def SVideocommands(self):
        svideo = self.textEntrySVideo.get()
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##speeds up or slows down video time##
        subprocess.call("ffmpeg -i video.mp4 -filter:v setpts=0.125*PTS " + svideo + ".mp4", shell = True)
        ##add poster image to audio
    def AddI(self):
        ##creates a new window##
        self.AddIwindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.AddIwindow.title('Add Image to Audio')
        ##this changes the spawn location of the window##
        self.AddIwindow.geometry('-1450+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelAddI = Tkinter.Label(self.AddIwindow, text = "Please enter the output file name.")
        self.labelAddI.pack()
        self.textEntryAddI = Tkinter.Entry(self.AddIwindow, width = 50)
        self.textEntryAddI.pack()
        self.AddIbutton = Tkinter.Button(self.AddIwindow, text = "Enter", command = self.AddIcommands)
        self.AddIbutton.pack()
    def AddIcommands(self):
        addi = self.textEntryaddi.get()
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##takes image and adds it to audio##
        subprocess.call("ffmpeg -loop 1 -i img.jpg -i audio.mp3 -c:v libx264 -c:a aac -strict experimental -b:a 192k -shortest " + addi + ".mp4", shell = True)
        ##Makes image to animated GIF##
    def MakeG(self):
        ##creates a new window##
        self.MakeGwindow = Tkinter.Tk()
        ##this gives a title to the window##
        self.MakeGwindow.title('Make image into gif')
        ##this changes the spawn location of the window##
        self.MakeGwindow.geometry('-175+400')
        ##Creates a new label, button, and a text entry box to allow for user input##
        self.labelMakeG = Tkinter.Label(self.MakeGwindow, text = "Please enter the output file name.")
        self.labelMakeG.pack()
        self.textEntryMakeG = Tkinter.Entry(self.MakeGwindow, width = 50)
        self.textEntryMakeG.pack()
        self.MakeGbutton = Tkinter.Button(self.MakeGwindow, text = "Enter", command = self.MakeGcommands)
        self.MakeGbutton.pack()
    def MakeGcommands(self):
        makeg = self.textEntryMakeG.get()
        ##searches desktop##
        subprocess.call("cd Desktop", shell = True)
        ##takes an image and creates a GIF##
        subprocess.call("ffmpeg -i gifvideo.mp4 -vf scale=500:-1 -t 10 -r 10 " + makeg + ".gif", shell = True)

##connects the gui and manipulation##
mygui = Manipulation()
