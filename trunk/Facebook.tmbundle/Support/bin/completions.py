#!/usr/bin/env python
# encoding: utf-8
import os
env = os.environ.get
import sys
sys.path.append(env("TM_SUPPORT_PATH")+"/lib")

import dialog
from tm_helpers import sh
import re



word = env('TM_CURRENT_WORD') 
if not word: word = ""
 
functions = sh('grep -i "^$TM_CURRENT_WORD" "$TM_BUNDLE_SUPPORT"/functions.txt').split("\n")

functions.pop()


if len(functions) > 1:
  skip_prefix = False
  if word and word[-1] == '_':
    # If the last char in the word is a _ we don't show the word in the completion list,
    # to enable the user to continue typing. See: array_⌥⎋
    skip_prefix = True
  names = [] 

  regex = re.compile(word+"(.*?)(%|$)")
  for line in functions :

    mat = regex.match(line)
    if skip_prefix:
      names.append(mat.group(1))
    else:
      names.append(word + mat.group(1))
  
  choice = dialog.menu(names)
  if not choice:
    exit()
  choice_check = choice 
  if skip_prefix:
    choice_check = word + choice
  choice = [f for f in functions if f[0:len(choice_check)]==choice_check].pop()
else:
  choice = functions.pop()


function, prototype = choice.split('%')

offset = len(word) 
  

sys.stdout.write(function[offset:] + '(')

parts = prototype.split(',')
tab = 0
l = len(parts) 
for tab in range(1,l+1):
  sys.stdout.write("${" + str(tab) +":" + parts[tab-1].strip().replace("$", "\\$") + "}")
  if tab <> l : print ", ",

print ")$0",

