# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cooked(time, temperature, pressure, desired_state):
    cooking_constant = time * temperature * pressure * COOKED_CONSTANT
    if desired_state == 'well-done': 
        return cooking_constant >= WELL_DONE
    if desired_state == 'medium':
        return cooking_constant >= MEDIUM
    return False