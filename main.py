import webbrowser, time, csv

# len taka srandicka :)

webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

t = time.gmtime()
list = [
    t.tm_mday,
    t.tm_mon,
    t.tm_year,
    "-",
    t.tm_hour + 1, # hours starts at 0 for some reason...
    t.tm_min,
    t.tm_sec
]

with open("file.csv", "a", newline="") as file:
    csv.writer(file).writerow(list)
