import serial
import paho.mqtt.client as mqtt

try:
  ser = serial.Serial(
    port="COM3",
    baudrate=9600,
    bytesize=serial.SEVENBITS,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE
  )
  ser.isOpen() 
  print ("port is opened!")

except IOError:
  ser.close()
  ser.open()
  print ("port was already open, was closed and opened again!")

try:
    client = mqtt.Client("controle")
    client.connect("179.225.153.162", 1883, 60)

    while True:
        print(ser.readline())
        client.publish("agv/controle", ser.readline())

except KeyboardInterrupt:
    client.disconnect()