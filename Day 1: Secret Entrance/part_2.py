dial = 50
counter = 0

with open("input.txt") as f:
    for line in f:
        value = int(line[1:])
        direction = line[0]

        if direction == "L":
            value = -value

        if value < 0:
            value = abs(value)
            for i in range(value):
                dial -= 1
                if dial == -1:
                    dial = 99
                if dial == 0:
                    counter += 1
        else:
            for i in range(value):
                dial += 1
                if dial == 100:
                    dial = 0
                    counter += 1

print(counter)
