# Vehicle-to-Vehicle (V2V) Chat System

![V2V Logo](v2v_logom.png)

A decentralized communication system designed for vehicles to send short messages or alerts to nearby drivers (e.g., "accident ahead" or "slow down"). This implementation uses MQTT for peer-to-peer networking and provides a simple text/emoji-based interface. It can be extended to integrate with vehicle HUDs (heads-up displays) for real-time notifications.

## Features
- **Peer-to-Peer Networking**: Uses MQTT protocol for decentralized message broadcasting.
- **Simple Interface**: Text messages with optional emojis for quick communication.
- **HUD Integration**: Simulated output that could be adapted for real HUD systems.
- **Use Case**: Enhances road safety and coordination between drivers.

## Prerequisites
- Python 3.6+
- `paho-mqtt` library (`pip install paho-mqtt`)
- An MQTT broker (e.g., Mosquitto) running locally or on a server

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/techdrivex/V2V
   cd V2V
   ```
2. Install dependencies:
   ```bash
   pip install paho-mqtt
   ```
3. Install and run an MQTT broker (e.g., Mosquitto):
   - On Ubuntu: `sudo apt install mosquitto mosquitto-clients`
   - Start the broker: `mosquitto`
   - Alternatively, use a public broker like `broker.hivemq.com`.

## Usage
1. Update the `BROKER_ADDRESS` variable in `v2v_chat.py` to your MQTT broker's address (default is `localhost`).
2. Set a unique `VEHICLE_ID` for each instance (e.g., `vehicle_1`, `vehicle_2`).
3. Run the script:
   ```bash
   python v2v_chat.py
   ```
4. Follow the prompts to send predefined messages to nearby vehicles.

### Example Interaction
```
Available messages:
1: Accident ahead ⚠️
2: Slow down 🐢
3: Road clear ✅
Enter message number (or 'q' to quit): 1
Sent: Accident ahead ⚠️
```
Other vehicles subscribed to the `v2v/nearby` topic will receive:
```
[Received from vehicle_1 at 14:30:45] Accident ahead ⚠️
HUD Display: Accident ahead ⚠️
```

## Extending the System
- **Real HUD Integration**: Replace the `display_message` function with an API call to a vehicle's HUD system.
- **WebRTC Alternative**: For true peer-to-peer without a broker, adapt the system to use WebRTC (requires additional libraries like `aiortc`).
- **Range Limitation**: Simulate proximity by adding geolocation checks or using multiple MQTT topics for different regions.
- **Security**: Add encryption (e.g., TLS for MQTT) and authentication to prevent unauthorized messages.

## Limitations
- This is a proof-of-concept and lacks real-world vehicle integration.
- Assumes all vehicles are within the same MQTT topic range (no proximity simulation).
- No error handling for network disruptions.

## License
MIT License - feel free to modify and distribute.

## Contributing
Contributions are welcome! Submit a pull request or open an issue for suggestions.
