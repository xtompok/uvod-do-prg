
def bin_search(l,start,end,num):
    print("Hledám {} v {}".format(num, l[start:end]))
    if (start==end): # Toto musí být první test, aby funkce nespadla na prázdném seznamu
        return False
    if l[start] == num:
        return True
    if (start == end-1):
        return False
    half = (start+end)//2
    if l[half] <= num:
	    start=half
    else:
	    end=half
    res = bin_search(l,start,end,num)
    return res

seznam = (1,2,3,6,8,13)
print(bin_search(seznam,0,len(seznam),5)) # vrátí False
print(bin_search(seznam,0,len(seznam),8)) # vrátí True
#print(bin_search([],0,len([]),2))
print(bin_search(seznam,0,len(seznam),0))

