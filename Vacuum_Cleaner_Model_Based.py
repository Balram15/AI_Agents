import tkinter as tk
import random

# Set up the environment
ROOMS = ['A', 'B', 'C', 'D']
room_states = {room: random.choice(['Clean', 'Dirty']) for room in ROOMS}
agent_state = {
    'current_room': 'A',
    'internal_memory': {room: 'Unknown' for room in ROOMS}
}

# GUI Setup
root = tk.Tk()
root.title("Model-Based Reflex Agent")
labels = {}

# Create labels for room states and memory visualization
def update_labels():
    for room, label in labels.items():
        text = f"Room {room}\nStatus: {room_states[room]}"
        if room == agent_state['current_room']:
            text += "\n🤖 Agent"
        label.config(text=text)

def update_memory_labels():
    for room, mem_label in memory_labels.items():
        mem_label.config(text=f"Room {room}: {agent_state['internal_memory'][room]}")

def update_internal_memory():
    current = agent_state['current_room']
    room_status = room_states[current]
    agent_state['internal_memory'][current] = room_status

# Random dirt appearance
def random_dirt():
    for room in ROOMS:
        if random.random() < 0.3:  # 30% chance to dirty the room
            room_states[room] = 'Dirty'

# Agent's Logic: move or clean, and update memory
def agent_logic():
    update_internal_memory()
    current = agent_state['current_room']
    
    if room_states[current] == 'Dirty':
        room_states[current] = 'Clean'
        log(f"Cleaned Room {current}")
    else:
        # Only move if the room is already clean or unknown, avoid staying in a clean room
        moved = False
        for room in ROOMS:
            mem = agent_state['internal_memory'][room]
            if mem == 'Dirty' or mem == 'Unknown':
                agent_state['current_room'] = room
                log(f"Moving to Room {room}")
                moved = True
                break
        
        # If agent didn't move, stay in the current room (clean)
        if not moved:
            log(f"Staying in Room {current}, it's clean!")

    # After action, randomly dirty some rooms
    random_dirt()

    update_labels()
    update_memory_labels()

# Log updates
def log(msg):
    log_text.insert(tk.END, msg + '\n')
    log_text.see(tk.END)

# GUI Layout
frame = tk.Frame(root)
frame.pack(pady=10)

# Room state labels
for room in ROOMS:
    label = tk.Label(frame, text="", width=15, height=5, relief="ridge", font=("Arial", 12))
    label.pack(side="left", padx=5)
    labels[room] = label

# Memory labels
memory_frame = tk.Frame(root)
memory_frame.pack(pady=10)

memory_labels = {}
for room in ROOMS:
    mem_label = tk.Label(memory_frame, text=f"Room {room}: Unknown", font=("Arial", 12))
    mem_label.pack(side="left", padx=5)
    memory_labels[room] = mem_label

# Log display
log_text = tk.Text(root, height=10, width=50)
log_text.pack(pady=10)

# Step button
step_btn = tk.Button(root, text="Next Step", command=agent_logic)
step_btn.pack()

# Initial update
update_labels()
update_memory_labels()

# Run GUI
root.mainloop()
