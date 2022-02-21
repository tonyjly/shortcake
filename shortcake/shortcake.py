import string
import random


class ShortLink:
    """Generate a short link."""


    def __init__(self, long_url):
        self.long_url = long_url


    def generate_string(self, size=8):
        """Generate a random string."""
        chars = (string.ascii_letters + string.digits)
        self.random_string = ''.join(random.choice(chars) for i in range(size))


link1 = ShortLink("https://www.dell.com")
link1.generate_string()
print(link1.random_string)
