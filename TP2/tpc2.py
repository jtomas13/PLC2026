import re

def conversorLinha(linha): #trata de linhas simples
    linha = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', linha)
    
    linha = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', linha)
    
    linha = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', linha)
    
    linha = re.sub(r'\*(.+?)\*', r'<i>\1</i>', linha)

    return linha

def conversorMarkdown(texto):
    resultado = []
    lista_itens = []
    dentro_de_lista = False

    for linha in texto.split("\n"):
        
        m = re.match(r'^(#+) (.*)', linha)
        if m: #ver se a linha começa com #
            n = len(m.group(1)) 
            titulo = m.group(2) 
            resultado.append(f'<h{n}>{titulo}</h{n}>')

        elif re.match(r'^(\d+)\.\s+(.*)', linha): #ver se a linha é do um item de lista
            m_lista = re.match(r'^(\d+)\.\s+(.*)', linha)
            conteudo_item = m_lista.group(2)
            conteudo_convertido = conversorLinha(conteudo_item) 
            lista_itens.append(f"<li>{conteudo_convertido}</li>")
            dentro_de_lista = True

        else: #fim da lista ou linha normal
            if dentro_de_lista:
                resultado.append('<ol>\n' + '\n'.join(lista_itens) + '\n</ol>')
                lista_itens = []
                dentro_de_lista = False
            
            if linha.strip() != '': # linha solta
                resultado.append(conversorLinha(linha))
            else:
                resultado.append('')

    if dentro_de_lista: #caso acabe em lista
        resultado.append('<ol>\n' + '\n'.join(lista_itens) + '\n</ol>')

    return "\n".join(resultado)

exemplo_md = """# Título Principal

Este é um **exemplo** com *itálico* e links como [página da UC](http://www.uc.pt).

1. Primeiro item da lista numerada
2. Segundo item com [link](http://www.uc.pt)
3. Terceiro item com imagem: ![coelho](http://www.coellho.com)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ..."""

html_resultante = conversorMarkdown(exemplo_md)
print(html_resultante)