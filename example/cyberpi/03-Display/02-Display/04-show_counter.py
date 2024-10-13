import cyberpi

cyberpi.display.show_label("Counter Program",16,0,0,0)
counter = 0

while True:
    
    if counter < 100:
        counter = counter + 1
    else:
        counter = 0
    cyberpi.display.set_brush(counter+100, 0, 0)
    cyberpi.display.show_label(counter,32,48,64,1)
