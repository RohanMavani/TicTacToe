from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
from tkinter.colorchooser import askcolor
from turtle import Turtle, Screen
from random import randint
import time

class window:

    screen = Screen()
    tur = Turtle()
    head = Turtle()
    first = ''
    user = ''
    computer = ''
    winning_combination = []

    def __init__(self):
        self.userscore = 0
        self.tie = 0
        self.computerscore = 0
        self.username = "User"
        self.screen = Screen()
        self.tur.speed(0)
        self.head.speed(0)
        self.tur.ht()
        self.head.ht()
        self.tur.pensize(6)
        self.head.pensize(6)
        self.initPos = (-150,150)
        self.lastIsUser = False
        self.lastIsCom = False
        self.places= {}
        self.pencolor = "black"

    def creat_window(self):
        self.root = Toplevel()
        self.root.title(string="TicTacToe")
        image = ImageTk.PhotoImage(Image.open("unnamed.png"))   # to add the image to the screen
        panel = Label(self.root, image = image)                 # reference of the image object
        panel.pack()
        menu = Menu(self.root)                                  # to create the menubar
        self.root.config(menu = menu)

        filemenu = Menu(menu,tearoff = 0)                       # to edit file menu to menubar
        filemenu.add_command(label="Name", command = self.getname)
        filemenu.add_command(label="Play",command = self.play)
        filemenu.add_command(label="Score", command = self.scorecard)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.exit)
        menu.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menu, tearoff = 0)
        menu.add_cascade(label = "Edit", menu = editmenu)
        editmenu.add_command(label = "Pencolor", command = self.pen_color)


        help = Menu(menu, tearoff = 0)
        menu.add_cascade(label="Help", menu=help)
        help.add_command(label="Rules", command = self.rules)                     # to show rules

        self.root.mainloop()

    def getname(self):
        self.username = simpledialog.askstring("Introduction", "Enter your name").capitalize()
        messagebox.showinfo("Welcome", "%s ! Welcome to Tic-Tac-Toe game." % self.username)

    def scorecard(self):
        top = Toplevel()
        Button(top, text=self.username, height = 1, width = 10,bg = "orange").grid(row = 0, column = 0)
        Button(top, text=str(self.userscore), height = 1, width = 5,bg = "green").grid(row = 0, column = 2)
        Button(top, text="Tie", height = 1, width = 10,bg = "orange").grid(row = 1, column = 0)
        Button(top, text=str(self.tie), height = 1, width = 5,bg = "green").grid(row = 1, column = 2)
        Button(top, text="Computer", height = 1, width = 10,bg = "orange").grid(row = 2, column = 0)
        Button(top, text=str(self.computerscore), height = 1, width = 5,bg = "green").grid(row = 2, column = 2)
        Button(top, text = "Ok", command = top.withdraw, height = 1, width = 5, bg = "gray").grid(row = 6 , column =1)


    def exit(self):
        if messagebox.askokcancel("Exit", "Do you Want to leave?"):
            self.root.destroy()

    def rules(self):
        top = Toplevel()
        top.title("Rules")
        rul = '''1. The game is played on a grid that's 3 squares by 3 squares.\n\n2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.
        \n\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
        '''
        Label(top, text=rul, font="-weight bold", justify=LEFT).pack()
        Button(top, text="Got it", command=top.withdraw, bg = "gray", height = 1, width = 8).pack()

    def pen_color(self):
        color =  askcolor(color = "red", title  = "%s's color"%self.username)
        self.pencolor = color[1]

    def set_title(self):
        self.head.pu()
        self.head.goto(-130, 250)
        self.head.pd()
        self.head.color("black")
        self.head.pensize(9)
        self.head.write("Welcome to Tic Tac Toe", False, "left", ("Arial", 20, "bold"))

    def set_screen(self):
        self.screen.title("Welcome to Tic Tac Toe")
        self.screen.bgcolor("#f2d068")
        self.set_title()

    def draw_o(self, dim):

        if self.user == 'o':
            self.tur.color(self.pencolor)
        else:
            self.tur.color("red")
        #self.tur.color()
        self.tur.pu()
        self.tur.goto(dim)
        self.tur.right(90)
        self.tur.forward(20)
        self.tur.left(90)
        self.tur.pd()
        self.tur.circle(20)
        self.tur.pu()
        self.tur.goto(self.initPos)

    def draw_x(self, dim):

        if self.user == 'x':
            self.tur.color(self.pencolor)
        else:
            self.tur.color("red")
        self.tur.pu()
        self.tur.goto(dim)
        self.tur.pd()
        self.tur.left(45)
        for i in range(4):
            self.tur.forward(20)
            self.tur.backward(20)
            self.tur.left(90)
        self.tur.pu()
        self.tur.right(45)
        self.tur.goto(self.initPos)

    def drawBox(self):

        self.head.color("black")

        self.head.pu()
        self.head.goto(self.initPos)

        for row in range(2):
            self.head.up()
            self.head.right(90)
            self.head.forward(120)
            self.head.pd()
            self.head.left(90)
            self.head.forward(360)
            self.head.backward(360)

        self.head.pu()
        self.head.goto(self.initPos)

        for column in range(2):
            self.head.up()
            self.head.forward(120)
            self.head.pd()
            self.head.right(90)
            self.head.forward(360)
            self.head.backward(360)
            self.head.left(90)

        self.head.pu()
        self.head.goto(self.initPos)


    def select_symbol(self):

        symbol = input("Select your symbol: ")
        if symbol == 'o':  # if user enters o, computer will get x.
            self.user = 'o'
            self.computer = 'x'
        else:
            self.computer = 'o'
            self.user = 'x'

    def whoGoesFirst(self):

        if randint(0, 1):  # if we get 0, computer is going first, else user is going first.
            self.first = "user"
        else:
            self.first = "computer"
        print(self.first + " is going first.")
    def result(self):

        combinations = [[0, 1, 2], [0, 3, 6], [6, 7, 8], [2, 5, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [3, 4, 5]]
        for combination in combinations:
            if self.keyExist(combination[0], combination[1], combination[2], self.places):
                if self.places[combination[0]] == self.places[combination[1]] == self.places[combination[2]]:
                    self.winning_combination = combination
                    return True
        return False

    def keyExist(self, a, b, c, place):
        return a in place and b in place and c in place

    def assign(self,x,y):
        self.x = x
        self.y = y


    def userInput(self):

        while True:
            place = int(input("Enter a digit between 0 - 8: "))
            if place not in self.places and place in range(0, 9):
                self.places[place] = self.user
                self.lastIsUser = True
                self.lastIsCom = False
                #print(self.places)
                return place
            else:
                print("You can not override the move.")
                continue


    def corners(self):
        for i in [4, 0, 2, 6, 8]:
            if i not in self.places:
                return i

    def block(self):

        combinations = [[0, 1, 2], [0, 3, 6], [6, 7, 8], [2, 5, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [3, 4, 5]]
        missing = 0
        for pos in combinations:
            usertracker = []
            for key in pos:
                if key in self.places:
                    usertracker.append(self.places[key])
                else:
                    missing = key
            if usertracker.count(self.user) == 2 and usertracker.count(self.computer) == 0:
                return missing
            else:
                continue
        return -1

    def strategi(self):

        combinations = [[0, 1, 2], [0, 3, 6], [6, 7, 8], [2, 5, 8], [1, 4, 7], [3, 4, 5], [0, 4, 8], [2, 4, 6]]

        best = {}
        best[2] = []
        best[1] = []

        for pos in combinations:
            missing = 0
            counter = 0
            for i in pos:
                if i not in self.places:
                    missing = i
                else:
                    if self.places[i] == self.user:
                        counter = 0
                        break
                    else:
                        counter += 1
            if counter == 2 and missing not in best[2]:
                best[2].append(missing)
            elif counter == 1 and missing not in best[1]:
                best[1].append(missing)

        #print(best)
        if len(best[2]) != 0:
            return (best[2][0], 2)
        elif len(best[1]) != 0:
            return (best[1][0], 1)
        else:
            for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                if i not in self.places:
                    return (i, 0)


    def computerInput(self):

        index = 0

        if len(self.places) <= 2:

            index = self.corners()
            self.places[index] = self.computer
            self.lastIsUser = False
            self.lastIsCom = True
            return index

        else:
            stob = self.strategi()
            blob = self.block()

            #print(stob)
            #print(blob)

            if stob[1] > 1:
                self.places[stob[0]] = self.computer
                self.lastIsUser = False
                self.lastIsCom = True
                #print(self.places)
                return stob[0]
            elif blob != -1:
                self.places[blob] = self.computer
                self.lastIsUser = False
                self.lastIsCom = True
                #(self.places)
                return blob
            else:
                self.places[stob[0]] = self.computer
                self.lastIsUser = False
                self.lastIsCom = True
                #print(self.places)
                return stob[0]

    def whereToDraw(self, index, symbol):

        if index == 0:
            where = (-90, 90)
            self.tur.pd()
            if symbol == 'o':
                self.draw_o(where)
            else:
                self.draw_x(where)
        elif index == 1:
            where = (30, 90)
            self.tur.pd()
            if symbol == 'o':
                self.draw_o(where)
            else:
                self.draw_x(where)
        elif index == 2:
            where = (150, 90)
            self.tur.pd()
            if symbol == 'o':
                self.draw_o(where)
            else:
                self.draw_x(where)
        elif index == 3:
            where = (-90, -30)
            self.tur.pd()
            if symbol == 'o':
                self.draw_o(where)
            else:
                self.draw_x(where)
        elif index == 4:
            where = (30, -30)
            self.tur.pd()
            if symbol == 'o':
                self.draw_o(where)
            else:
                self.draw_x(where)
        elif index == 5:
            where = (150, -30)
            self.tur.pd()
            if symbol == 'o':
                self.draw_o(where)
            else:
                self.draw_x(where)
        elif index == 6:
            where = (-90, -150)
            self.tur.pd()
            if symbol == 'o':
                self.draw_o(where)
            else:
                self.draw_x(where)
        elif index == 7:
            where = (30, -150)
            self.tur.pd()
            if symbol == 'o':
                self.draw_o(where)
            else:
                self.draw_x(where)
        elif index == 8:
            where = (150, -150)
            self.tur.pd()
            if symbol == 'o':
                self.draw_o(where)
            else:
                self.draw_x(where)


    def draw(self):

        self.select_symbol()
        self.whoGoesFirst()
        counter = 0

        if self.first == "computer":
            index = self.computerInput()
            print("computer:", str(index))
            self.whereToDraw(index, self.computer)
        elif self.first == "user":
            index = self.userInput()
            print("%s:" % self.username, str(index))
            self.whereToDraw(index, self.user)

        counter += 1

        while True:
            counter += 1
            if self.lastIsUser:
                index = self.computerInput()
                print("computer:", str(index))
                self.whereToDraw(index, self.computer)
            else:
                index = self.userInput()
                print("%s:" % self.username, str(index))
                self.whereToDraw(index, self.user)
            if self.result():
                break
            elif counter == 9:
                break

    def showno(self):
        counter = 0

        for col in range(3):
            x = -40
            y = 35

            for row in range(3):
                self.head.pu()
                self.head.goto(x + (row * 120), y - (col * 120))
                self.head.pd()
                self.head.write(counter)
                counter += 1
                self.head.pu()
        self.head.goto(self.initPos)


    def cross_line(self, combination):
        self.tur.color("green")
        self.tur.speed(1)

        if combination == [0, 1, 2]:
            self.tur.pu()
            self.tur.goto(-90, 90)
            self.tur.pd()
            self.tur.pensize(15)
            self.tur.goto(150, 90)
            self.tur.pu()
        elif combination == [3, 4, 5]:
            self.tur.pu()
            self.tur.goto(-90, -30)
            self.tur.pd()
            self.tur.pensize(15)
            self.tur.goto(150, -30)
            self.tur.pu()
        elif combination == [6, 7, 8]:
            self.tur.pu()
            self.tur.goto(-90, -150)
            self.tur.pd()
            self.tur.pensize(15)
            self.tur.goto(150, -150)
            self.tur.pu()
        elif combination == [0, 3, 6]:
            self.tur.pu()
            self.tur.goto(-90, 90)
            self.tur.pd()
            self.tur.pensize(15)
            self.tur.goto(-90, -150)
            self.tur.pu()
        elif combination == [1, 4, 7]:
            self.tur.pu()
            self.tur.goto(30, 90)
            self.tur.pd()
            self.tur.pensize(15)
            self.tur.goto(30, -150)
            self.tur.pu()
        elif combination == [2, 5, 8]:
            self.tur.pu()
            self.tur.goto(150, 90)
            self.tur.pd()
            self.tur.pensize(15)
            self.tur.goto(150, -150)
            self.tur.pu()
        elif combination == [0, 4, 8]:
            self.tur.pu()
            self.tur.goto(-90, 90)
            self.tur.pd()
            self.tur.pensize(15)
            self.tur.goto(150, -150)
            self.tur.pu()
        elif combination == [2, 4, 6]:
            self.tur.pu()
            self.tur.goto(150, 90)
            self.tur.pd()
            self.tur.pensize(15)
            self.tur.goto(-90, -150)
            self.tur.pu()

    def Reset(self):
        self.tur.reset()
        self.places = {}
        self.winning_combination = []
        self.lastIsUser = False
        self.lastIsCom = False
        self.first = ' '
        self.user = ' '
        self.computer = ' '
        self.tur.speed(0)
        self.head.speed(0)
        self.tur.ht()
        self.head.ht()
        self.tur.pensize(6)
        self.set_screen()
        self.drawBox()
        self.showno()

    def YesNo(self):
        if messagebox.askyesno("verify", "Do you want to continue?"):
            return True
        else:
            return False

    def winningEmoji(self):
        self.tur.reset()
        self.head.reset()
        screen = Screen()
        screen.bgcolor("black")
        self.tur.pencolor("white")
        self.tur.pu()
        self.tur.ht()
        self.head.ht()
        self.tur.pensize(6)
        self.tur.speed(0)

        self.tur.goto(-75, 150)
        self.tur.pd()
        self.tur.circle(20)  # eye one

        self.tur.pu()
        self.tur.goto(75, 150)
        self.tur.pd()
        self.tur.circle(20)  # eye two

        self.tur.pu()
        self.tur.goto(0,0)
        self.tur.pd()
        self.tur.circle(100,80)   #right smile
        self.tur.pu()
        self.tur.setheading(180) # <-- look West
        self.tur.goto(0,0)
        self.tur.pd()
        self.tur.circle(-100,80)
        self.tur.pu()
        self.tur.goto(-110, -150)
        self.tur.write("You won..Hurray", False, "left", ("Arial", 20, "bold"))


    def TieEmoji(self):
        self.tur.reset()
        self.head.reset()
        screen = Screen()
        screen.bgcolor("black")
        self.tur.pencolor("white")
        self.tur.pu()
        self.tur.ht()
        self.head.ht()
        self.tur.pensize(6)
        self.tur.speed(0)

        self.tur.goto(-75, 150)
        self.tur.pd()
        self.tur.pencolor("#FFC300")
        self.tur.circle(20)  # eye one

        self.tur.pu()
        self.tur.goto(75, 150)
        self.tur.pd()
        self.tur.circle(20)  # eye two

        self.tur.pu()
        self.tur.goto(0, 80)
        self.tur.left(180)
        self.tur.pd()
        self.tur.pencolor("red")
        self.tur.fd(60)
        self.tur.back(120)
        self.tur.pu()
        self.tur.goto(-110, -150)
        self.tur.pencolor("white")
        self.tur.write("It's tie...Try again", False, "left", ("Arial", 20, "bold"))


    def loosingEmoji(self):
        self.tur.reset()
        self.head.reset()
        screen = Screen()
        screen.bgcolor("black")
        self.tur.pencolor("white")
        self.tur.pu()
        self.tur.ht()
        self.head.ht()
        self.tur.pensize(6)
        self.tur.speed(0)

        self.tur.goto(-75, 150)
        self.tur.pd()
        self.tur.pencolor("#FFC300")
        self.tur.circle(20)  # eye one

        self.tur.pu()
        self.tur.goto(75, 150)
        self.tur.pd()
        self.tur.circle(20)  # eye two

        self.tur.pu()
        self.tur.goto(0, 80)
        self.tur.left(180)
        self.tur.pd()
        self.tur.pencolor("red")
        self.tur.circle(100, 80)  # right smile

        self.tur.pu()
        self.tur.setheading(0)  # <-- look West
        self.tur.goto(0, 80)
        self.tur.pd()
        self.tur.circle(-100, 80)
        self.tur.pu()
        self.tur.goto(-110,-150)
        self.tur.pencolor("white")
        self.tur.write("You lost..Try again",False, "left", ("Arial", 20, "bold"))


    def play(self):
        self.set_screen()
        self.drawBox()
        self.showno()

        while True:

            self.draw()
            self.cross_line(self.winning_combination)

            if len(self.winning_combination) == 3:
                if self.places[self.winning_combination[0]] == self.user:
                    self.userscore += 1
                    self.winningEmoji()

                elif self.places[self.winning_combination[0]] == self.computer:
                    self.computerscore += 1
                    self.loosingEmoji()

            else:
                self.tie += 1
                self.TieEmoji()

            if self.YesNo():
                self.Reset()
            else:
                break

m = window()
m.creat_window()


