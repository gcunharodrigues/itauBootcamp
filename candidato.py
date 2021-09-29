# Dados de apresentação do candidato Guilherme Cunha Rodrigues
import os, statistics

candidato = {
    'nome' : 'Guilherme Cunha Rodrigues',
    'idade' : 34,
    'email' : 'rodrigues.guilhermecunha@gmail.com',
    'residencia' : 'Rua Cônego Amaral Mello',
    'numero' : 28,
    'CEP' : '02513-030',
    'complementoResidencia' : 'apto 14 C',
    'cidade' : 'São Paulo',
    'estado' : 'SP',
    'formacaoAcademica' : 'Engenharia Civil',
    'instituicao' : 'Escola Politécnica da USP',
    # Experiência profissional nas áreas de projetos de 
    # engenharia e mercado financeiro, neste atuação com atendimento e 
    # comercial.
    'experienciaProfissional' : [
        'Projesoft', 'Engeform', 'Groupe Allard', 'TCRE/PROMAPEN',
        'W1 Finance', 'Modalmais', 'Carbon Investing',
    ],
    # Mais informações sobre experiência profissional, certificados e 
    # competências podem ser visualizadas em: 
    # https://www.linkedin.com/in/guilhermecunharodrigues/
    'casoSucesso' : 'Redes de Esgoto em Itapevi - SP',
    'oportunidadePretendida' : 'Expert em Dados pelo Itaú', 
    'objetivosProfissionais' : 'Resolução de problemas desafiadores ' \
                               'utilizando Ciência de Dados'
}

for informacao, dado in candidato.items():
    print(f"  {informacao}: {dado}")
    