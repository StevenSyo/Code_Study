# 2.0 コレクション collection と コンテナ container

# 2.1 データの集まり
# 2.1.1 変数が持つ不便さ
network = 99
database = 95
security = 90
total = network + database + security
avg = total / 3
print(f'合計点:{total}')
print('平均点:{}'.format(avg))
print('##########################################################')

# 2.2 リスト
# 2.2.1 リストの特徴
member1 = '工藤'
member2 = '松田'
member3 = '浅木'
members = ['工藤','松田','浅木']  # 変数 = [要素1,要素2,要素3...]
print(members)
print('########################')
members = [member1,member2,member3]
print(members)

print(members[0])  # リストの順番は、0から記録します。記録番号の名前は:Index。
print(members[1])
print(members[2])
# print(members[3])  # もし、Indexの値は、入っていない場合、エラーに表示する。IndexError: list index out of range
print('##########################################################')

# 補充
# list は異なるデータ型の要素を同時に含むことができる
myList = ["apple", 42, 3.14, True]  
print(myList)
print(myList[0:3])
print('##########################################################')

# リスト要素の合計と要素数の取得
scores = [88,90,95]
total = scores[0] + scores[1] + scores[2]
print('合計{}点'.format(total))
print('##########################################################')

# sum関数 リスト中のすべての要素の総和を求める。
# sum(リスト) ←←← 注意:リストのみです。他のTypeだとエラーになる。 
scores = [88,91,95]
# x = 1
# total = sum(x) xは、int型であり、エラーになる。 TypeError:'int' object is not interable
total = sum(scores)
print(f'合計{total}点')
print('##########################################################')

# len関数　リスト中の文字列の長さまたは要素の数を計算する
# len(リスト) ←←← 注意:リストのみです。他のTypeだとエラーになる。 
scores = [88,90,95]
total = sum(scores)
avg = total / len(scores) # average関数はありません。この方法で計算できます。
print(type(scores))
print(type(total))
print(type(avg))
print('合計点:{}\n平均点:{}'.format(total,avg))
print('##########################################################')

# 2.2.5 要素の追加・削除・変更
# append関数 要素の追加
# リスト.append(リストに追加したい値)
members = ['工藤','松田','浅木']
members.append('菅原')
members.append('湊')
members.append('朝香')
print(members)
print('##########################################################')

# remove関数 要素の削除
# リスト.remove(リストから削除したい値)
members.remove('菅原')
members.remove('湊')
members.remove('朝香')
print(members)
print('##########################################################')

# リストの要素の変更
# リスト[Index] = [変更したい要素]
members = ['工藤','松田','浅木']
print(members)
members[0] = ['朝香']
print(members)
print('##########################################################')

# 高度な要素の指定
# スライス(slice)による範囲指定
# リスト変数[A:B] A以上の要素(Aは含まれる),B未満の要素(Bは含まれない)
x = [10,20,30,40,50,60,70,80,90]
print(x[0:6]) # 10,20,30,40,50,60 (70はprintしない)
print(x[2:])  # 30,40,50,60,70,80,90 
print(x[:8])  # 10,20,30,40,50,60,70,80 (90はprintしない)
print('##########################################################')

#　負の数による指定 先頭ではなく、末尾からの順番で進める。
x = [10,20,30,40,50,60,70,80,90]
print(x[-1]) # 90
print(x[-2]) # 80
print('##########################################################')

######################################### 補充 ##########################################
members = ['工藤','松田','浅木']
members.reverse() # リスト.reverse ⇒ リストを反転させる
print(members)
print('##########################################################')

# members.copy() リスト.copy ⇒ リストの浅いコピーを作成し、新しいリストを返する
members = ['工藤','松田','浅木']
newList = members.copy()
print(newList)
print('##########################################################')

# members.clear() リスト.clear ⇒ リストを空にし、リスト内のすべての要素を削除する
members = ['工藤','松田','浅木']
newList = members.clear()
print(newList)
print('##########################################################')

# members.count() リスト.count ⇒ リスト内の特定の要素()の数を数える
members = ['工藤','松田','浅木']
x = '工藤'
count = members.count(x) # ()の中に要素を入れてください。
print(count)
x = ['工藤','松田','浅木']
count = members.count(x) #　エラーにならないが、希望の結果は出れない
print(count)
print('##########################################################')

# members.extend(x) リスト.extend ⇒ リストの末尾で他のリスト要素を追加する
members = ['工藤', '松田', '浅木']
x = ['工藤']  # リスト
members.extend(x)  # リストを拡張
print(members)  # members リストが拡張されています
members = ['工藤', '松田', '浅木']
x = ('工藤',)  # タプル (カンマが必要)
members.extend(x)  # タプルを拡張
print(members)  # members リストが拡張されています
print('##########################################################')

