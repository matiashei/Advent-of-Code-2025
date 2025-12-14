locations = []
max_area = 0

with open("input.txt") as file:
    for line in file:
        a, b = line.strip().split(",")
        locations.append((int(a), int(b)))

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            area = (abs(locations[i][0] - locations[j][0])+1) * (abs(locations[i][1] - locations[j][1])+1)
            if area > max_area:
                max_area = area

print(max_area)
