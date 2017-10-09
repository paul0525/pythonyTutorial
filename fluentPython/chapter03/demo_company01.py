
import sys, locale

expressions = """
              locale.getpreferredencoding()
              type(my_file)
"""
locale.getpreferredencoding()
my_file.encoding
sys.stdout.isatty()
sys.stdout.encoding

my_file=open('demo_company.py','w')

for expression in expressions.split():
    value = eval(expression)
    print repr(value)