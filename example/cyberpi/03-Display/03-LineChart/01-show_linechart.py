import cyberpi

value = 0

while True:
    if value < 100:
        value = value + 1
    else:
        value = 0
    cyberpi.linechart.add(value)
