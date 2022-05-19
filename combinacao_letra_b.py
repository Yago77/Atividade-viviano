from itertools import combinations

banco = ['SQL','NoSQL','GIS']
programacao = ['Python','Java','C','PHP']
eng = ['Metodos','Processos']
temp = combinations(banco+programacao+eng,1)
for i in list(temp):
    print (i)
    
