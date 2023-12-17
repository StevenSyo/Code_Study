# 点数を入力して、平均点の計算
def input_scores(name):
    print('{}さんの試験結果を入力してください。'.format(name))
    network = int(input('network point?'))
    database = int(input('database point?'))
    security = int(input('security point?'))
    scores = [network, database, security]
    return scores #　ローカル変数scoresは、この関数以外のところいけないただし、関数の実行結果になる

def calc_average(scores):
    avg = sum(scores) / len(scores)
    print('平均点は{}'.format(avg))

scores = input_scores("Steven") #　input_scores()関数の計算結果を、次の関数の仮引数に代入
calc_average(scores)

'''
戻り値 return value

def 関数名(引数1,引数2,...):
    処理
    return 値

変数 = 関数名(引数1,引数2,...)
↓  ↓  ↓ イコール ↓ ↓ ↓
変数 = 関数名のreturn 値

戻り値を受け取る変数名 = 関数名(引数1,引数2,...)

*もしreturn文がない場合、returnは「None」、空っぽのけっかです。
'''

# どんどん代入して計算します。
def puls(x,y):                # puls関数を定義
    answer = x + y
    return answer             # puls関数の計算結果を戻し　puls(x,y

answer = puls(100,50)            
# 引数を代入して、puls(100,50)計算して、「puls(100,50)」が「150」になる。そして、「150」はanswerに代入
print("足し算の答えは{}です".format(answer))   # answerの結果をprint関数に出し

