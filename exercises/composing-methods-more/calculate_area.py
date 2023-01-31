# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_under_graph(graph):   # TODO: Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_max_value(li):  # TODO: Rename this function to reflect what it's doing.
    maximum = li[0]
    for value in li:
        if value > maximum:
            maximum = value
    return maximum


li = [5, -1, 43, 32, 87, -100]
print(get_max_value(li))

############################
def split_process(sentence):  # TODO: Rename this function to reflect what it's doing.
    words = sentence[0:].split(' ')
    return words

print(split_process('If you were a vegetable, you’d be a ‘cute-cumber.'))
