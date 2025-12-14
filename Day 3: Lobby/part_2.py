voltages = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        k = len(line)-12
        stack = []
        for i in range(len(line)):
            while k > 0 and stack and stack[-1] < line[i] and len(stack) - 1 + (len(line) - i) >= 12:
                stack.pop()
                k -= 1
            if len (stack) < 12:
                stack.append(line[i])

        voltage = int("".join(stack))
        voltages.append(voltage)

print(sum(voltages))
