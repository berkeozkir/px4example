from pymavlink import mavutil

print("Start a connection to listen serial port.")

# Start a connection listening to a UDP port
the_connection = mavutil.mavlink_connection('/dev/ttyACM0')
#MAKE SURE YOU TYPE THE DEVICE PATH CORECTLY OTHERWISE IT WILL NOT WORK

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))


while 1:
    msg = the_connection .recv_match(blocking = True)
    print(msg)

'''
#Parse the message to get specific information
while 1:
    msg = the_connection .recv_match(type='ATTITUDE',blocking = True)
    print(msg)
'''

# Once connected, use 'the_connection' to get and send messages