# members.index リスト.index ⇒ リスト内で最初に見つかった要素'x'のindexを返す
members = ['工藤','松田','浅木'] 
x = '浅木'
index = members.index(x) 
print(index)
print('##########################################################')

# members.insert リスト.insert ⇒ 指定した位置'i'に要素'x'をリストに挿入する
members = ['工藤','松田','浅木'] 
x = '朝香'
i = 0 # i は　Indexの値
members.insert(i,x)
print(members)
print('##########################################################')

#members.pop リスト.pop ⇒ 指定した位置'i'の要素を削除して返す。位置 i を指定しない場合、デフォルトで最後の要素を削除して返しす
members = ['工藤','松田','浅木'] 
pop = members.pop(0) # # 指定Index[0]の要素を削除して返す
print(f'リスト内容は:{members},削除した内容は:{pop}')

members = ['工藤','松田','浅木'] 
pop = members.pop() # ()は必要である。指定Indexがない場合、末尾の要素を削除して返す
print(f'リスト内容は:{members},削除した内容は:{pop}')
print('##########################################################')

# members.sort  リスト.sort ⇒ リストを昇順でソートし、リストの順序を変更する
members = [1,5,4,2,8,6,7,3,9,0] 
members.sort() # 整数は昇順で並び 0 ⇒ 9
print(members)

members = ['浅木','松田光','工藤新一'] 
members.sort() # 文字列は長さにより、昇順で並び 長 ⇒ 短
print(members)
print('##########################################################')

## numbers.sort(reverse=True) # 降順の場合
members = [1,5,4,2,8,6,7,3,9,0] 
members.sort(reverse=True) # 整数は降順で並び 9 ⇒ 0
print(members)

members = ['浅木','松田光','工藤新一'] 
members.sort(reverse=True)  # 文字列は長さにより、昇順で並び 短 ⇒ 長
print(members)
print('##########################################################')

#################################### ディクショナリ(Dictionary) #########################################33
# ディクショナリの作成
# {}波カッコによってディクショナリを生み出している
# 変数 = {キー1:値,キー2:値,キー3:値...}
scores = {'network':60,'database':80,'security':50} # 'network'、'database'、'security'は キー と呼び。原則的に キー は往復しない
print(scores)
print('network')

scores = {1:10,2.0:20,'30':30,True:40,False:50} #キーのデータ型は、様々な種類ができる。
print(scores) # ここに、なぜTrue:40が出ないのは分からない
print(scores[True]) # ただし、表示されないが、探してprintとすると、出れる
print(scores[False]) # Falseへの影響は無い

# ディクショナリの要素の追加と変更
scores = {'network':60,'database':80,'security':50}
scores['programing'] = 70 # 要素の追加 ディクショナリ[新しいキー] = 新しい値
scores['security'] = 90 #要素の変更 ディクショナリ[変更したい要素のキー] = 変更後の値
print(scores)

# ディクショナリの要素の削除
scores = {'network':60,'database':80,'security':50}
scores['programing'] = 70
print(scores)
del scores['programing']  # del という特殊な構文を用る。 del ディクショナリ[削除したいキー]
print(scores)

# ディクショナリとリストの比較
# ディクショナリは、一つ一つの キー を作成する必要があります。スモークデータの処置に適切
# リストは、Indexで0から、値を保存します。そのため、ビッグデータの処置に使いやすい

# ディクショナリの合計
scores =  {'network':60,'database':80,'security':50}
total = sum(scores.values()) # 関数の式を間違いないように注意してください。
print(total)

# タプルとセット
# リストやディクショナリ以外のデータをまとめる方法があります。

# タプル tuple
# リストとほぼ同じ、ただし、要素の追加、変更、削除はできません
#        タプル                                                   リスト
#        ↓ ↓ ↓                                                    ↓ ↓ ↓
# 変数 = (値1,値2,値3...)                                 変数 = [値1,値2,値3...]
# 書き換えるのない複数データを管理に適切       |      書き換える可能性のあうる複数データを管理に適切
scores = (70,80,90)
print(scores)
print(scores[0])
print('scoresの要素数は:{}'.format(len(scores)))
print(f'scoresの合計は:{sum(scores)}')

# 試してタプルの値を変更すると、エラーになります
scores = (40,50,60)
# scores[0] = 80 # TypeError 'tuple' object does not support item assignment

