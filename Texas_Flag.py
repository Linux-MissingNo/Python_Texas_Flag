#Author: Linux_MissingNo
#
# Created to practice with Python
#
#
from turtle import *

TEXAS_BLUE_COLOR = "#00205B"
TEXAS_RED_COLOR = "#BF0D3E"
TEXAS_WHITE_COLOR = "#FFFFFF"
TEXAS_FLAG_LENGTH = 2
TEXAS_FLAG_WIDTH = 3

#define draw_star
def  draw_star(t, side_length, line_color=None, fill_color=None):
    if line_color:
        t.color(line_color)

    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    for _ in  range(5):
        t.forward(side_length)
        t.right(144)
        t.forward(side_length)
        t.left(72)

    if fill_color:
        t.end_fill()
#End of define draw_Star

#define draw_rectangle
def draw_rectangle(t, length, width,  line_color=None, fill_color=None):
    if line_color:
        t.color(line_color)

    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    for _ in  range(2):
       t.forward(width)
       t.right(90)
       t.forward(length)
       t.right(90)

    if fill_color:
        t.end_fill()
#end define draw_rectangle

#Preparing the Program
intWidth = TEXAS_FLAG_WIDTH * 100
intLength = TEXAS_FLAG_LENGTH * 100


designer = Turtle()

######### Start program ###########

    #set the background
bgcolor('gray')

    #draw the base of the flag
draw_rectangle(designer,  TEXAS_FLAG_LENGTH * 100, TEXAS_FLAG_WIDTH * 100, TEXAS_RED_COLOR, TEXAS_RED_COLOR)

    # return back to 0,0 
designer.home()

    #Begin paiting in the white part of the flag
draw_rectangle(designer, TEXAS_FLAG_LENGTH * 50, TEXAS_FLAG_WIDTH * 100, TEXAS_WHITE_COLOR, TEXAS_WHITE_COLOR)

    #return back to 0,0
designer.home()

    #Begin painting in the blue part of the flag
draw_rectangle(designer, TEXAS_FLAG_LENGTH * 100, TEXAS_FLAG_WIDTH * 35, TEXAS_BLUE_COLOR, TEXAS_BLUE_COLOR)

    #return to 0,0
designer.home()

    #move into postion to paint the star
starPostionX = TEXAS_FLAG_WIDTH * 20
starPostionY = TEXAS_FLAG_LENGTH * 45

designer.penup()
designer.setx(starPostionX)
designer.sety(-starPostionY)
designer.pendown()

    #Begin painting in the star
draw_star(designer, TEXAS_FLAG_LENGTH * 10, TEXAS_WHITE_COLOR, TEXAS_WHITE_COLOR)

    #preparing to end the program
        #Heading back to 0,0
designer.penup()
designer.home()
designer.pendown()

designer.hideturtle()
################# END OF PROGRAM ####################
done()