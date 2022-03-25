import webbrowser, time

# len taka srandicka :)

webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

t = time.gmtime()

x = ""
x += str(t.tm_year)
if t.tm_mon < 10:
    x += "0" + str(t.tm_mon)
else:
    x += str(t.tm_mon)
if t.tm_mday < 10:
    x += "0" + str(t.tm_mday)
else:
    x += str(t.tm_mday)

x += "-"

if t.tm_hour < 10:
    x += "0" + str(t.tm_hour + 1)
else:
    x += str(t.tm_hour + 1)
if t.tm_min < 10:
    x += "0" + str(t.tm_min)
else:
    x += str(t.tm_min)

with open("file.txt", "a") as file:
    file.write(x + "\n")
