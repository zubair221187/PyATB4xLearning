class Son:
    gold="1Kg"

class Father(Son):
    diamond="22 karat"

class Grandfather(Father):
    btc="1btc"

gf=Grandfather()
print(gf.diamond)

