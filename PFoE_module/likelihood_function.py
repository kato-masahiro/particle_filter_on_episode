#coding:utf-8

import math

def likelihood_function(sensor,past_sensors):
    """
    概要:尤度関数を定義する.
         過去のエピソードで取得されたセンサ値と、現在取得したセンサ値
         を比較し、適切な尤度を返す。
         具体的な関数の内容は使用者が考えて実装する。

    処理:センサ値のリスト(1×センサ数)と過去のセンサ値のリスト(センサ数×エピソード数)を受け取り、
         尤度のリスト(1×エピソード数)を返す

    引数:sensor[],past_sensors[[]]

    戻り値:likelihood[]
    """
    likelihood = [0.0 for i in range( len(past_sensors) )  ]
    n = [0.0 for i in range( len(sensor) ) ]

    """
    このループ内で尤度関数の内容を定義せよ
    """
    for i in range( len(past_sensors) ):
        if len( past_sensors[i] ) != len(sensor):
            print "* エラー *: センサ数が異なる(likelihood_func.py)"
            exit(1)
        for ii in range( len(sensor) ):
            n[ii] += math.fabs( sensor[ii] - past_sensors[i][ii] )
        likelihood[i] = 0.5 ** sum(n)

        n = [0.0 for i in range( len(sensor) ) ]

    return likelihood

if __name__ == '__main__':
    sensor,episode = input()   
    print func(sensor,episode)
