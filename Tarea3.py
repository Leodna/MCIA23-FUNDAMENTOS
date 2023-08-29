# %%
def suma_lista(lista):
    if lista == []:
        return 0
    else:
        return lista[-1]+suma_lista(lista[:-1])

# %%
l = [10,9,8,7]
print (suma_lista(l))

# %%
def invertir_lista(lista):
    if lista == []:
        return []
    else:                
        return [lista[-1]] + invertir_lista(lista[:-1])

# %%
il = invertir_lista(l)
print (l)
print (il)

# %%
def dec_bin(n):
    if n == 1:
        return "1"
    else:        
        return dec_bin(n//2)+"{}".format(n%2)


# %%
print (dec_bin(10))

# %%
def bin_dec (n):
    if len(n)-1 == 0:        
        return int(n) * 2**0
    else:    
        p = len(n)-1
        return int(n[0]) * (2**p) + bin_dec(n[1:])


# %%
n = "10101"
bin_dec(n)


