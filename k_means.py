#!/bin/env python
#coding:utf-8
import random
import math

def classification(data,class_num):
    M = 10
    C = 0
    data_num = len(data)
    data_dimension = len(data[0])
    classification = [0] * data_num
    for i in range(data_num):
        classification[i] = random.randint(0,class_num-1)
    centroid = [[ 0.0 for i in range(data_dimension)] for j in range(class_num)]

    while C < M:
        C += 1
        #重心を求める
        counter = 0
        for i in range(class_num):

            for ii in range(data_num):
                if i == classification[ii]:
                    counter += 1
                    for iii in range(data_dimension):
                        centroid[i][iii] += data[ii][iii]
            if counter != 0:
                for iii in range(data_dimension):
                    centroid[i][iii] /= counter
                counter = 0

        #重心を用いて再クラスタリング
        old_classification = classification[:]
        print "old_classification",old_classification

        length_from_centroid = [[ 0.0 for i in range(class_num)] for j in range(data_num)]
        for d_n in range(data_num):
            for c_n in range (class_num):
                for d_d in range(data_dimension):
                    length_from_centroid[d_n][c_n] += (data[d_n][d_d] - centroid[c_n][d_d]) ** 2
                length_from_centroid[d_n][c_n] = math.sqrt(length_from_centroid[d_n][c_n])

        for d_n in range(data_num):
            classification[d_n] = length_from_centroid[d_n].index(min(length_from_centroid[d_n]))

        #変化がなければ終了
        if classification == old_classification:
            break

    print "data_num:",data_num
    print "data_dimension:",data_dimension
    print "class_num:",class_num
    print "old_classification:",old_classification
    print "classification:",classification
    print "centroid:",centroid
    print "length_from_centroid:",length_from_centroid
    return classification
