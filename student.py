
 # Name: Jairo Pixabaj
# Email: JAIRO.PIXABAJ05@login.cuny.edu


import turtle 

thea = turtle.Turtle()
thea.shape('turtle')


for i in range(5):
 user_hex = input('Enter a  hex color( include the #) : ')
 thea.color(user_hex)
 thea.forward(20)
 thea.stamp()
