'''
This is an argmax function, taking an array as an argument
outputs the element of max value, if the array contains multiple
of the same max value, our function select one index randomly

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example:

Given a list of example_list = [1, 2, 3, 3]
argmax(example_list) will output index 2 and index 3 with same probability



'''

# import in numpy
import numpy as np


# let's start our function
def argmax(q_values):
    """
    Takes in a list of q_values and returns the index of the item 
    with the highest value. Breaks ties randomly.
    returns: int - the index of the highest value in q_values

    """

    # to start we set the top_value as negative infinity
    top_value = float("-inf")

    # creat a list of empty elements to store ties
    ties = []

    # now, let's loop through our argument q_values
    for i in range(len(q_values)):

        # compare the current element with our top_value, if it's higher:
        if q_values[i] > top_value:

            # store the q_value as the new top value
            top_value = q_values[i]

            # clear tie list
            ties.clear()

            # put the index of our new top_value in our tie list
            ties.append(i)

        # if the current element is same as our top_value:
        if q_values[i] == top_value:

            # store the index of current value in our ties list
            ties.append(i)

    # return the top_value stored in tie, or randomly pick in our ties
    return np.random.choice(ties)
