import paho.mqtt.client as mqtt
import random
import time

mqtt_host = "mqtt3.thingspeak.com"
mqtt_port = 1883
mqtt_client_id = "YOUR_CLIENT_ID"
mqtt_user = "YOUR_USER_NAME"
mqtt_pass = "YOUR_PASSWORD"
channel_id = "YOUR_CHANNEL_ID"

def generate_sensor_data():
	temperature = random.uniform(-50, 50)
	humidity = random.uniform(0, 100)
	co2 = random.uniform(300, 2000)
	return temperature, humidity, co2

def on_connect(client, userdata, flags, rc, props=None):
	print("Connected to MQTT Broker with result code "+ str(rc))

def main():
	client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=mqtt_client_id)
	client.on_connect = on_connect
	client.username_pw_set(username=mqtt_user, password=mqtt_pass)
	client.connect(mqtt_host, mqtt_port, 60)

	client.loop_start()

	while True:
		temperature, humidity, co2 = generate_sensor_data()
		payload = "field1={:.2f}&field2={:.2f}&field3={:.2f}".format(humidity, temperature, co2)
		topic = "channels/{}/publish".format(channel_id)
		print("Publishing to topic:", topic)
		print("Payload:", payload)
		client.publish(topic, payload=payload)
		print("Published: Humidity={}, Temperature={}, CO2={}".format(humidity, temperature, co2))
		time.sleep(3600)

if __name__ == "__main__":
	main()
