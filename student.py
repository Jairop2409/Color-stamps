
 # Name: Jairo Pixabaj
# Email: JAIRO.PIXABAJ05@login.cuny.edu


import turtle 

thea = turtle.Turtle()
thea.shape('turtle')
user_hex = input('Enter a  hex color( include the #) : ')
thea.color(user_hex)

for i in range(4):
  thea.forward(20)
  thea.stamp()
