#!/bin/bash
#coding:utf-8

#引数にセンサ値の入ったテキストファイルを取る
if [ "$#" -eq 0 ];then
    echo "引数としてセンサ値の入ったテキストファイルを指定してください"
    exit 1
fi

#センサ値がいくつあるか
input_num=$(cat $1 | wc -l)
past=$(cat $1 | tr '\n' ',' | sed -e 's/,$//') #センサ値の改行をカンマに直し、最後のカンマを削減

for n in $(seq 1 $input_num)
do
    sen=$(sed -n "$n"p sensor_val.txt)
    echo ===
    echo sensor: "$sen"
    echo past: "$past"
    echo likelihood:
    echo "$sen",[ "$past" ] | python ../../PFoE_module/functions/likelihood_function.py
done
