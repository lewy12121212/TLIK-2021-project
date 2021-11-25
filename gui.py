from tkinter import *
from tkinter import filedialog
import os
from os.path import exists

import sys
sys.path.insert(0, './lzw-rs-py')

from lzw import compress_file, decompress_file, compress_file_named, decompress_file_named

class LZW_class:


  def __init__(self):
    self.filePath = ""
    self.OryginalFileSize = ""
    self.CompressFileSize = ""
    self.DecompressFileSize = ""

  def browseFiles(self):
    label_file_oryginal_size.configure(text="")
    label_file_compress_size.configure(text="")
    label_file_decompress_size.configure(text="")

    self.filePath = filedialog.askopenfilename(initialdir = "./", title = "Select a File", filetypes = (("Text files","*.txt*"),("all files","*.*")))
    label_file_explorer.configure(text="File Opened: " + self.filePath)
    print("oryginal file path: " + self.filePath)
    self.OryginalFileSize = os.path.getsize(self.filePath)
    label_file_oryginal_size.configure(text="Oryginal size: " + str(self.OryginalFileSize) + "B")

  def compress(self):
    if self.filePath == "":
      label_file_explorer.configure(text="No file to compress")
    else:
      label_file_explorer.configure(text="File Opened: " + self.filePath)
      compress_file_named(self.filePath, "./compress.lzw")
      self.CompressFileSize = os.path.getsize("./compress.lzw")
      label_file_compress_size.configure(text="Compress size: " + str(self.CompressFileSize) + "B")
      #print(str(self.CompressFileSize) + "\n" + str(self.ToCompressFileSize))

  def decompress(self):
    if exists("./compress.lzw"):
      decompress_file_named("./compress.lzw", "./decompress")
      self.DecompressFileSize = os.path.getsize("./decompress")
      label_file_decompress_size.configure(text="Decompress size: " + str(self.DecompressFileSize) + "B")
    else:
      label_file_explorer.configure(text="File not exists")
    
if __name__=="__main__":
  window = Tk()
  window.title('LZW')
  window.geometry("978x500")
  window.config(background = "white")

  lzwc = LZW_class()
  #lzwc.browseFiles()
  # Create a File Explorer label
  label_file_explorer = Label(window, text = "Please - choose file to compress", font = ('Arial 14 bold'), width = 75, height = 1, fg = "white")

  label_file_oryginal_size = Label(window, text = "", font = ('Arial 14 bold'), width = 75, height = 1, fg= "white")
  label_file_compress_size = Label(window, text = "", font = ('Arial 14 bold'), width = 75, height = 1, fg= "white")
  label_file_decompress_size = Label(window, text = "", font = ('Arial 14 bold'), width = 75, height = 1, fg= "white")

  button_explore = Button(window, text = "Choose file to compress", font = ('Arial 14 bold'), command = lambda: lzwc.browseFiles(), width = 30)
  compress_bt = Button(window, text = "Compress", font = ('Arial 14 bold'), command = lambda: lzwc.compress(), width = 30)
  decompress_bt = Button(window, text = "Decompress", font = ('Arial 14 bold'), command = lzwc.decompress, width = 30)
  button_exit = Button(window, text = "EXIT", font = ('Arial 14 bold'), command = exit, width = 30)
  label_file_explorer.grid(column = 1, row = 1)
  label_file_oryginal_size.grid(column = 1, row = 2)
  label_file_compress_size.grid(column = 1, row = 3)
  label_file_decompress_size.grid(column = 1, row = 4)
  
  button_explore.grid(column = 1, row = 5, pady=5)
  compress_bt.grid(column = 1, row = 6, pady=5)
  decompress_bt.grid(column = 1, row = 7, pady=5)
  button_exit.grid(column = 1,row = 8, pady=5)

  window.mainloop()
