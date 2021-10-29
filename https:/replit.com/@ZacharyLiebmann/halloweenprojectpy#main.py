import turtle
tr = turtle.Turtle()
wn = turtle.Screen()
wn.addshape('giphy.gif')
tr.right(45)
tr.circle(10,360,4)
def click(x, y):
  if x < 11 and y < 11 and x > 0 and y > 0:
      tr.shape('giphy.gif')


wn.onclick(click)
wn.mainloop()
