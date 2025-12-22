import pyshorteners as pys

s = pys.Shortener()

print('''
    URL SHORTENER!
''')

url = input("Enter URL: ")
short = s.tinyurl.short(url)

print(f"Shortened URL: {short}")