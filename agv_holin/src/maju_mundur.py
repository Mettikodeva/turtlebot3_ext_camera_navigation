import rospy
from std_msgs.msg import Int8MultiArray

if __name__ == "__main__":
    rospy.init_node("yok_main_line_follower")
    pub_motor = rospy.Publisher("/motor", Int8MultiArray, queue_size=1)
    r = rospy.Rate(10)
    s = rospy.Time().now().secs
    while not rospy.is_shutdown():
        motor = Int8MultiArray()
        motor.data = [10,10]
        pub_motor.publish(motor)
        if rospy.Time().now().secs - s > 5:
            motor.data *= -1
            s = rospy.Time().now().secs
        r.sleep()