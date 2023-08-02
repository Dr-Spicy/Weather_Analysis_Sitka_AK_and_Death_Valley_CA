# import Path from pathlib and csv module
from pathlib import Path
import csv

# read files into a list of lines objects by splitliens() method
path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

# Use csv.reader() to build a reader obj that reads from the list of lines and parses file
reader = csv.reader(lines)
# return the next(1st) line from the beginning
header_row = next(reader)

# Let's print this info out neatly in the following with enumerate().
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract high temps
highs = [int(row[4]) for row in reader]