# また、要素数が 1つ の際に、リストとディクショナリは可能、タプルはエラー
scoresList = [80]                    # データ型は:リスト
scoresDict = {'security':90}         # データ型は:ディクショナリ
scoresTupleInt = (100)               # データ型は:整数  注意:この場合、式 = scorestuplestr = '松田'　
scoresTupleStr = ('松田')            # データ型は:文字列 注意:この場合、式 = scorestuplestr = '松田'　
scoresTuple = ('松田',)              # データ型は:タプル 注意: tupleとして保存したい場合、('松田',)で入力
scoresTupleHy = ('松田',100)
scoresTupleSip = '松田',50 # データ型は:タプル 注意:タプル型の決め手は、()ではなく、','カンマである。ただ、勧めはしない
print(f'scoresListのタイプは:{type(scoresList)}\n\
scoresDictのタイプは:{type(scoresDict)}\n\
scoresTupleIntのタイプは:{type(scoresTupleInt)}\n\
scoresTupleStrのタイプは:{type(scoresTupleStr)}\n\
scoresTupleのタイプは:{type(scoresTuple)}\n\
scoresTupleHyのタイプは:{type(scoresTupleHy)}\n\
scoresTupleSipのタイプは:{type(scoresTupleHy)}\n\
')

# セット set
# 変数 = {値1,値2,値3...}
signal = {'Red','Yellow','Green'}
print(signal)

# セットをリストに比較して、4つの点で異なります
# 1. 重複した値を格納することができない
signal = {'Red','Yellow','Green','Red','red'}  # 'Red'が二回入力したが、表示されない。ただ、エラーにならない
print(signal)
# or
num = {1,2,3,4,5,5} # 5 が二回入力したが、表示されない。ただ、エラーにならない
print(num)

# 2. 添え字やキーという概念がなく、特定の要素に対して代入・参照する方法が存在しない
signal = {'Red','Yellow','Green'}
num = {1,2,3}
# print(signal[0]) # TypeError 'set' object is not subscriptable
# print(num[0]) # TypeError 'set' object is not subscriptable

# 3. 添え字がないため、要素は順序を持たない
signal = {'Yellow','Green','Red'}
num = {1,3,2}
print(signal) # 特別な順序で保存、たとえ{'Yellow','Green','Red'}と入力しても、{'Red', 'Yellow', 'Green'}に変換される
print(num)    # 特別な順序で保存、たとえ{1,3,2}と入力しても、{1, 2, 3}に変換される

# 4. append関数の代わりにadd関数で要素を追加する
signal = {'Yellow','Green','Red'}
num = {1,3,2}
# signal.append(5)  # append関数を使用すると、エラーになる。 AttributeError 'set' object has no attribute 'append'
signal.add(5)  # 他の種類のデータ型の要素を追加しても、OK
# num.append('Red')  # append関数を使用すると、エラーになる。 AttributeError 'set' object has no attribute 'append'
num.add('Red') # 他の種類のデータ型の要素を追加しても、OK
print(signal)  
print(num)
len(signal)
# sum(num) # TypeError unsupported operand type(s) for +: 'int' and 'str'

# 削除は .remove(値) で削除する
signal.remove(5)
print(signal)  
num.remove('Red')
print('信号の種類{}個であり、整数の合計は{}である。'.format(len(signal),sum(num)))

# コレクションたちの別名
# 名                   別名                    説明
# リスト               配列(array)             配列と呼び場合が多い
# ディクショナリ        辞書、マップ(map)       マップは対応表という意味
# タプル               --                     要素の変換できない
# セット               集合                    重複はできなく、順序もないことを示す


# コレクションの応用

# 複数のデータをひとまとまりにして取り扱う方法は、4つがあります。
# リスト　x = [1,2,3] indexと値
# ディクショナリ x = {x:1,y:2,z:3} キーと値 
# タプル x = (3,1,2)  indexと値、決め手は:カンマ','、変更はできない
# セット x = {1,2,3}  重複はできない、順序がない

# コレクションの相互変換
# リストに変換 list関数
scoresTuple = (1,2,3)
scoresSet = {1,2,3}
print(f'\n\
>>>>>>>>>> タイプ 転換前 >>>>>>>>>>\n\
scoresTupleのタイプは:{type(scoresTuple)}\n\
scoresSetのタイプは:{type(scoresSet)}')
# scoresTuple = list(scoresTuple)
# scoresSet = list(scoresSet)
print(f'\n\
>>>>>>>>>> タイプ 転換後 >>>>>>>>>>\n\
scoresTupleのタイプは:{type(list(scoresTuple))}\n\
scoresSetのタイプは:{type(list(scoresSet))}')

# タプルに変換 tuple関数
scoresList = [1,2,3]
scoresSet = {1,2,3}
print(f'\n\
>>>>>>>>>> タイプ 転換前 >>>>>>>>>>\n\
scoresListのタイプは:{type(scoresList)}\n\
scoresSetのタイプは:{type(scoresSet)}')

