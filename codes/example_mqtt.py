import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("192.168.15.178", 1883, 60)
client.publish("agv/linha", "teste")
client.disconnect()