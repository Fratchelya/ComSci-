#Name: Fratchelya Fergie Ciputra
#Email: Prefered email Fratchelyaciputra21@mhshs.org
#Date: Feb 25, 2021
#This program transitions the color of a turtle from red to green 

import turtle
wn=turtle.Screen()
wn.screensize(8000,500)
#Import the turtle drawing package

turtle.colormode(255)		#Allows colors to be given as 0...255
tess = turtle.Turtle()		#Create a turtle
tess.shape("turtle")		#Make it turtle shaped
tess.backward(100)			#Move her backwards, to give more space to draw

#For 0,10,20,...,250

for i in range(0,255,10):
     tess.forward(25)		#Move forward
     tess.pensize(i)		#Set the drawing size to be i (larger each time)
     tess.color(0,i,0)
     tess.color(255-i,i,0)
