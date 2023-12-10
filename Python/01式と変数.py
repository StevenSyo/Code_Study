# 1.0 変数とデータ型　variate

# 1.1 式と演算
print(1 + 0)
print(8 - 6)
print(1 * 3)
print(4 / 1)    # 割り算の結果は小数
print(30 // 6)  # 割り算の結果は整数
print(41 % 6)   # 割り算の結果は余り
print(3 ** 3)   # 立方根の計算の結果

# 文字列の演算
## 一回文字列の連結
print('1' + '1')
## 文字列の反復
print('コーヒーが' + 'とても' * 3 + '美味しかった')

#　エスケープシーケンス（escape sequence）特殊な記号、文字列は対象
print('参照:初めまして、私は蕭蕭と申します。Azureエンジニアです。どうぞよろしくお願いいたします。')
## \n 改行
print('初めまして、私は蕭蕭と申します。\nAzureエンジニアです。どうぞよろしくお願いいたします。')
## \\　バックスラッシュ　反斜杠　テストして
print('初めまして、私は蕭蕭と申します。"Azure\"エンジニアです。どうぞよろしくお願いいたします。')
print('初めまして、私は蕭蕭と申します。\\Azure\\エンジニアです。どうぞよろしくお願いいたします。')
## \'　シングルクォーテーション　テストして
#print('初めまして、私は蕭蕭と申します。'Azure'エンジニアです。どうぞよろしくお願いいたします。')
print('初めまして、私は蕭蕭と申します。\'Azure\'エンジニアです。どうぞよろしくお願いいたします。')
## \"　ダブルクオーテーション　テストして
print('初めまして、私は蕭蕭と申します。"Azure"エンジニアです。どうぞよろしくお願いいたします。')
print('初めまして、私は蕭蕭と申します。\"Azure\"エンジニアです。どうぞよろしくお願いいたします。')

# 1.1.4　式と評価 expression
## オペランド operand | 演算子 operator | 評価 evaluation
'''
演算子の優先順位
高 **
中 *,/,%
低 +,-
'''
## 優先のテスト
print(1 + 3 * 3 / 3 - 1)
print((1 + 3) * 3 / (3 - 1))
print(1 + 3 * 3 ** 3 / 3 - 1)
print((1 + 3) * 3 ** 3 / (3 - 1))
# print(1 + '1') 数字と文字列の評価はエラー

# 1.2 変数
## 1.2.1 変数の利用 
print('半径が3CMの円の直径は:')
print(3 * 2)
print('半径が3CMの円の直径は:,直径×円周率を求めるのは:')
print(3 * 2 * 3.1415926)

name = '松田'
age = 23
print( name )
print( age )

print('半径が3CMの円の直径は、')
dia = 3 * 2
print( dia )
print('その円の円周の長さは、')
print(dia * 3.14)
perimeter = dia *3.14
print('半径が3CMの円の直径は{}、その円の円周の長さは{}です。'.format(dia,perimeter))
print(f'半径が3CMの円の直径は{dia}、その円の円周の長さは{perimeter}です。')

## 1.2.2 変数名のルール
'''
①予約語(keyword)は使用できない
Example:if,for,global,with...

②先頭の文字は数字であってはならない
Example:1,2,3,4,5,6,7...

③先頭に_(アンダースコア)を２つ付けた名前は原則として使用しない
Example:_

④大文字/小文字,全角/半角は区別される
Example:Aa,Bb,Cc,Dd,Ee,Ff...

⑤小文字で始まるわかりやすい名前が望ましい
Example:dia
'''

## 1.2.3 変数の上書き
'''
原則として、以下のように変数の再利用は避けることを勧めです。
'''
age = '23'
print('今年、私は'+ age + '歳です。')

age = '24'
print('今年、私は'+ age +'歳です。')

########################################### 予約語の調査方法 ###########################################
import keyword
print(keyword.kwlist)

## 1.2.4 まとめて代入(アンパック)
name,age = '浅木',23
print('私は{}です。今年は{}歳です。'.format(name,age))

## 1.2.5 自分自身への代入
age = 23
print(f'私は浅木です。今年は{age}です。')
age = age + 1
print(f'来年は{age}です。')
age = age + 1
print('再来年は{}です。'.format(age))

## 1.2.6 複合代入演算子
age = 23
print(age)
age += 2   # 23 + 2 = 25 → age
print(age)
age -= 5   # 25 - 5 = 20 → age
print(age)
age *= 5   # 20 * 5 = 100 → age
print(age)
age /= 4   # 100 / 4 = 25 → age
print(age)

## 1.2.7 キーボード入力値の代入
'''
変数名 = input(文字列)

注意:input関数により、入力した内容は、文字列です。もし、「1」,「0.1」など数字を入力して、
intデータ型あるいはfloatデータ型として利用したい場合、int(),float()関数を利用してください。
'''
name = input('あなたの名前を入力してください\n>>')
print('こんにちは！' + name + 'さん！')

price = input('料金を入力\n>>')
number = input('人数を入力\n>>')
price = int(price)
number = int(number)
payment = price // number
payment = str(payment)
print('お支払いは' + payment + '円です。')
 
# 1.3 データ型
## 1.3.1 データ型とは
'''
主なデータ型
int 整数
⇒100,-100
float 小数
⇒3.14,-5
str 文字列
⇒"Hello","食事"
bool 真偽値
⇒True,False
'''

######################################### データ型の調べ方法 ##############################################
#　type関数
x = input('文字列を入力してください。\n>_:')
type1 = type(str(x))
x = input('整数を入力してください。\n>_:')
type2 = type(int(x))
x = input('小数を入力してください。\n>_:')
type3 = type(float(x))
x = input('任意の数を入力してください。\n>_:')
type4 = type(bool(x))

types = [type1,type2,type3,type4]
# typesStr = sum(types) # TypeErro unsupported operand type(s) for +: 'int' and 'type'
typesNumbers = len(types)
print('データは{}種類があり、それは{}{}{}{}です。'.format(typesNumbers,types[0],types[1],types[2],types[3]))

### 文字列を入れて、typeをprintする
x = 'xiao'
print(x)
print(type(x)) #<class 'str'>
### 整数を入れて、typeをprintする
x = 7
print(x)
print(type(x)) #<class 'int'>
### 小数を入れて、typeをprintする
x = 3.14
print(x)
print(type(x)) #<class 'float'>

## 1.3.2データの変換
'''
関数名: int関数  float関数  str関数  bool関数
例：    int(x)   float(x)  str(x)   bool(x)
'''
# ⇒ int関数:
# ・数値の小数点以下を切り捨て 四捨五入はなし
x = 1.5
x = int(x)
print(x)
x = 1.6
x = int(x)
print(x)
# ・数値として解釈できない文字列の場合はエラー
x = 'XIAO'
#x = int(x)  #发生异常: ValueError
print(x)    #invalid literal for int() with base 10: 'XIAO'

# ⇒ float関数:
x = '7'
x = float(x)
print(x)
# ・数値として解釈できない文字列の場合はエラー
x = 'xiao'
#x = float(x) #发生异常: ValueError
print(x)     #could not convert string to float: 'xiao'

# ⇒ str関数:
x = 10
x = str(x)
print(x)

# ⇒ bool関数:
''' bool型に変換する際 '''
## 整数の場合、0は、Falesに変換される。0以外の整数は、Trueに変換される。
x = 10
x = bool(x)
print(x)
x = 0
x = bool(x)
print(x)
## 小数の場合、0.0は、Falesに変換される。0.0以外の整数は、Trueに変換される。
x = 20.0
x = bool(x)
print(x)
x = 0.0
x = bool(x)
print(x)
## 文字列の場合、""(空)は、Falesに変換される。""(空)以外の文字列は、Trueに変換される。
x = 'Xiao'
x = bool(x)
print(x)
x = ""  # "" or ''は、どちらでも良い。
x = bool(x)
print(x)


# 1.3.3 文字列の中に数値を入れ込み 様々な入れ込み方法があります。
name = 'Steven.x'
age = 31
companyName = 'KGG'
workingAge = 1 + 1 + 0.5
sentence = 'My name is {},I am {} years old.I have been work at {} Company for {} years.'
print('My name is Stevn.xiao,I am ' + str(age)  + 'years old.I have been work at {} Company for {} years.'.format(name,str(age),companyName,workingAge))
print('My name is {},I am {} years old.I have been work at {} Company for {} years.'.format(name,str(age),companyName,workingAge))
print(f'My name is {name},I am {str(age)} years old.I have been work at {companyName} Company for {workingAge} years.')
print(sentence.format(name,str(age),companyName,workingAge))

# 練習
num = 35+ int(x)
num += 5
GLOBAL = '世界' + str(num) + '箇国'
check_code = num * (9/3)

print('これからBMIを計算します')
hight = int(input('身長(M)を入力してください。\n>>'))
if hight > 2 :
    hight /= 100
else :
    hight = hight  
weight = float(input('体重(KG)を入力してください。\n>>'))
BMI = weight / hight / hight 
print(f'{name}さんのBMIは{BMI}です。')

print('第一章 終了')

