from itertools import combinations

banco = ['SQL','NoSQL','GIS']
programacao = ['Python','Java','C','PHP']
eng = ['Metodos','Processos']
combinacoes = combinations(banco+programacao+eng,1)
for i in list(combinacoes):
    print (i)
    
