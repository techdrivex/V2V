import paho.mqtt.client as mqtt
import json
import threading
import time
from datetime import datetime

# Simulated vehicle ID (unique for each vehicle)
VEHICLE_ID = "vehicle_1"  # Change this for each instance
BROKER_ADDRESS = "localhost"  # Replace with actual MQTT broker address
TOPIC = "v2v/nearby"  # Topic for nearby vehicle communication

# Predefined message templates (for simplicity)
MESSAGE_TEMPLATES = {
    "1": {"text": "Accident ahead", "emoji": "⚠️"},
    "2": {"text": "Slow down", "emoji": "🐢"},
    "3": {"text": "Road clear", "emoji": "✅"}
}

# Callback when connected to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"{VEHICLE_ID} connected to MQTT broker")
        client.subscribe(TOPIC)
    else:
        print("Connection failed")

# Callback when a message is received
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        sender_id = payload.get("vehicle_id")
        if sender_id != VEHICLE_ID:  # Ignore own messages
            timestamp = payload.get("timestamp")
            message = payload.get("message")
            emoji = payload.get("emoji", "")
            display_message(sender_id, timestamp, message, emoji)
    except Exception as e:
        print(f"Error processing message: {e}")

# Display the message (simulating HUD or console output)
def display_message(sender_id, timestamp, message, emoji):
    print(f"\n[Received from {sender_id} at {timestamp}] {message} {emoji}")
    # Simulate HUD integration (could be extended to a real HUD API)
    print(f"HUD Display: {message} {emoji}")

# Send a message to nearby vehicles
def send_message(client, message_key):
    if message_key in MESSAGE_TEMPLATES:
        message_data = MESSAGE_TEMPLATES[message_key]
        payload = {
            "vehicle_id": VEHICLE_ID,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "message": message_data["text"],
            "emoji": message_data["emoji"]
        }
        client.publish(TOPIC, json.dumps(payload))
        print(f"Sent: {message_data['text']} {message_data['emoji']}")
    else:
        print("Invalid message key")

# User input thread
def user_input(client):
    while True:
        print("\nAvailable messages:")
        for key, msg in MESSAGE_TEMPLATES.items():
            print(f"{key}: {msg['text']} {msg['emoji']}")
        choice = input("Enter message number (or 'q' to quit): ")
        if choice == 'q':
            break
        send_message(client, choice)

# Main function to start the V2V system
def main():
    # Initialize MQTT client
    client = mqtt.Client(VEHICLE_ID)
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to broker
    client.connect(BROKER_ADDRESS, 1883, 60)

    # Start the MQTT loop in a separate thread
    client.loop_start()

    # Start user input thread
    input_thread = threading.Thread(target=user_input, args=(client,))
    input_thread.start()

    # Keep the main thread alive
    try:
        input_thread.join()
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
    