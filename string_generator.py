import random
import string


def generateString(size):
    text = string.ascii_letters + string.digits
    return "".join(random.sample(text, size))
