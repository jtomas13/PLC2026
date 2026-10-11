

# PLC2026 - Processamento de Linguagens e Compiladores

## TPC3

**Problema:** Desenvolvimento de um analisador léxico em Python para uma linguagem de query, utilizando expressões regulares para identificar e categorizar os elementos (tokens) que compõem o código-fonte.
* Comentários: Linhas iniciadas por #, que devem ser ignoradas no processamento final;
* Strings: Sequências de caracteres delimitadas por aspas duplas "texto";
* Variáveis: Identificadores que começam por ? seguidos de caracteres alfanuméricos;
* Língua (Tags de idioma): Identificadores que começam por @ seguidos de dois caracteres alfabéticos (ex: @en);
* Palavras Reservadas: Palavras-chave da linguagem, neste caso a palavra reservada LIMIT e a instrução select;
* Números: Valores numéricos inteiros;
* Delimitadores: Caracteres de pontuação estrutural {, } e .;
* Conceitos: Identificadores alfanuméricos que representam elementos como atributos ou entidades (ex: where, a, dbo:MusicalArtist, foaf:name);
* Espaços: Espaços em branco, tabulações e quebras de linha (\n), que devem ser ignorados.

O algoritmo processa o texto utilizando uma expressão regular combinada (re.finditer) para extrair os tokens sequencialmente.
* **Definição e Ordem dos Tokens:** O script define uma lista de expressões regulares nomeadas (tokens). A ordem de avaliação é crítica: regras específicas como palavras reservadas (LIMIT, select), e cadeias delimitadas (STRING, VARIAVEL, LINGUA) devem surgir antes da regra geral de captura de CONCEITO (identificadores alfanuméricos) para evitar classificações incorretas.

---

**Exemplo**

Para este input:

```
"""
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
  ?s a dbo:MusicalArtist.
  ?s foaf:name "Chuck Berry"@en .
  ?w dbo:artist ?s.
  ?w foaf:name ?nome.
  ?w dbo:abstract ?desc
} LIMIT 1000
"""
```

O analisador léxico produziu o seguinte resultado:

```
SELECT          select
VARIAVEL        ?nome
VARIAVEL        ?desc
CONCEITO        where
DELIMITADOR     {
VARIAVEL        ?s
CONCEITO        a
CONCEITO        dbo:MusicalArtist
DELIMITADOR     .
VARIAVEL        ?s
CONCEITO        foaf:name
STRING          "Chuck Berry"
LINGUA          @en
DELIMITADOR     .
VARIAVEL        ?w
CONCEITO        dbo:artist
VARIAVEL        ?s
DELIMITADOR     .
VARIAVEL        ?w
CONCEITO        foaf:name
VARIAVEL        ?nome
DELIMITADOR     .
VARIAVEL        ?w
CONCEITO        dbo:abstract
VARIAVEL        ?desc
DELIMITADOR     }
LIMIT           LIMIT
NUMERO          1000
```
