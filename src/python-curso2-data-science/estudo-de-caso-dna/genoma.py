entrada = open("dna-humano.fasta").read()
saida   = open("dna-humano.html","w")

cont = {}

for i in ['A','T','C','G']:
        for j in ['A','T','C','G']:
                cont[i+j] = 0

entrada = entrada.replace("N","")

for k in range(len(entrada)-1):
        cont[entrada[k]+entrada[k+1]] += 1

i = 1
for k in cont:
        transparencia = cont[k] / max(cont.values())
        saida.write("<div style='width: 100px; height: 100px; float: left; background-color: rgba(0, 0, 0, "+str(transparencia)+"); color: #fff; border: 1px solid #111;'>"+k+"</div>")
        
        if i%4 == 0:
                saida.write("<div style='clear: both;'></div>")
        
        i += 1

saida.close()