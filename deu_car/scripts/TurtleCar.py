#! /usr/bin/env python

import rospy

from TempKeyInput import TempKeyInput

from DriveTurtle import DriveTurtle

if __name__ == "__main__":
    rospy.init_node('deu_car')
    temp = TempKeyInput()
    drive = DriveTurtle()
    rate = rospy.Rate(10)

    print "start"
    while not rospy.is_shutdown():
        input = temp.getKey()

        if input == 'p':
            print "exit"
            break
        elif input == 'k':
            drive.forceStop()
        elif input == 'w':
            drive.increaseSpeed()
        elif input == 's':
            drive.decreaseSpeed()
        elif input == 'a':
            drive.increaseLeftTurn()
        elif input == 'd':
            drive.increaseRightTurn()
        elif input == 'q':
            drive.turnLeft()
        elif input == 'e':
            drive.turnRight()

        drive.publish()
        rate.sleep()
