"""
Правильно
"""


v = '9'*207
while '9999' in v or '333' in v:
    if '9999' in v:
        v = v.replace('9999','3',1)
    else:
        v = v.replace('333','99',1)
print(v)