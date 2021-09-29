import os
import statistics

def solucaoCase(case):
    googleSearch = [
        'app Itaú', 'Quantidade de acessos a aplicativos bancários'
    ]
    appItau = [
		'Banco Itaú', 'Itaú Light: Conta Bancária', 
		'Itaucard: Cartão de crédito', 'Banco Itaú Personnalité',
		'Itaú Empresas: Conta PJ e MEI',
	]
    
    caminho = 'C:/Users/guicr/Desktop/itauBootcamp/pesquisa/'
    arquivos = os.listdir(caminho)
    #for arquivo in arquivos:
        #with open(caminho + arquivo) as arquivoObjeto:
           # conteudo = arquivoObjeto.read()
            
    numeroCorrentistas = 15_100_000 + 1_300_000
    
    appItau.append('iti: banco digital do Itaú')
    
    sessoesAdjust = [1.62, 1.68]
    mediaSessoesAdjust = statistics.mean(sessoesAdjust)

    acessosGratuitosApptopia = [0.36, 0.43]
    mediaApptopia = statistics.mean(acessosGratuitosApptopia)
    
    quantidadeAcessosDiarios = (
        numeroCorrentistas
        * mediaApptopia
        * mediaSessoesAdjust
    )
    quantidadeAcessosMensal = quantidadeAcessosDiarios * 30
    return quantidadeAcessosMensal

if __name__ == '__main__':
    case = "Quantos acessos o app do Itaú tem por mês?"
    solucao = solucaoCase(case)
    print(solucao)