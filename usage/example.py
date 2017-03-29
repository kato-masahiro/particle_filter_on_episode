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

while True:
    decision_making([100,200,399,400])
    set_reward(1.0)
    see_distribution():
