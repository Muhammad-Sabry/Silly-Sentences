import random
import words
import time


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    ind = 0

    # Add a while loop here.
    while ind < len(template):
        if template[ind : ind+8] == "{{noun}}":
            output.append(random.choice(nouns))
            ind += 8
        elif template[ind : ind+8] == "{{verb}}":
            output.append(random.choice(verbs))
            ind += 8
        else:
            output.append(template[ind])
            ind += 1

    # After the loop has finished, join the output and return it.
    return "".join(output)

while True:
    print(silly_string(words.nouns, words.verbs, words.templates))
    time.sleep(1)
