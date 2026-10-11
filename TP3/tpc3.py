import re

codigo = """
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
  ?s a dbo:MusicalArtist.
  ?s foaf:name "Chuck Berry"@en .
  ?w dbo:artist ?s.
  ?w foaf:name ?nome.
  ?w dbo:abstract ?desc
} LIMIT 1000
"""

tokens = [
    ('SELECT', r'#.*'),
    ('STRING', r'"[^"]*"'),
    ('VARIAVEL', r'\?[a-zA-Z0-9]+'),
    ('LINGUA', r'@[a-zA-Z]{2}'),
    ('LIMIT', r'\bLIMIT\b'),
    ('NUMERO', r'\d+'),
    ('DELIMITADOR', r'[{}.]'),
    ('CONCEITO', r'[a-zA-Z_][a-zA-Z0-9_:]*'),
    ('ESPACO', r'[ \t\n]+'),
    ('DESCONHECIDO', r'.'),
]

# Compilar a expressão regular combinada
apanhar_tokens = '|'.join('(?P<%s>%s)' % pair for pair in tokens)
mo = re.compile(apanhar_tokens).finditer

# Analisar o código
for m in mo(codigo):
    tipo = m.lastgroup
    valor = m.group(tipo)
    
    # Ignorar comentários e espaços em branco
    if tipo in ['COMENTARIO', 'ESPACO']:
        continue
    elif tipo == 'DESCONHECIDO':
        raise RuntimeError(f'Carácter inesperado: {valor!r}')
    
    print(f'{tipo:<15} {valor}')