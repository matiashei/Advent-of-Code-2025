dial = 50
counter = 0

with open("input.txt") as f:
     for line in f:
        value = int(line[1:])
        if line[0] == "L":
          value = -value
        dial = (dial + value) % 100
        if dial == 0:
          counter += 1

print(counter)
