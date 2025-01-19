"""*********************************************************************
*! \fn          main
*  \brief       start code
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
"""*********************************************************************
                includes
*********************************************************************"""
from paho.mqtt import client as mqtt_client
import random
import time
"""*********************************************************************
                Constant
*********************************************************************"""
broker = ''
port = 1883
topic = "self"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60
"""*********************************************************************
                local val
*********************************************************************"""

"""*********************************************************************
*! \fn          worker(sum_of_loops=None, json_config_data)
*  \brief       work functon, loop through the tasks
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt(mqtt_url="", mqtt_port=1883, mqtt_topic="server"):
    global client
    global broker
    global port
    global topic
    broker = mqtt_url
    port = mqtt_port
    topic = mqtt_topic
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    client = mqtt_client.Client()
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.loop_start()
    return client


def publish(msg):
    global client
    msg_count = 1
    time.sleep(1)
    #msg = f"messages: {msg_count}"
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    #if status == 0:
    #    print(f"Send `{msg}` to topic `{topic}`")
    #else:
    #    print(f"Failed to send message to topic {topic}")