print(f'\n\
>>>>>>>>>> タイプ 転換後 >>>>>>>>>>\n\
scoresTupleのタイプは:{type(tuple(scoresList))}\n\
scoresSetのタイプは:{type(tuple(scoresSet))}')

# セットに変換 set関数
scoresList = [1,2,3]
scoresTuple = (1,2,3)
print(f'\n\
>>>>>>>>>> タイプ 転換前 >>>>>>>>>>\n\
scoresListのタイプは:{type(scoresList)}\n\
scoresTupleのタイプは:{type(scoresTuple)}')

print(f'\n\
>>>>>>>>>> タイプ 転換後 >>>>>>>>>>\n\
scoresListのタイプは:{type(set(scoresList))}\n\
scoresTupleのタイプは:{type(set(scoresTuple))}')

# ディクショナリをリスト、タプル、セットに変換
# リストへ
scores = {'network':70,'database':80,'security':90}
print(list(scores))              # scoresのキーをリストに変換する
print(list(scores.values()))     # scoresの値をリストに変換する

# タプルへ
scores = {'network':70,'database':80,'security':90}
print(tuple(scores))              # scoresのキーをリストに変換する
print(tuple(scores.values()))     # scoresの値をリストに変換する

# セットへ
scores = {'network':70,'database':80,'security':90}
print(set(scores))              # scoresのキーをリストに変換する
print(set(scores.values()))     # scoresの値をリストに変換する

# リスト、タプル、セットをディクショナリに変換するのはできません
# ディクショナリへの変換は、キーを保存するコレクション と 値を保存するコレクション　2つが必要です。
dictkeys = ['network','database','security']
dictvalues = (70,80,90) 
dictSet = {100,200}
scoresdict = dict(zip(dictkeys,dictvalues))
print(scoresdict)
scoresdict = dict(zip(dictkeys,dictSet))
print(scoresdict)

# ディクショナリの中にディクショナリをネスト(nest,嵌套)
############################################################################
# データ
scoreskey = ['network', 'database', 'security']
nameEn = ['matuda', 'asaki', 'asaka']
nameJp = ['松田', '浅木', '朝香']
point1 = [71, 81, 91]
point2 = [72, 82, 92]
point3 = [73, 83, 93]
# 空のディクショナリを作成
scores = {}
# ネームごとにディクショナリを作成して、scoresに入れる
for i in range(len(nameJp)):
    name = nameJp[i]
    scores[name] = dict(zip(scoreskey, [point1[i], point2[i], point3[i]]))
# Output scores
print(scores)
# 結果
'''
scores = {
    '松田': {'network': 71, 'database': 72, 'security': 73},
    '浅木': {'network': 81, 'database': 82, 'security': 83},
    '朝香': {'network': 91, 'database': 92, 'security': 93}
}
'''
############################################################################

# ディクショナリの中にディクショナリをネスト
key = ['network','database','security']
matuta_points = [71, 81, 91]
asaki_points = [72, 82, 92]
asaka_points = [73, 83, 93]
matuta_scores = dict(zip(key,matuta_points))
asaki_scores = dict(zip(key,asaki_points))
asaka_scores = dict(zip(key,asaka_points))
nameJp = ['松田', '浅木', '朝香']
scores = {}
scores[nameJp[0]] = matuta_scores
scores[nameJp[1]] = asaki_scores
scores[nameJp[2]] = asaka_scores
print(scores)

# ディクショナリの中にセットをネスト　省略

# 2次元リスト
a = [1,2,3]
b = [4,5,6]
c = [a,b] # a と b は、入れ子と言えます
print(c)
print(c[0])    # cのaリストを取り出す
print(c[1][2]) # cのbに行って、aの6を取り出す

# 集合演算
# セットの & 演算
# セット1 & セット2
memberHobbies = {
    '松田':{'SNS','麻雀','自転車'},
    '浅木':{'麻雀','食べ歩き','数学','数学','数学'}
}
print(memberHobbies['松田'])
print(memberHobbies['浅木'])
commonHobbies = memberHobbies['松田'] & memberHobbies['浅木']
print(commonHobbies)

# 4つの集合演算
A = {1,2,3,4}
B = {2,3,4,5}
print(A | B) # 和集合 わしゅうごう    并集
print(A & B) # 積集合 せきしゅうごう  交集
print(A - B) # 差集合 さしゅうごう    差集     本集减去交集
print(A ^ B) # 対称差　たいしょうさ   对称差集 先并集后减去交集

print('第二章 終了')