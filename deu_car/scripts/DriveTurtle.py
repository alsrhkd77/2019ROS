#! /usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

class DriveTurtle:

    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=5)
        self.speed = 0
        self.turn = 0
        self.twist = Twist()
        self.twist.linear.x = 0
        self.twist.linear.y = 0
        self.twist.linear.z = 0
        self.twist.angular.x = 0
        self.twist.angular.y = 0
        self.twist.angular.z = 0


    def getTwist(self):
        self.twist.linear.x = self.speed
        self.twist.linear.y = 0
        self.twist.linear.z = 0
        self.twist.angular.x = 0
        self.twist.angular.y = 0
        self.twist.angular.z = self.turn
        return self.twist


    def increaseSpeed(self):
        self.speed += 0.1
        if(self.speed > 1):
            self.speed = 1


    def decreaseSpeed(self):
        self.speed -= 0.1
        if (self.speed < -1):
            self.speed = -1


    def increaseLeftTurn(self):
        self.turn += 0.2
        if(self.turn > 2):
            self.turn = 2


    def increaseRightTurn(self):
        self.turn -= 0.2
        if(self.turn < -2):
            self.turn = -2


    def forceStop(self):
        self.speed = 0
        self.turn = 0

    def turnLeft(self):
        self.speed = 0
        self.turn = 2

    def turnRight(self):
        self.speed = 0
        self.turn = -2

    def publish(self):
        self.pub.publish(self.getTwist())
        if self.turn > 0:
            self.turn -= 0.1
            if self.turn < 0.2:
                self.turn = 0
        elif self.turn < 0:
            self.turn += 0.1
            if self.turn > -0.2:
                self.turn = 0



if __name__=="__main__":
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node("turtle_car")
    drive = DriveTurtle()
    rate = rospy.sleep(10)
    twist = Twist()
    while not rospy.is_shutdown():
        drive.increaseSpeed()
        twist = drive.getTwist()
        pub.publish(twist)
        rate.sleep()
