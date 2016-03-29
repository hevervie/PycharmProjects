#!/usr/bin/env python
#coding=utf-8
__author__ = 'zhoupana'
#mosi . --> 0 - -->1

#导入系统模块
import sys

#定义编码字典
drit={'a':'01',   'b':'1000', 'c':'1010', 'd':'100',  'e':'0',
      'f':'0010', 'g':'110',  'h':'0000', 'i':'00',   'j':'0111',
      'k':'101',  'l':'0100', 'm':'11',   'n':'10',   'o':'111',
      'p':'0110', 'q':'1101', 'r':'010',  's':'000',  't':'1',
      'u':'001',  'v':'0001', 'w':'011',  'x':'1001', 'y':'1011',
      'z':'1100',

      '1':'01111', '2':'00111', '3':'00011', '4':'00001', '5':'00000',
      '6':'10000', '7':'11000', '8':'11100', '9':'11110', '0':'11111',

      '.':'010101',':':'111000', ',':'110011',';':'101010','?':'001100',
      '=':'10001', '!':'101011', '-':'100001','_':'001101','(':'10110',
      ')':'101101','$':'0001001','&':'01000','@':'011010','+':'01010',
      "'":'011110','/':'10010',
      ' ':' '
      }
#定义解码字典
drit_reversed={}

#反转编码字典得到解码字典
for key,value in drit.items():
    drit_reversed[value]=key

#加密，并写入文件
def EncodeReadFile():
      #加密文件
      encode=open("1.encode",'r')
      #解密文件
      decode=open("1.decode",'w')
      #迭代整合文件
      for string in encode.readlines():
            print(string,end="")
            for str in string:
                  try:
                        decode.write(drit[str.lower()])
                        decode.write(" ")
                  except KeyError:
                        pass
            decode.write("\n")
#解密，输出到文件到你中，并显示在屏幕上
def DecodeReadFile():
      #加密文件
      encode=open("2.encode",'w')
      #解密文件
      decode=open("1.decode",'r')
      #迭代整个文件
      for string in decode.readlines():
            #将读取的一行用空格分隔开
            result=Split(string)
            for str in result:
                  try:
                       print(drit_reversed[str],end="")
                       encode.write(drit_reversed[str])
                  except KeyError :
                        encode.write(drit_reversed[" "])
                        print(" ",end="")
            encode.write("\n")
            print()
#加密
def Encode():
      string=input()
      for str in string:
            print(drit[str.lower()],end=' ')
            if(str == ' '):
                  print("",end='')
#字符串分割
def Split(String):
      ret=[]
      j=0
      for i in range(0,len(String)):
            if(String[i] == ' '):
                  if(i == 0):
                        pass
                  elif(i == j):
                        ret.append(String[j])
                  else:
                        ret.append(String[j:i])
                  j=i+1
      return ret
#解码
def Decode():
      string=input()
      result=Split(string)
      for str in result:
            try:
                  print(drit_reversed[str],end="")
            except KeyError :
                  print(" ",end="")
#测试
def Test():
      while True:
            key=input()
            print(drit[key])
#主函数
def main():
      try:
            if(sys.argv[1] == "encode"):
                  Encode()
            elif(sys.argv[1] == "decode"):
                  Decode()
            else:
                  print("Usage:  python Test.py encode/decode")
      except IndexError:
            print("Usage:   python Test.py encode/decode")
if __name__ == '__main__':
      #main()
      #print(drit_reversed[''])
      #Encode()
      #Decode()
      #解密
     # DecodeReadFile()
      #加密
      EncodeReadFile()
