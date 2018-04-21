

'''
Exponencial

Tipo de distribuicao continua de probabilidade 
representada por um parametro.

- lambda e X 
'''

'''
T-Student

- Mesma form em sino da distruibuição Normal, mas reflete a 
maior variabilidade que é de se experar em amostras pequenas,

- Quanto maior grau de liberdade mais se aproxima de uma normal

'''

'''
Teorema do limite Central

- Se tivermos informacoes detabladas sobre alguma populacao entao
 podemos fazer inferenceias podrosas sobre qualquer amostra 
 adequatamente extraida dessa populacao

- Se tivermos informacoes detralbades sobre uma amostra extraida de mode
  adequado podemosfazer inferencias surpreendetnemte acurados sobre a populacao
  da qual a mostra foi retirada

- De acordo com TLC, as medias das amostras 
pra qualquer populacao estarao distribuição 
estarao dstribuidas aproximadamente como uma 
distribuicao normal em tormno da media da populacao.

- tamanho da amostra n >= 30.

- Erro padrao: média das amostras.

- Erro padrao = std()/ Math.sqrt(n).
'''

import math;


def calculateDesvioPopulacao(std, qtdElements):
	return std/math.sqrt(qtdElements);





