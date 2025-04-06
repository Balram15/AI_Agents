import tkinter as tk
import random

# Number of rooms
NUM_ROOMS = 5

# Environment and agent setup
environment = [random.choice(['Clean', 'Dirty']) for _ in range(NUM_ROOMS)]
agent_position = 0
step = 0

# GUI setup
root = tk.Tk()
root.title("Multi-Room Reflex Vacuum Agent")

canvas = tk.Canvas(root, width=120 * NUM_ROOMS, height=200)
canvas.pack()

room_rects = []
room_texts = []
status_texts = []
agent_icon = None

# Draw all rooms
for i in range(NUM_ROOMS):
    x1, y1 = 20 + i * 100, 50
    x2, y2 = x1 + 80, y1 + 100
    rect = canvas.create_rectangle(x1, y1, x2, y2, fill="white")
    room_text = canvas.create_text((x1 + x2) // 2, 70, text=f"Room {i}")
    status = canvas.create_text((x1 + x2) // 2, 120, text="")
    room_rects.append(rect)
    room_texts.append(room_text)
    status_texts.append(status)

# Create agent icon
agent_icon = canvas.create_oval(0, 0, 0, 0, fill="blue")

# Update GUI with environment state
def update_gui():
    for i in range(NUM_ROOMS):
        canvas.itemconfig(status_texts[i], text=environment[i])
    x1 = 20 + agent_position * 100 + 30
    canvas.coords(agent_icon, x1, 55, x1 + 20, 75)

# Simple reflex logic
def simple_reflex_agent(status):
    return 'Clean' if status == 'Dirty' else 'Move'

# Run one step
def run_step():
    global agent_position, step
    step += 1
    current_status = environment[agent_position]
    action = simple_reflex_agent(current_status)

    if action == 'Clean':
        environment[agent_position] = 'Clean'
    else:
        # Move right, wrap around
        agent_position = (agent_position + 1) % NUM_ROOMS

    update_gui()
    step_label.config(text=f"Step {step} | Action: {action} | Room: {agent_position}")

# Button and status label
step_btn = tk.Button(root, text="Next Step", command=run_step)
step_btn.pack(pady=10)

step_label = tk.Label(root, text="Step 0 | Action: None")
step_label.pack()

# Start
update_gui()
root.mainloop()
