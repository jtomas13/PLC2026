
# PLC2026 - Processamento de Linguagens e Compiladores

## TPC2

**Problema:** Desenvolvimento de um pequeno conversor em Python de Markdown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:
* Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto";
* Bold: pedaços de texto entre "\*\*";
* Itálico: pedaços de texto entre "\*";
* Lista numerada;
* Link: [texto](endereço URL);
* Imagem: ![texto alternativo](path para a imagem).

O algoritmo processa o texto linha a linha utilizando expressões regulares (`re`) para identificar e converter elementos estruturais e de formatação inline.
* **Cabeçalhos e Listas:** A função principal (`conversorMarkdown`) analisa se a linha começa com `#` ou com uma estrutura de lista numerada (`1.`). Os itens de lista são acumulados temporariamente em `lista_itens` e encapsulados numa tag `<ol>` assim que a lista termina.
* **Formatação Inline:** A função auxiliar `conversorLinha` utiliza `re.sub` para tratar elementos internos como imagens, links, negrito e itálico.

---

**Exemplo**

Para este input:

```
# Título Principal

Este é um **exemplo** com *itálico* e links como [página da UC](http://www.uc.pt).

1. Primeiro item da lista numerada
2. Segundo item com [link](http://www.uc.pt)
3. Terceiro item com imagem: ![coelho](http://www.coellho.com)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
```

A função `conversorMarkdown` deu o seguinte resultado:

```
<h1>Título Principal</h1>

Este é um <b>exemplo</b> com <i>itálico</i> e links como <a href="http://www.uc.pt">página da UC</a>.

<ol>
<li>Primeiro item da lista numerada</li>
<li>Segundo item com <a href="http://www.uc.pt">link</a></li>
<li>Terceiro item com imagem: <img src="http://www.coellho.com" alt="coelho"/></li>
</ol>

Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
```
