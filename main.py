import webbrowser, time, csv

# len taka srandicka :)

time.sleep(2)
webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

t = time.gmtime()
list = [
    t.tm_mday,
    t.tm_mon,
    t.tm_year,
    "-",
    t.tm_hour,
    t.tm_min,
    t.tm_sec
]

with open("file.csv", "a", newline="") as file:
    csv.writer(file).writerow(list)
