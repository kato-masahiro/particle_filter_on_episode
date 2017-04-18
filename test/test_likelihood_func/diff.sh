#!/bin/bash
#coding:utf-8

./test/test_likelihood_func/test.sh ./test/test_likelihood_func/sensor_val.txt > result
diff result ./test/test_likelihood_func/ref
echo $?
