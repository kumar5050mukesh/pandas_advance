import pandas as pd
def test(x):
    arr=[]
    for i in x:
        if i != "@":
            arr.append(i)
        else:
            break
    return arr

df3_new = pd.DataFrame({"Email":["jhon.doe@gmail.com", "muk.kr@gmail.com", "suk.smt@gmail.com"]})

a = (map(test, df3_new["Email"]))

for i in a:
    print(str(i))