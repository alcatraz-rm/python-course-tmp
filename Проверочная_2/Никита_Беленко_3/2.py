"""
Правильно

1. В if можно проверять наличие подстроки в строке так же, как вы это делаете в while: if "4444" in s.
"""


s = "4"*186

while "4444" in s or "777" in s:
    if(s.find("4444") != -1):
        s = s.replace("4444", "77", 1)
    else:
        s = s.replace("777", "4", 1)
print(s)

# 7744