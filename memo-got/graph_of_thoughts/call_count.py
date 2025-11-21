# config.py

# Initialize your global counter
global_counter = 0

def increment_counter():
    """Increments the global counter."""
    global global_counter
    global_counter += 1

def get_counter_value():
    """Returns the current value of the global counter."""
    return global_counter

def reset_counter():
    global global_counter
    global_counter = 0