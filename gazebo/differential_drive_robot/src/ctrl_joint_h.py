#!/usr/bin/env python3
# license removed for brevity
import rospy
import math
import socket
import time as t
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties
from std_msgs.msg import Header

UDP_IP = '127.0.0.1'
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def setRight(pub, val):
    buff = ApplyJointEffort()
    buff.effort = val

    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)

    buff.joint_name = "dd_robot::right_wheel_hinge"
    pub(buff.joint_name, buff.effort, start_time, end_time)

def setLeft(pub, val):
    buff = ApplyJointEffort()
    buff.effort = val

    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)

    buff.joint_name = "dd_robot::left_wheel_hinge"
    pub(buff.joint_name,  buff.effort, start_time, end_time)


def getPos(pub):
    buff = GetJointProperties()
    buff.joint_name = 'dd_robot::left_wheel_hinge'

    val = pub(buff.joint_name)
    leftw = val.rate[0]
    buff.joint_name = 'dd_robot::right_wheel_hinge'
    val = pub(buff.joint_name)
    rightw = val.rate[0]
    v = (leftw, rightw)
    return v


def talker(val, dir):
#    pub = rospy.Publisher('/gazebo/apply_joint_effort', ApplyJointEffort, queue_size=10)
    rospy.init_node('dd_ctrl', anonymous=True)
    pub    = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)
    pubget = rospy.ServiceProxy('/gazebo/get_joint_properties',GetJointProperties)
    rate = rospy.Rate(10) # 10hz

    if(dir == "right"):
        setRight(pub, val)
    elif(dir == "left"):
        setLeft(pub, val)
    else:
        print("wrong direction!")
    v = getPos(pubget)
    if v[0] > 0:
        leftdir = "clockwise"
    else:
        leftdir = "counter clockwise"
    if v[1] > 0:
        rightdir = "clockwise"
    else:
        rightdir = "counter clockwise"
    print "left wheel vel: " + str(v[0]) + " | dir: " + leftdir
    print "right wheel vel: " + str(v[1]) + " | dir: " + rightdir
    #print dir + " " + math.sqrt((v[0]*v[0]) + (v[1]*v[1]))
    rate.sleep()

if __name__ == '__main__':
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            temp = data.split(" ")
            
            val = int(temp[0])
            talker(val, temp[1])
    except rospy.ROSInterruptException:
        pass
