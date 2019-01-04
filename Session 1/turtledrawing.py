import turtle # Allows us to use turtles
wn = turtle.Screen() # Creates a playground for turtles
 # Create a turtle, assign to alex


wn.bgcolor("green")
wn.title("alex")


alex = turtle.Turtle()
alex.shape("classic")
alex.speed(0)
for i in range (100):
    alex.circle(15)
    alex.right(30)
 


wn.mainloop() 