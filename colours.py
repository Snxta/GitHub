import colorsys
import math
import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Zero-Install Interactive Vortex (Move Mouse to Morph)")
screen.tracer(0)  # Enables manual screen refresh for maximum speed

# Turtle setup
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.width(2)

# Global control variables
hue_shift = 0.0
twist_factor = 2.4


def draw_fractal_vortex(x_offset=0, y_offset=0):
    """Draws a complex geometric star spiral with HSV color gradients."""
    global hue_shift, twist_factor
    pen.clear()

    # Dynamic morphing parameters based on mouse position
    angle_step = 59 + (x_offset / 40)
    max_steps = 220

    for i in range(max_steps):
        # Calculate HSV to RGB colors for smooth rainbow transitions
        hue = (i / max_steps + hue_shift) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        pen.color(r, g, b)

        # Draw line segment & rotate
        pen.forward(i * 1.5)
        pen.left(angle_step + math.sin(i * 0.05) * (y_offset / 50))
        pen.width(1 + (i / 50))

    screen.update()


def track_mouse(event):
    """Updates rendering dynamics dynamically as mouse moves."""
    global hue_shift
    hue_shift += 0.01  # Continuously shift color wheel
    # Center-relative mouse coordinates
    x = event.x - (screen.window_width() / 2)
    y = (screen.window_height() / 2) - event.y
    draw_fractal_vortex(x, y)


# Bind mouse movement directly through Tkinter interface
canvas = screen.getcanvas()
canvas.bind("<Motion>", track_mouse)

# Initial render frame
draw_fractal_vortex(0, 0)

# Keeps window open
screen.mainloop()