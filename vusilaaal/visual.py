
class StructOfCordinate:
    def __init__(self, NameRoom, X, Y):
        self.NameRoom = str(NameRoom)
        self.X = int(X)
        self.Y = int(Y)

class lastCoord:
    def __init__(self, X, Y):
        self.X = int(X)
        self.Y = int(Y)

class Connects:
    def __init__(self, firstRoom, secondRoom):
        self.firstRoom = str(firstRoom)
        self.secondRoom = str(secondRoom)

def IsItCordinate(lines):
    """ to check is it coordinate or not """
    count = 0
    for i in lines:
        if i == " ":
            count = count + 1
    if count == 2:
        return True
    return False

def  IsItConnects(lines):
    """ .......  """
    for i in lines:
        if str(i) == "-":
            return True
    return False

def Maxis(method, s):
    """ max """
    if method == "X":
        arrays = []
        for i in s:

            arrays.append(i.X)
        return max(arrays)
    if method == "Y":
        arrays = []
        for i in s:

            arrays.append(i.Y)
        return max(arrays)

def GiveCord(name):
    for i in ArrayOfRooms:
        if i.NameRoom == name:
            return (i.X, i.Y)

def Fromline(lines, tochoose):
    """ Return Array wich, has Name of room and coordinates or Connects """
    array = []
    arraycoonect = []
    text = ""
    count = 0
    for i in lines:
        if IsItCordinate(lines) == True:
            if str(i) != ' ' and str(i) != '\n':
                text = text + str(i)
            if str(i) == ' ' or str(i) == '\n':
                count = count + 1
                if count == 1:
                    array.append(str(text))
                    text = ""
                    continue
                lol = int(text)
                text = ""
                array.append(lol)
        if IsItConnects(lines) == True:
            if str(i) != '-' and str(i) != '\n':
                text = text + str(i)
            if str(i) == '-' or str(i) == '\n':
                lol = int(text)
                text = ""
                arraycoonect.append(lol)
    if tochoose == "c":
        return array
    if tochoose == "t":
        return arraycoonect


def ToChecK(X, Y):
    for i in Arrayoflastcord:
        if i.X == X and i.Y == Y:
            return True
    return False

data = open("file.txt", "r") # Read File by Line

ArrayOfRooms = [] # type StructOfCordinate
ArrayOfConnects = [] # type  Connects
Arrayoflastcord = [] # type lastCoord

for lines in data:
    if IsItCordinate(lines) == True:
        fromarray = Fromline(lines, "c")
        toStruct = StructOfCordinate(fromarray[0], fromarray[1], fromarray[2])
        ArrayOfRooms.append(toStruct)
    if IsItConnects(lines) == True:
        fromarray = Fromline(lines, "t")
        toStruct = Connects(fromarray[0], fromarray[1])
        ArrayOfConnects.append(toStruct)

Y = Maxis("Y", ArrayOfRooms)
X = Maxis("X",ArrayOfRooms)


from tkinter import *

root = Tk()

c = Canvas(root, width = 2000, height = 2000, bg = 'white')

c.pack()


for i in ArrayOfRooms:
    nameRoom = i.NameRoom
    Xn = i.X * 40
    Yn = i.Y * 40
    c.create_rectangle(Xn, Yn, Xn + 50 , Yn + 50, fill = "yellow")

for i in ArrayOfConnects:
    X1 , Y1 = GiveCord(i.firstRoom)
    X2, Y2 = GiveCord(i.secondRoom)
    if Y1 == Y2:
        c.create_line(X1*40 + 25  , Y1*40+25, X2*40 + 25, Y2*40+25, fill = 'yellow')
        for i in range(X1*40, X2*40):
            a = lastCoord(i, Y1)
            Arrayoflastcord.append(a)
    if X1 == X2:
        c.create_line(X1*40 + 25 , Y1*40 + 25, X2*40 + 25, Y2*40 + 25, fill = 'yellow')
        for i in range(Y1*40, Y2*40):
            a = lastCoord(X1, i)s
            Arrayoflastcord.append(a)
    if X1 != X2 and Y1 != Y2:
        a = False
        for i in range(X1*40 , X2 *40):
            for x in range(Y1*40, Y2*40):
                if ToChecK(i, x) == True:
                    a = True
        if a == False:
            c.create_line(X1*40 + 25 , Y1*40 + 25, X2*40 + 25, Y2*40 + 25, fill = 'green')
            a = True

for i in ArrayOfRooms:
    nameRoom = i.NameRoom
    X = i.X * 40
    Y = i.Y * 40
    c.create_text((X + 25, Y + 25), text = nameRoom)



root.mainloop()






# ArrayDraw = [[" "]*(Y+1) for i in range(X+1)]
#
# for i in ArrayOfRooms:
#     ArrayDraw[i.X][i.Y] = i.NameRoom

# for y in range(0,Y+1):
#     for x in range(0,X+1):
#         if x == X:
#             print(ArrayDraw[x][y])
#         else:
#             print(ArrayDraw[x][y], end = "")
#
