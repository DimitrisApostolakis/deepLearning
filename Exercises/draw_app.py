import tkinter as tk

def on_left_click(event, canvas):
    x, y = event.x, event.y
    size = 8
    canvas.create_oval(x-size, y-size, x+size, y+size, fill="white", outline="white")
    
def predict():
    print(f"Predict pressed")
    
def clear(canvas):
    canvas.delete("all")
    canvas.configure(bg="black")
    
def window():
    width = 400
    height = 500

    m = tk.Tk()
    m.title("myLeNet")
    m.minsize(width, height)
    m.maxsize(width, height)

    w = tk.Canvas(master=m, width=400, height=400, bg="black")
    w.pack(pady=10)

    frame_buttons = tk.Frame(m)
    frame_buttons.pack(side="bottom", pady=10)

    clear_button = tk.Button(frame_buttons, text="Clear", width=25, command= lambda: clear(w))
    clear_button.pack(side="left", padx=5)

    predict_button = tk.Button(frame_buttons, text="Predict", width=25, command=predict)
    predict_button.pack(side="right", padx=5)

    w.bind("<B1-Motion>", lambda event: on_left_click(event, w))

    m.mainloop()


window()
model = customCNN()