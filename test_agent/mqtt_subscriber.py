import paho.mqtt.client as mqtt


class MqttClient(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        print('Connection result: {}'.format(rc))

    def on_message(self, mqttc, obj, msg):
        print('{}: {}'.format(msg.topic, msg.payload))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print('Subscribed')

    def run(self, host, port, data_topic):
        self.connect(host, port, 60)
        self.subscribe(data_topic, 0)

        rc = 0

        while rc == 0:
            rc = self.loop()
        return rc


host = '172.17.0.2'
port = 1883
data_topic = 'garden/data'
client = MqttClient()
rc = client.run(host, port, data_topic)