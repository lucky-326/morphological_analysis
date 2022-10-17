#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#--------------------------------------------------------------------------
#
#最終更新：2022/10/17
#
#--------------------------------------------------------------------------


# In[12]:


#各libraryをimport
from janome.tokenizer import Tokenizer
import tkinter
from tkinter import filedialog,Tk
from tkinter import messagebox
import os


# In[13]:


#janomeのインスタンスを作成
t = Tokenizer()


# In[14]:


#inputファイルのパスを取得
root = tkinter.Tk()                   #ウインドウを生成
root.attributes('-topmost', True)     #topmost指定(最前面に配置)
root.withdraw()                       #空のルートウインドウを非表示
root.focus_force()                    #ウインドウにフォーカスを当てる

typ = [('テキストファイル','*.txt')]  #ダイアログで開くファイルの識別子を指定
dir = 'C:'                            #ダイアログの初期表示ディレクトリの場所を指定
path = filedialog.askopenfilename(filetypes =  [('テキストファイル','*.txt')], initialdir = dir) #inputファイルのPATHをファイルダイアログで取得


# In[15]:


#inputファイルを読み込んでresult.txtに解析結果をoutputする
def writeFile():

    f = open(path, 'r', encoding="utf-8_sig")
    data = f.read()

    with open(r'result.txt', 'w', encoding="utf-8_sig") as fp:
        for token in t.tokenize(data):
            fp.write(str(token))
            fp.write("\n")

    f.close()


# In[17]:


#形態素解析完了メッセージをポップアップする
def endMsg():
    
    messagebox.showinfo('形態素解析', '形態素解析が完了しました')


# In[18]:


#result.txtが存在するか確認
resultFile = 'result.txt'
is_file = os.path.isfile(resultFile)

#result.txtの存在と上書きするかどうかを判定
if is_file:
    hantei = messagebox.askokcancel('確認', 'result.txtが存在しますが上書きしてもよろしいですか？')
       
    if hantei == True:
        writeFile()
        endMsg()
    
else:
    writeFile()
    endMsg()


# In[ ]:




