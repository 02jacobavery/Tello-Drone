# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess

# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 8999
locaddr = (host, port)
tello_address = ('192.168.10.1', 8889)  # Get the Tello drone's address

# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep=6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)


# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....

# Drone through first hoop
def firstHoop():
    sendmsg('up 50')
    sendmsg('forward 200')


# Drone through second hoop
def secondHoop():
    sendmsg('go 200 0 40 75')


# Drone through third hoop
def thirdHoopYaw():
    sendmsg('curve 100 100 0 30 250 0 60')
    time.sleep(3)
    sendmsg('ccw 180')

# Drone through fourth hoop
def fourthHoop():
    sendmsg('go -250 0 -60 75')


print("\nJacob Avery")
print("Program Name: Tello Drone Training School")
print("Date: 11.8.2020")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
print("\n****CHECK IF CO-PILOT IS READY****")
ready = input('\nAre you ready to take flight: ')

try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')

        firstHoop()

        secondHoop()

        thirdHoopYaw()

        fourthHoop()

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
