voltages = []

biggest_voltage = "00"

with open("input.txt") as f:
     for line in f:
        length = len(line.strip())
        for i in range(length-1):
            for x in range(i+1, length):
                if line[i]+line[x] > biggest_voltage:
                    biggest_voltage = line[i] + line[x]
        voltages.append(int(biggest_voltage))
        biggest_voltage = "00"

print(sum(voltages))