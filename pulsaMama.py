import zerorpc
import paho.mqtt.client as mqtt

mqttClient = mqtt.Client(client_id="pulsaID", clean_session=False)
mqttClient.connect("127.0.0.1", port=1883)

class Operator(object):
    def beliPulsaMama(self, uang):
        mqttClient.publish("/pulsa", payload=("pulsa MaMa terisi: %s" % uang), qos=0)
        print(uang)

operatorBerow = zerorpc.Server(Operator())
operatorBerow.bind('tcp://0.0.0.0:4000')
operatorBerow.run()