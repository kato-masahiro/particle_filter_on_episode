#coding:utf-8

def func(sensor,episode):
    """
    概要:尤度関数を定義する.
         過去のエピソードで取得されたセンサ値と、現在取得したセンサ値
         を比較し、適切な尤度を返す。
         具体的な関数の内容は使用者が考えて実装する。

    処理:センサ値(1次元リスト)とエピソード集合(多次元リスト)を受け取り、
         エピソードの数だけの尤度が入ったリストを返す

    引数:sensor[],episode[]

    戻り値:likelihood[]
    """

    likelihood = [0.0 for i in range( len(episode) )  ]
    n = [0.0 for i in range( len(sensor) ) ]

    """
    このループ内で尤度関数の内容を定義せよ
    """
    for i in range( len(likelihood) ):
        for ii in range( len(sensor) ):
            n[ii] += math.fabs( sensor[ii] - episode[i][0][ii] )
        likelihood[i] = 0.5 ** sum(n)

    return likelihood

