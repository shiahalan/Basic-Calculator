from ast import Delete
from logging import exception
from tkinter import Tk
from Variables.variables import *
ans=0
calcerror=str()
class Calculator():
 
    def __init__(self, s):
        self._s = s
        self._i = 0
        self._len = len(s)
        self._err = False
    
    def next(self):
        self._i += 1
        
    def take(self):
        l = self._len
        j = i = self._i
        s = self._s
        if j<l and s[j] == '(':
            self.next()
            n = self.calc()
            if s[self._i] != ')':
                raise Exception()
            self.next()
            return n
        while j < l and s[j].isdigit():
            j += 1
        self._i = j
        if i == j:
            raise Exception()
        return int(s[i:j])
        
    def poww(self):
        res = self.take()
        l = self._len
        s = self._s
        while self._i < l and s[self._i] == '^':
            self.next()
            num = self.take()
            res = res**num
        return res
    
    def mul_div(self):
        global calcerror
        res = self.poww()
        l = self._len
        s, i = self._s, self._i
        while self._i < l and s[self._i] in ('/', 'x'):
            op = s[self._i]
            self.next()
            num = self.poww()
            if op == 'x':
                res *= num
            if op == '/':
                if num==0:
                  calcerror="error division"
                else:
                  res /= num
        return res
    
    def plus_minus(self):
        res = self.mul_div()
        l = self._len
        s, i = self._s, self._i
        while self._i < l and s[self._i] in ('+', '-'):
            op = s[self._i]
            self.next()
            num = self.mul_div()
            if op == '+':
                res += num
            if op == '-':
                res -= num
        return res
    
    def calc(self):
        try:
            return self.plus_minus()
        except:
            if not self._err:
                print('Parsing Error at index {}'.format(self._i))
            self._err = True
        return None

def edit_numbers(num):
  global first
  text.config(state=tk.NORMAL)
  if first==True:
    text.delete("1.0", tk.END)
  text.insert(tk.END, num)
  first=False
  text.config(state=tk.DISABLED)
    

def add_signe(op):
  global first
  global calcerror
  global answer
  text.config(state=tk.NORMAL)
  if first==True:
    if calcerror !="":
      calcerror=""
      text.delete("1.0", tk.END)
      text.insert(tk.END, answer)
    first=False
  text.insert(tk.END, op)
  first=False
  text.config(state=tk.DISABLED)


def calculate():
  global first
  global calcerror
  global answer
  calcerror=""
  exp=text.get("1.0",tk.END)
  answer=int()
  i=Calculator(exp).calc()

  text.config(state=tk.NORMAL)
  text.delete("1.0","end")
      
  if calcerror:
    text.insert("1.0", calcerror)
    first=True
  else:
    answer=i
    text.insert("1.0", answer)
  text.config(state=tk.DISABLED)
  first=True;
  return ans
