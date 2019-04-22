import os, time


def measure_temp():
  temp = os.popen("vcgencmd measure_temp").readline()
  return (temp.replace("temp=", "").strip())


while True:
  print(measure_temp())
  time.sleep(1)
