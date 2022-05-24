import json
import paho.mqtt.client as mqtt

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
    mqtt_client.on_publish = behaviour_on_publish
    mqtt_client.on_disconnect = behaviour_on_disconnect
    mqtt_client.connect(host, port = 1883, keepalive = 30)
    mqtt_client.loop_start()

    running = True

    while running:
        user_input = input("Enter your message\n")

        if user_input == "exit" or user_input == "Exit":
            running = False

        else:
            payload = {"type": "message", "from": username, "message": user_input}
            publish_status = mqtt_client.publish(topic, json.dumps(payload))

            if publish_status.rc != mqtt.MQTT_ERR_SUCCESS:
                print("the message wasn't sent")

    mqtt_client.loop_stop()
    mqtt_client.disconnect()

def behaviour_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection established")
    else:
        print("Connection failed.")
        sys.exit()

def behaviour_on_publish(client, userdata, mid):
    print("Message published")

def behaviour_on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection!")
        client.loop_stop()

    else:
        print("Successfully dissconected!")

if __name__ == '__main__':
    run()