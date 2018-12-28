from sense_hat import SenseHat

sense = SenseHat()

sense.set_rotation(180)

green = (0,255,0)
red = (255,0,0)

temp_low = 18.3
temp_high = 26.7

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temp: " + str(t) + " Press: " + str(p) + " Hum: " + str(h)
  
  if t > temp_low and t < temp_high:
    bg = green
  else:
    bg = red

  # Display the scrolling message
  sense.show_message(message, back_colour=bg, scroll_speed=0.05)

