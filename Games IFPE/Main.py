from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pickle
import os

userName = ''
tempdir = ''


def window():

    global userName, tempdir

    # ----------------- Getting Name From File -------------------
    file = open("user.dat", "rb")
    userName = pickle.load(file)
    print(userName)
    file.close()
    file = open("user.dat", "wb")
    blank = ""
    pickle.dump(blank, file)
    file.close()

    def lol():
        # ----------------- Configuring Window to LOL -------------------
        imageLabel.place_forget()
        csImageLabel.place_forget()
        minecraftImageLabel.place_forget()
        smiteImageLabel.place_forget()
        fibonniroImageLabel.place_forget()
        internLabel.place_forget()
        intern2Label.place_forget()
        intern3Label.place_forget()
        intern4Label.place_forget()

        lolImageLabel.place(x=-2, y=-2)

        playButton.place(x=650, y=500)

        getDirectoryButton.place(x=650, y=530)

    def cs():
        # ----------------- Configuring Window to CS -------------------
        imageLabel.place_forget()
        lolImageLabel.place_forget()
        minecraftImageLabel.place_forget()
        smiteImageLabel.place_forget()
        fibonniroImageLabel.place_forget()
        internLabel.place_forget()
        intern2Label.place_forget()
        intern3Label.place_forget()
        intern4Label.place_forget()

        csImageLabel.place(x=-2, y=-2)

        playButton.place(x=650, y=500)

        getDirectoryButton.place(x=650, y=530)

    def minecraft():
        # ----------------- Configuring Window to Minecraft -------------------
        imageLabel.place_forget()
        lolImageLabel.place_forget()
        csImageLabel.place_forget()
        smiteImageLabel.place_forget()
        fibonniroImageLabel.place_forget()
        internLabel.place_forget()
        intern2Label.place_forget()
        intern3Label.place_forget()
        intern4Label.place_forget()

        minecraftImageLabel.place(x=-150, y=-2)

        playButton.place(x=650, y=500)

        getDirectoryButton.place(x=650, y=530)

    def smite():
        # ----------------- Configuring Window to Smite -------------------
        imageLabel.place_forget()
        lolImageLabel.place_forget()
        csImageLabel.place_forget()
        minecraftImageLabel.place_forget()
        fibonniroImageLabel.place_forget()
        internLabel.place_forget()
        intern2Label.place_forget()
        intern3Label.place_forget()
        intern4Label.place_forget()

        smiteImageLabel.place(x=-150, y=-2)

        playButton.place(x=650, y=500)

        getDirectoryButton.place(x=650, y=530)

    def fibonniro():
        # ----------------- Configuring Window to Fibonniro -------------------
        imageLabel.place_forget()
        lolImageLabel.place_forget()
        csImageLabel.place_forget()
        minecraftImageLabel.place_forget()
        smiteImageLabel.place_forget()
        playButton.place_forget()
        getDirectoryButton.place_forget()

        fibonniroImageLabel.place(x=-2, y=-2)

        internLabel["text"] = "Fibonniro"
        internLabel.place(x=260, y=20)

        intern2Label["text"] = "Gotta Go Fast!!!"
        intern2Label.place(x=180, y=90)

        intern3Label["text"] = "In Development by Alex and Henrique"
        intern3Label.place(x=165, y=480)

        intern4Label["text"] = "A project being supported by the community, with a total of 0 supporters"
        intern4Label.place(x=210, y=550)

    def play():

        global tempdir
        # ----------------- Executing the Path From the Game -------------------
        os.system(tempdir)

    def getdirectory():

        global tempdir
        # ----------------- Getting the Path From the Game -------------------
        currdir = os.getcwd()
        tempdir = filedialog.askopenfilename(parent=win2, initialdir=currdir, title='Please select a directory')

        tempdir = ('"' + tempdir + '"')
        print("You chose %s" % tempdir)

    def friends():
        # ----------------- Creating Friends Window -------------------
        friendswin = Tk()
        friendswin.title("Friends Launcher")
        friendswin.geometry("300x600")
        friendswin.configure(bg='black')
        friendswin.resizable(width=False, height=False)
        friendswin.iconbitmap(default="icons/LogoIcon.ico")
        # ----------------- Creating Friends Frames -------------------
        friendsFrame = Frame(friendswin, width=300, height=600, bg='gray25', relief='raise')
        friendsFrame.pack()
        # ----------------- Creating Friends Widgets -------------------
        friendsLabel = Label(friendsFrame, text='Your Friends', font=('Malgun Gothic', 37, 'bold'), bg='gray20',
                             fg='white')
        friendsLabel.place(x=0, y=0)

        friend1Label = Label(friendsFrame, text='Friend 1', font=('Malgun Gothic', 30, 'italic', 'bold'), bg='gray25',
                             fg='black')
        friend1Label.place(x=0, y=100)

        friend2Label = Label(friendsFrame, text='Friend 2  ', font=('Malgun Gothic', 30, 'italic', 'bold'), bg='gray25',
                             fg='black')
        friend2Label.place(x=0, y=200)

        friend3Label = Label(friendsFrame, text='Friend 3 ', font=('Malgun Gothic', 30, 'italic', 'bold'), bg='gray25',
                             fg='black')
        friend3Label.place(x=0, y=300)
        # ----------------- Creating Friends Buttons -------------------
        friend1Button = Button(friendsFrame, text='Open', width=5, bd=1, activebackground="green",
                               activeforeground="white")
        friend1Button.place(x=200, y=122)

        friend2Button = Button(friendsFrame, text='Open', width=5, bd=1, activebackground="green",
                               activeforeground="white")
        friend2Button.place(x=200, y=222)

        friend3Button = Button(friendsFrame, text='Open', width=5, bd=1, activebackground="green",
                               activeforeground="white")
        friend3Button.place(x=200, y=322)

        friendswin.mainloop()

    # ----------------- Creating the Main Window -------------------
    win2 = Tk()
    win2.title("IFPE Games System")
    win2.geometry("1200x600")
    win2.configure(background='black')
    win2.resizable(width=False, height=False)
    win2.attributes("-alpha", 0.99)
    win2.iconbitmap(default="icons/LogoIcon.ico")
    # ----------------- Creating Frames -------------------
    leftF = Frame(win2, width=400, height=600, bg='CHARTREUSE2', relief='raise')
    leftF.pack(side=LEFT)

    internLeftFrame = Frame(leftF, width=360, height=420, bg='ForestGreen', relief='raise')
    internLeftFrame.place(x=25, y=120)

    rightF = Frame(win2, width=800, height=600, bg='black', relief='raise')
    rightF.pack(side=RIGHT)
    # ----------------- Creating Widgets and Buttons-------------------
    welcomeLabel = Label(leftF, text=f'Welcome {userName}!', font=("Malgun Gothic", 22, "bold"), bg="CHARTREUSE2",
                         fg="black")
    welcomeLabel.place(x=10, y=10)

    gameLabel = Label(leftF, text='Games:', font=("Malgun Gothic", 25, "bold"), bg="CHARTREUSE2", fg="black")
    gameLabel.place(x=20, y=62)

    lolLabel = Label(internLeftFrame, text='- League of Legends', font=("Malgun Gothic", 20, "bold"), bg="ForestGreen",
                     fg="black")
    lolLabel.place(x=1, y=1)

    lolButton = Button(internLeftFrame, text="Open", width=5, bd=1, activebackground="orange", activeforeground="white",
                       command=lol)
    lolButton.place(x=295, y=17)

    lolImage = PhotoImage(file="icons/lol1.png")
    lolImageLabel = Label(rightF, image=lolImage, bg='black')

    csLabel = Label(internLeftFrame, text="- Counter Strike:GO", font=("Malgun Gothic", 20, "bold"), bg="ForestGreen",
                    fg="black")
    csLabel.place(x=1, y=51)

    csButton = Button(internLeftFrame, text="Open", width=5, bd=1, activebackground="orange", activeforeground="white",
                      command=cs)
    csButton.place(x=295, y=65)

    csImage = PhotoImage(file="icons/cs1.png")
    csImageLabel = Label(rightF, image=csImage, bg='black')

    minecraftLabel = Label(internLeftFrame, text="- Minecraft", font=("Malgun Gothic", 20, "bold"), bg="ForestGreen",
                           fg="black")
    minecraftLabel.place(x=1, y=101)

    minecraftButton = Button(internLeftFrame, text="Open", width=5, bd=1, activebackground="orange",
                             activeforeground="white", command=minecraft)
    minecraftButton.place(x=295, y=113)

    minecraftImage = PhotoImage(file="icons/Minecraft1.png")
    minecraftImageLabel = Label(rightF, image=minecraftImage, bg='black')

    smiteLabel = Label(internLeftFrame, text="- Smite", font=("Malgun Gothic", 20, "bold"), bg="ForestGreen",
                       fg="black")
    smiteLabel.place(x=1, y=151)

    smiteButton = Button(internLeftFrame, text="Open", width=5, bd=1, activebackground="orange",
                         activeforeground="white", command=smite)
    smiteButton.place(x=295, y=161)

    smiteImage = PhotoImage(file="icons/smite1.png")
    smiteImageLabel = Label(rightF, image=smiteImage, bg='black')

    fibonniroLabel = Label(internLeftFrame, text="- Fibonniro", font=("Malgun Gothic", 20, "bold"), bg="ForestGreen",
                           fg="black")
    fibonniroLabel.place(x=1, y=201)

    fibonniroButton = Button(internLeftFrame, text="Open", width=5, bd=1, activebackground="orange",
                             activeforeground="white", command=fibonniro)
    fibonniroButton.place(x=295, y=212)

    fibonniroImage = PhotoImage(file="icons/fibonniro1.png")
    fibonniroImageLabel = Label(rightF, image=fibonniroImage, bg='black')

    internLabel = Label(rightF, text="", font=("Malgun Gothic", 40, "bold"), bg="#01ca0c", fg="black")

    intern2Label = Label(rightF, text="", font=("Segoe Print", 40, "bold"), bg="#01ca0c", fg="black")

    intern3Label = Label(rightF, text="", font=("Malgun Gothic", 20, "italic"), bg="#01ca0c", fg="black")

    intern4Label = Label(rightF, text="", font=("Terminal", 10), bg="#01ca0c", fg="black")

    playButton = ttk.Button(rightF, text='Play', width=20, command=play)

    getDirectoryButton = ttk.Button(rightF, text='Choose Directory', width=20, command=getdirectory)

    friendsButton = ttk.Button(leftF, text="Friends", width=22, command=friends)
    friendsButton.place(x=25, y=550)

    image = PhotoImage(file="icons/friends.png")

    imageLabel = Label(rightF, image=image, bg='black')
    imageLabel.place(x=-2, y=-2)

    win2.mainloop()


if __name__ == '__main__':
    window()
