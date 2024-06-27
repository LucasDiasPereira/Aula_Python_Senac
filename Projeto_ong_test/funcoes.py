def criacao_ong(nome,tipo,CNPJ):
    ong = {
    'nome':nome,
    'tipo':tipo,
    'CNPJ':CNPJ,
    'projetos':[] 
    }
    return ong


def criacao_projeto(nome,descricao):
    projeto = {
    'nome':nome,
    'descricao':descricao
}
    return projeto

def localizar_ong(nome,catalogo):
    for ong in catalogo:
        if ong['nome'] == nome:
            return ong
    return None

def lista_projeto(nome,ong):
    for projeto in ong['projetos']:
        if projeto['nome'] == nome:
            return projeto
