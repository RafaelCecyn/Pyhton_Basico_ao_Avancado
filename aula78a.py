# Sets são eficientes para remover valores duplicados
# de iteráveis.
# Seus valores serão sempre únicos;
# Não aceitam valores mutáveis;
# não tem indexes;
# não garantem ordem;
# são iteráveis (for in, in, not in)

s1 = {1,2,3,3,3,3,1}
print(s1) # {1,2,3}
l2 = [1,2,3,2,2,2,1]
s2 = set(l2)
l3 = list(s2)
print(l3) # [1, 2, 3]
# s3 = {[1,2]} # ERRO
print(3 in s1) # True
print(3 not in s1) # False

for i in s1:
    print(i) # 1 2 3