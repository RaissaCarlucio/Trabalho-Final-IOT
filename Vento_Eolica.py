import paho.mqtt.client as mqtt
import random
import time

# Conectando com o broker MQTT
mqttBroker = "test.mosquitto.org"
mqttPort = 1883  # Porta padrão para MQTT

client_id = "ses/Inatel/ges/c115/vento/eolica"
client = mqtt.Client()  

# Definindo o callback de conexão
def on_connect(client, userdata, flags, reason_code, properties=None):  # Ajuste para aceitar 'properties' opcional
    if reason_code == 0:
        print("Conexão bem-sucedida.")
    else:
        print(f"Erro na conexão. Código de razão: {reason_code}")

client.on_connect = on_connect

# Inicia a conexão com o broker MQTT
client.connect(mqttBroker, mqttPort, 60)

# Inicia o loop para gerenciar eventos MQTT
client.loop_start()

# Aguarda a conexão ser estabelecida
time.sleep(2)

while True:
    # Gera um valor de vento aleatório entre 0 e 15
    randVento = random.uniform(1.0, 15.0)

    # Publica o valor do vento em um tópico
    client.publish("srs/inatel/sec/c115/vento/eolica", randVento)

    # Verifica se o vento está acima de 10 e controla as hélices
    if randVento > 10.0:
        print(f"Vento: {randVento}. Diminuindo a velocidade das hélices")
    else:
        print(f"Vento: {randVento}. Tudo funcionando normalmente.")

    time.sleep(5)

# Para o loop quando o programa terminar
client.loop_stop()
client.disconnect()
