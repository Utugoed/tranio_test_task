import random
import string


CODE_LENGTH = 6

def generate_code():
    letters = string.ascii_letters + string.digits
    link = "".join(random.choice(letters) for i in range(CODE_LENGTH))
    return link