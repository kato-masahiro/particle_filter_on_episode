#!/bin/bash
#coding:utf-8

./test.sh sensor_val.txt > result
diff result ref
echo $?
