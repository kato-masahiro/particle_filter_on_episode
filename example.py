#!/bin/env python
#coding:utf-8

"""
Concrete example of how to use module "PFoE.py"
"""
import PFoE 

#Define your robot with an arbitrary numbers of sensors and choices.
robot = PFoE.Robot(sensor=4,choice=3)

#If you want to implement "Retrospective Resetting",
#you have to define threshold.
robot = PFoE.Robot(sensor=4,choice=3,threshold=0.5)

while 1:
    #You somehow need to get sensors val.
    #The robot as defined above has 4 sensors,
    # then a suitable input is a list of for numbers.
    #For example,[192,1182,903,331]
    robot.sensor = [192,1182,903,331]

    #Robot update his belief with input.
    robot.update()

    #Robot decide a choice which he think the best.
    #Robot defined above having 3 choices,
    # so he return three kinds integers 0,1,or 2.
    #typically,this means fowawrd,right turn,left turn,for example.
    action = robot.decision_making()

    #Follow his decision,please move robot actually.
    #As a result,robot will get some value as a reward.
    #For example, -0.5
    reward = -0.5

    #By a series of events,the robot gained the following experience.
    #-He got the sensor value[192,1182,903,331],
    #  and took an action against it.
    #-As a result,he got "-0.5" as a reward of his action.
    #Then,you need to add this series of events at his memory.
    robot.add_event(robot.sensor,action,reward)

    #If you want to check robot's beliefe space and particle's distribution,
    # type this.
    robot.see_distribution()
