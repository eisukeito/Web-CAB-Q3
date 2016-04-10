# -*- coding: utf-8 -*-

class cab_list():
    '''
    Web-CABの第3問「関数」を解くためのプログラム

    # cab_listクラスのインスタンスproblemを生成 
    > problem = cab_list()
    # デフォルトは図形が4つ．cab_list(3)で図形が3つの場合にも対応
    
    # printで状態を表示．初期状態は以下のようにa,b,c,dで符号化してある．
    > print problem
    ['a', 'b', 'c', 'd']

    # メソッドチェーンで適用する関数を順番に指定すると答えが得られる
    > print problem.f4().f6().f5().f5().f10()
    ['c', 'a', 'b', 'd']

    # 命令関数
    # f1: 上下を逆さまにする
    # f2: 左右を逆さまにする
    # f3: 前の図形を消す
    # f4: 次の図形を消す
    # f5: 前の図形と入れかえる
    # f6: 前の命令を取り消す
    # f7: 次の命令を取り消す
    # f8: 図形の順序を右の要領で入れかえる [1,2,3,4] -> [4,3,2,1]
    #     (3つの場合 [1,2,3] -> [3,2,1])
    # f9: 図形の順序を右の要領で入れかえる [1,2,3,4] -> [3,4,1,2]
    # f10: 図形の順序を右の要領で入れかえる [1,2,3,4] -> [2,1,4,3]

    # 命令記号
    # rev_TB: 上下逆転
    # rev_LR: 左右逆転
    ['d', 'c', 'rev_TB(a)', 'b']
    -> [図形dそのまま, 図形cそのまま, 図形aの上下反転, 図形bそのまま]
    '''
    import copy

    state = []
    history = []
    def __init__(self, num=4):
        if num == 3:
            self.state = ['a','b','c']
        else:
            self.state = ['a','b','c','d']
        self.history = []
        self.save(self.state)
        self.undo_next = False
    
    def __str__(self):
        return str(self.state)
    
    def current_idx(self):
        return len(self.history)-1
    
    def save(self, state):
        current_state = copy.deepcopy(state)
        self.history.append(current_state)
    
    def check_prev_lock(func):
        import functools
        @functools.wraps(func)
        def wrapper(self,*args,**kwargs):
            if self.undo_next:
                self.undo_next = False
                self.save(self.state)
                return self
            else:
                return func(self,*args,**kwargs)
        return wrapper
    
    @check_prev_lock
    def f1(self):
        idx = self.current_idx()
        self.state[idx] = 'rev_TB(' + self.state[idx] + ')'
        self.save(self.state)
        return self
    
    @check_prev_lock
    def f2(self):
        idx = self.current_idx()
        self.state[idx] = 'rev_LR('+ self.state[idx] + ')'
        self.save(self.state)
        return self
    
    @check_prev_lock
    def f3(self):
        idx = self.current_idx()
        self.state[idx-1] = ''
        self.save(self.state)
        return self
    
    @check_prev_lock
    def f4(self):
        idx = self.current_idx()
        self.state[idx+1] = ''
        self.save(self.state)
        return self
     
    @check_prev_lock
    def f5(self):
        idx = self.current_idx()
        if idx == 0:
            assert IndexOutofRange
        else:
            tmp = self.state[idx]
            self.state[idx] = copy.deepcopy(self.state[idx-1])
            self.state[idx-1] = copy.deepcopy(tmp)
            self.save(self.state)
            return self
    
    @check_prev_lock
    def f6(self):
        self.state = copy.deepcopy(self.history[-2])
        self.save(self.state)
        return self
    
    @check_prev_lock
    def f7(self):
        idx = self.current_idx()
        self.undo_next = True
        self.save(self.state)
        return self
    
    @check_prev_lock
    def f8(self):
        self.state.reverse()
        self.save(self.state)
        return self
        
    @check_prev_lock
    def f9(self):
        tmp = copy.deepcopy(self.state)
        self.state[0] = tmp[2]
        self.state[1] = tmp[3]
        self.state[2] = tmp[0]
        self.state[3] = tmp[1]
        self.save(self.state)
        return self
    
    @check_prev_lock
    def f10(self):
        tmp = copy.deepcopy(self.state)
        self.state[0] = tmp[1]
        self.state[1] = tmp[0]
        self.state[2] = tmp[3]
        self.state[3] = tmp[2]
        self.save(self.state)
        return self
