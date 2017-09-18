
#coding=utf-8

import re

pattern = re.compile("[abc$]")

print pattern.findall("abcdef")
print pattern.findall("ab$")

result = pattern.match("aefg")

pattern1 = re.compile("a[bcd]*d")

#match search findall  finditer的区别
print pattern1.match("abcdacd").group()
print pattern1.search("efabcdabcd").group()
print  pattern1.findall("abcb")

#
print pattern1.match("abcdacd").end()
print pattern1.match("abcdacd").span()

# model - level function
print re.match(r"[abc]", "abc").group()

