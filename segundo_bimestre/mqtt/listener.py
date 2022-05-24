import paho.mqtt.client as mqtt
import json
import sys

def run():
    host = "mothership.inf.tu-dresden.de"
    topic = "chat"
    username = "chat"
    password = "chat"

    user_info = {"host": host, "topic": topic, "username": username}
    mqtt_client = mqtt.Client(userdata = user_info)
    mqtt_client.username_pw_set(username, password)
    mqtt_client.will_set(topic, payload = "User " + username + " timed out.\n", qos = 0, retain = False)
    mqtt_client.reconnect_delay_set(min_delay=1, max_delay=120)
    mqtt_client.on_connect = behaviour_on_connect
    mqtt_client.on_subscribe = behaviour_on_subscribe
    mqtt_client.on_message = behaviour_on_message
    mqtt_client.on_disconnect = behaviour_on_disconnect
    mqtt_client.connect(host, port = 1883, keepalive = 30)
    mqtt_client.loop_start()
    mqtt_client.subscribe(topic, qos = 0)
    input("Press Enter to disconnect ... \n")
    notice = "User " + username + " disconnecting from " + topic + " ."
    payload = {"type": "notice", "from": username, "notice": notice }
    mqtt_client.publish(topic, json.dumps(payload))
    mqtt_client.loop_stop()
    mqtt_client.disconnect()

def behaviour_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection to the broker established.")
    else:
        print("Connection failed.")
        sys.exit()

def behaviour_on_subscribe(client, userdata, mid, granted_qos):
    print("Subscription successfull(" +userdata.get("topic") + ").")
    notice = "User " + userdata.get("username") + " is now subscribed to " + userdata.get("topic") + " ."
    payload = {"type": "notice", "from": userdata.get("username"), "notice": notice }
    client.publish(userdata.get("topic"), json.dumps(payload))


def behaviour_on_message(client, userdata, message):
    message_data = json.loads(message.payload)

    if message_data["type"] == "message":
        print(str(message_data["from"]) + ": " + str(message_data["message"]))

    if message_data["type"] == "notice":
        print(str(message_data["notice"]))

def behaviour_on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection!")

        client.loop_stop()

    else:
        print("Successfully dissconected!")

if __name__ == '__main__':
    run()