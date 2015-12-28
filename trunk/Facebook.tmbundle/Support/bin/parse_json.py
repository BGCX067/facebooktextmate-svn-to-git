import simplejson
import sys
obj = simplejson.loads(sys.stdin.readline())
taglist = []

for group in obj:
  if group.has_key("children"):
    taglist += group["children"]

for tag in taglist:
  ret = tag["label"] + "%"
  end = False
  if tag.has_key("attrs") :
    for attr in tag["attrs"]:
      if attr.has_key("req") and attr["req"]:
        ret += attr["label"] + ","
        end = True
  if end:
    print ret[:-1]
  else : 
    print ret
