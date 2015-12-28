import sys
import re 

regex = re.compile("function (.*?)\((.*?)\)")
for l in sys.stdin:
  columns = l.split("\t")
  if len(columns) == 4  and columns[3]=="f\n":
    mat = regex.search(columns[2])
   
    if mat:
      print columns[0] + "%" + mat.group(2)
      
      