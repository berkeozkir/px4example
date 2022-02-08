from pymavlink import mavutil

print("Start a connection to listen serial port.")

# Start a connection listening to a UDP port
the_connection = mavutil.mavlink_connection('/dev/ttyACM0')
#MAKE SURE YOU TYPE THE DEVICE PATH CORECTLY OTHERWISE IT WILL NOT WORK

# Wait for the first heartbeat 
#   This sets the system and component ID of remote system for the link
the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

#USE THIS TO ARM
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)

# #USE THIS TO DISARM
# the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
#                                      mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 0, 0, 0, 0, 0, 0, 0)


msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)