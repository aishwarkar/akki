import turtle as t
import random as r
akki=t.Turtle()

#random color window 
win=t.Screen() 
color=["light green","pink","sky blue","yellow","orange","violet","blue","red","gray"]
win.bgcolor(r.choice(color))

#players
akki.shape("turtle")
akki.color("black")
#akki.pendown()

#target
akki9=t.Turtle()
akki9.shape("circle")
akki9.color("violet")
#akki9.pendown()
akki9.penup()
#akki9.forward(100)
akki9.setpos(r.randint(-200,300),r.randint(-200,300))


#moving player

speed=25   #defines speed for the turtle

def turnleft():
  akki.left(10)

def turnright():
  akki.right(10)

def moveforward():
  akki.forward(speed)

def movebackward():
  akki.backward(speed)


#assign keys for movement

win.listen()
win.onkey(turnright,"right")
win.onkey(turnleft,"left")
win.onkey(moveforward,"up")
win.onkey(movebackward,"down")

akki9.pendown()
#moving the cirle randomly with code
while True:
  akki9.forward(111)
  if akki9.xcor() > 200:
    akki9.setheading(r.randint(90,180))
  if akki9.xcor() < -200:
    akki9.setheading(r.randint(-90,90))
  if akki9.ycor() > 200:
    akki9.setheading(r.randint(180,360))
  if akki9.ycor() < -200:
    akki9.setheading(r.randint(0,180))
  if akki.distance(akki9.xcor(),akki9.ycor()) < 20:
     win.bgcolor("gold")
     break

win.mainloop()
#akki9.setpos