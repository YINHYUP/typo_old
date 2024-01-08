"""

alien_0 = {'color' : 'green', 'point' : 5}

print(alien_0['color'])
print(alien_0['point'])

"""

"""

alien_0 = {'color' : 'green', 'point' : 5}

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

"""

"""

alien_0 = {'color' : 'green'}
print(f"Alien color is {alien_0['color']}.")
alien_0['color'] = 'red'
print(f"Now alien color is {alien_0['color']}.")

"""

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'fast'}

print(f"Original alien position : {alien_0['x_position']}, {alien_0['y_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
    y_increment = 2
elif alien_0['speed'] == 'medium':
    x_increment = 2
    y_increment = 4
elif alien_0['speed'] == 'fast':
    x_increment = 3
    y_increment = 6

alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_0['y_position'] = alien_0['y_position'] + y_increment

print(f"New alien position : {alien_0['x_position']}, {alien_0['y_position']}")


