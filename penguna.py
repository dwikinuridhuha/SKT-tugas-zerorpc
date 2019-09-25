import zerorpc
import paho.mqtt.client as mqtt
import sys

mqttClient = mqtt.Client(client_id="userID", clean_session = False)
mqttClient.connect('127.0.0.1', port=1883)
mqttClient.subscribe("/pulsa", qos=0)

def headleMessage(client, obj, msg):
    print(msg.payload)
    mqttClient.disconnect()

print("\n1. mengisiMarket\n2. mengisiBank\n3. cekSaldoBank\n4. cekSaldoMarket\n5. BeliPulsa")
pilih = int(input("pilih: "))
if(pilih == 1):
    masuk = int(input("masukan nominal: "))
    penguna = zerorpc.Client()
    penguna.connect("tcp://127.0.0.1:6000")
    keter = penguna.tambahUangMarket(masuk)
    print("sekarang saldo market anda: ", keter)
    sys.exit()

elif(pilih == 2):
    masuk = int(input("masukan nominal: "))
    penguna = zerorpc.Client()
    penguna.connect("tcp://127.0.0.1:6000")
    keter = penguna.isiDuitBank(masuk)
    print("sekarang saldo Bank anda: ", keter)
    sys.exit()
        
elif(pilih == 3):
    penguna = zerorpc.Client()
    penguna.connect("tcp://127.0.0.1:6000")
    keter = penguna.cekSaldoBank()
    print("Saldo anda bank: ", keter)
    sys.exit()
            
elif(pilih == 4):
    penguna = zerorpc.Client()
    penguna.connect("tcp://127.0.0.1:6000")
    keter = penguna.cekSaldoMarket()
    print("Saldo anda market: ", keter)
    sys.exit()

elif(pilih == 5):
    masuk = int(input("masukan nominal: "))
    penguna = zerorpc.Client()
    penguna.connect("tcp://127.0.0.1:6000")
    penguna.MamaBeliPulsa(masuk)
        
else:
    print("anda salah input")
    
mqttClient.on_message = headleMessage
mqttClient.loop_forever()