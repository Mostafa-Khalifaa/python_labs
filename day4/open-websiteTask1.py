import webbrowser
import random

websites = ["https://www.google.com", "https://www.youtube.com", "https://www.github.com", "https://www.linkedin.com/feed/","https://aws.amazon.com/ar/"]
random_site = random.choice(websites)
webbrowser.open(random_site)