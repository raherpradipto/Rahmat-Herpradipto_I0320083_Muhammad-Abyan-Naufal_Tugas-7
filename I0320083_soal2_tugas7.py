# fungsi numerik
import math
a = -99.9
b = 224.5
c = -143.1
print("terdapat tiga bilangan: ", a, b, c)
# abs
aa = abs(a)
ab = abs(b)
ac = abs(c)
print("bilangan setelah berharga mutlak: ", aa, ab, ac)
# ceil
ca = math.ceil(aa)
cb = math.ceil(ab)
cc = math.ceil(ac)
print("bilangan setelah dibulatkan keatas: ", ca, cb, cc)
# sqrt
sa = math.sqrt(ca)
sb = math.sqrt(cb)
sc = math.sqrt(cc)
print("bilangan setelah diakarkuadratkan: ", sa, sb, sc)
# max min
print("nilai tertinggi dari ketiga bilangan: ", max(sa, sb, sc))
print("nilai terendah dari ketiga bilangan: ", min(sa, sb, sc))
