
# coding: utf-8

# In[1]:


import os,sys
import codecs


# In[4]:


path = 'C:\\Users\\**'
mylist = os.listdir(path)


# In[7]:


for file in mylist:

  data = file.replace("", "")
  data_modified = data.replace("_", " ")

  file = codecs.open("testfile.txt","+a","utf-8")
  file.write(data_modified+"\n")
  file.close()


# In[40]:


def list_all_file_name(root='C:\\Users\\xx',write_to=codecs.open('./default.txt','+w','utf-8'),
                       recursion=True,indentation=''):
    if os.path.isdir(root):
        file_list=os.listdir(root)
#         file=codecs.open('list_file.txt','+w','utf-8')
        for file in file_list:
            write_to.write(indentation + file+"\n")
            if os.path.isdir(root+"\\"+file) and recursion:
                list_all_file_name(root+"\\"+file, write_to, indentation + "  ")
            
    else:
        write_to.write(indentation + file)
        


# In[37]:


list_all_file_name("C:\\Users\\**",codecs.open('list_file.txt','+w','utf-8'))


# In[41]:


list_all_file_name("D:\github",codecs.open('list_file.txt','+w','utf-8'), False)

