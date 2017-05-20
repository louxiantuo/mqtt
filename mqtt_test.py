import paho.mqtt.client as mqtt
import time
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("sun")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    client.publish("qwer",payload="louxiantuo", qos=0, retain=False)
#user = "user"
#pwd = "userpassword"


client = mqtt.Client()
#client.username_pw_set(user, pwd)
client.on_connect = on_connect
client.on_message = on_message

client.connect("47.93.223.142", 1883, 60)

time.sleep(1)
client.publish("qwer",payload="louxiantuo", qos=0, retain=False)
client.publish("qwer",payload="hahaha", qos=0, retain=False)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
