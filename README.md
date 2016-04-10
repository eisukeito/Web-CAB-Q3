## Web-CAB Q3 Solver

Web-CABの第3問「関数」を解くためのプログラム．
図形a, 図形b, 図形c, 図形dに対する関数を適用すると、解が得られる．

### 使用例

```
  >>> import cab
  >>> problem = cab.cab_list()
  >>> print problem
  ['a', 'b', 'c', 'd']
  >>> print problem.f1().f2().f6().f5().f10()
  ['b', 'rev_TB(a)', 'c', 'd']
```

###　解説

cab_listクラスのインスタンスproblemを生成 

```
  >>> problem = cab.cab_list()
```

- デフォルトインスタンスは図形が4つ．
- 図形が3つの場合は、``cab_list(3)``と指定する．
    
printで状態を表示．初期状態は以下のようにa,b,c,dで符号化してある．

```
  >>> print problem
  ['a', 'b', 'c', 'd']
```

メソッドチェーンを使って適用する関数を順番に指定すると解が得られる．

```
  >>> print problem.f4().f6().f5().f5().f10()
  ['c', 'a', 'b', 'd']
```

#### 命令関数

- f1: 上下を逆さまにする
- f2: 左右を逆さまにする
- f3: 前の図形を消す
- f4: 次の図形を消す
- f5: 前の図形と入れかえる
- f6: 前の命令を取り消す
- f7: 次の命令を取り消す
- f8: 図形の順序を右の要領で入れかえる [1,2,3,4] -> [4,3,2,1] (3つの場合 [1,2,3] -> [3,2,1])
- f9: 図形の順序を右の要領で入れかえる [1,2,3,4] -> [3,4,1,2]
- f10: 図形の順序を右の要領で入れかえる [1,2,3,4] -> [2,1,4,3]
    
#### 結果の記号
-  rev_TB: 上下逆転
-  rev_LR: 左右逆転

``['d', 'c', 'rev_TB(a)', 'b']``のとき、[図形dはそのまま, 図形cはそのまま, 図形aの上下反転, 図形bはそのまま]という意味になる．