import string
import random


class ShortLink:
    """Generate a short link."""


    def __init__(self, long_link):
        self.long_link = long_link
        self.random_string = ""
        self.short_link = ""


    def generate_string(self, size=8):
        """Generate a random string."""
        chars = (string.ascii_letters + string.digits)
        self.random_string = ''.join(random.choice(chars) for i in range(size))


    def generate_short_link(self):
        """Generate a Short Link."""
        self.generate_string()
        self.short_link = 'https://www.shortcake.com/' + self.random_string


link1 = ShortLink("https://www.dell.com")
link1.generate_short_link()
print(link1.short_link)
