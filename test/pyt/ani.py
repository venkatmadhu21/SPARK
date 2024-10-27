import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Animated Assistant Logo")

# Load the logo images
logo_image = tk.PhotoImage(file=r"C:\Users\USER\Desktop\JARVIS\motion.png")  # Initial logo
animated_image = tk.PhotoImage(file=r"C:\Users\USER\Desktop\JARVIS\motion.png")  # Animated logo

# Create a label to display the logo
logo_label = tk.Label(window, image=logo_image)
logo_label.pack()

# Animation state
animated = False

# Animation function
def animate():
    global animated
    if animated:
        logo_label.config(image=logo_image)  # Show initial logo
    else:
        logo_label.config(image=animated_image)  # Show animated logo
    animated = not animated  # Toggle the state
    window.after(500, animate)  # Schedule the next animation frame

# Start the animation
animate()

# Run the main loop
window.mainloop()