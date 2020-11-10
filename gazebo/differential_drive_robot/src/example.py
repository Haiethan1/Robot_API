#!/usr/bin/env python3
import rospy
from gazebo_msgs.srv import ApplyJointEffort

msg_topic = '/gazebo/apply_joint_effort'
joint_left = 'dd_roobot::left_wheel_hinge'
joint_right = 'dd_roobot::right_wheel_hinge'

msg_topic_feedabck = '/gazebo/get_joint_properties'

rospy.init_node('dd_ctrl', anonymous=True)
pub = rospy.ServiceProxy(msg_topic, ApplyJointEffort)

pub_feedback = ApplyJointEffort()
effort = 1.0
start_time = rospy.Time(0,0)

f = 0.5
T = 1/f
end_time = rospy.Time(1,0)
rate = rospy.Rate(f)

while True:
    effort = -effort
    pub(joint_left, effort, start_time, end_time)
    val = pub_feedback(joint_left)
    print(val.rate)
    rate.sleep()