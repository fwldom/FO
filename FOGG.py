import turtle
num = int(turtle.textinput(title="Enter Number Forward", prompt=("Enter Forward !")))
num = int(turtle.textinput(title="Enter Number Range", prompt=("Enter Forward !")))

num2 = int(turtle.textinput(title="Enter Number left", prompt=("Enter left Range !")))
num3 = int(turtle.textinput(title="Enter Number left", prompt=("Enter left End Range  !  ")))
width = int(turtle.textinput(title="Enter Number width", prompt=("Enter width !  ")))
laki = turtle.Turtle()
laki.shape('turtle')
laki.width(width)
for i in range(50):
    for j in range(8):
        laki.forward(num)
        laki.left(num2)
    laki.left(num3)
input()