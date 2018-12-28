from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

sense.set_rotation(180)
# sense.flip_h()

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)

# Generate a random color
def pick_random_color():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  return (r,g,b)

# sense.clear(red)

# while True:
#sense.show_message("Hello, world!", text_colour=green, back_colour=red, scroll_speed=0.1)

#while True:
# sense.show_letter("J", pick_random_color(), pick_random_color())
# sleep(1)
# sense.show_letter("u", pick_random_color(), pick_random_color())
# sleep(1)
# sense.show_letter("n", pick_random_color(), pick_random_color())
# sleep(1)
# sense.show_letter("i", pick_random_color(), pick_random_color())
# sleep(1)
# sense.show_letter("p", pick_random_color(), pick_random_color())
# sleep(1)
# sense.show_letter("e", pick_random_color(), pick_random_color())
# sleep(1)
# sense.show_letter("r", pick_random_color(), pick_random_color())
# sleep(1)

# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

# Set up where each colour will display
creeper_pixels = [
  g, g, g, g, g, g, g, g,
  g, g, g, g, g, g, g, g,
  g, b, b, g, g, b, b, g,
  g, b, b, g, g, b, b, g,
  g, g, g, b, b, g, g, g,
  g, g, b, b, b, b, g, g,
  g, g, b, b, b, b, g, g,
  g, g, b, g, g, b, g, g
]

# Display these colours on the LED matrix
sense.set_pixels(creeper_pixels)
sleep(2)


# Define some colours
B = (102, 51, 0)
b = (0, 0, 255)
S = (205,133,63)
W = (255, 255, 255)

# Set up where each colour will display
steve_pixels = [
  B, B, B, B, B, B, B, B,
  B, B, B, B, B, B, B, B,
  B, S, S, S, S, S, S, B,
  S, S, S, S, S, S, S, S,
  S, W, b, S, S, b, W, S,
  S, S, S, B, B, S, S, S,
  S, S, B, S, S, B, S, S,
  S, S, B, B, B, B, S, S
]

# Display these colours on the LED matrix
sense.set_pixels(steve_pixels)
sleep(2)

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  w,w,w,e,e,w,w,w,
  w,w,b,e,e,w,w,b,
  w,w,w,e,e,w,w,w,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e,
  e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

while True:
  sleep(1)
  sense.flip_h()

sense.clear()
