import turtle
import tkinter as tk

def draw_pattern(size, depth):
    if depth == 0 or turtle.stopped:
        return
    else:
        for i in range(4):
            turtle.forward(size)
            draw_pattern(size/2, depth-1)
            turtle.backward(size)
            turtle.left(90)

def stop():
    turtle.stopped = True
    root.quit()  # Quit the tkinter main loop to exit the program

turtle.speed(0)
turtle.bgcolor("black")
turtle.color("Red")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.stopped = False  # Add a new attribute to the turtle object to keep track of whether the recursion should continue or not

root = tk.Tk()  # Create a tkinter window
stop_button = tk.Button(root, text="Stop", command=stop)  # Create a button that calls the stop function when clicked
stop_button.pack()  # Display the button in the window

while not turtle.stopped:  # Keep running the recursion until the stop function is called
    draw_pattern(200, 4)
    root.update()  # Update the tkinter window to handle events

turtle.done()
