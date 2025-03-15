import network
import socket
import json
from time import sleep
from picozero import pico_led, pico_temp_sensor
import rp2
import sys

# WiFi Credentials
ssid = "COMOTION ON KING-Guest"
password = ""

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        if rp2.bootsel_button() == 1:
            sys.exit()
        print("Waiting for connection...")
        sleep(1)
    print(f"Connected on {wlan.ifconfig()[0]}")
    return wlan.ifconfig()[0]

def open_socket(ip):
    address = (ip, 80)  # Change to another port if needed
    connection = socket.socket()
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(address)
    connection.listen(5)  # Allow multiple connections
    return connection

def serve(connection):
    while True:
        client, _ = connection.accept()
        request = client.recv(1024).decode()
        print("Request:", request)

        response_data = {"status": "error", "message": "Invalid request"}

        if "GET /temperature" in request:
            temp = pico_temp_sensor.temp
            response_data = {"status": "success", "temperature": temp}

        elif "GET /led/on" in request:
            pico_led.on()
            response_data = {"status": "success", "message": "LED turned on"}

        elif "GET /led/off" in request:
            pico_led.off()
            response_data = {"status": "success", "message": "LED turned off"}

        # Convert response_data to JSON string
        response_body = json.dumps(response_data)

        # Include CORS headers
        response_headers = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            "Access-Control-Allow-Origin: *\r\n"
            "Access-Control-Allow-Methods: GET, POST, OPTIONS\r\n"
            "Access-Control-Allow-Headers: Content-Type\r\n"
            "\r\n"
        )

        client.send(response_headers.encode())  # Send headers
        client.send(response_body.encode())  # Send JSON response
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    sys.exit()
