# Grupo
AMPHIBIA = 'AMPHIBIA'
ARACHNIDA = 'ARACHNIDA'
AVES = 'AVES'
MAMMALIA = 'MAMMALIA'
REPTILIA = 'REPTILIA'
CLASSE_ANIMAIS_CHOICES = [
    (AMPHIBIA, 'Amphibia'),
    (ARACHNIDA, 'Arachnida'),
    (AVES, 'Aves'),
    (MAMMALIA, 'Mammalia'),
    (REPTILIA, 'Reptilia'),
    ]

# Sexo
FEMEA = 'FÊMEA'
MACHO = 'MACHO'
INDEFINIDO = 'INDEFINIDO'
SEXO_CHOICES = [
    (FEMEA, 'Fêmea'),
    (MACHO, 'Macho'),
    (INDEFINIDO, 'Indefinido'),
]

# Faixa Etaria
FILHOTE = 'FILHOTE'
JOVEM = 'JOVEM'
ADULTO = 'ADULTO'
FAIXA_ETARIA_CHOICES = [
    (FILHOTE, 'Filhote'),
    (JOVEM, 'Jovem'),
    (ADULTO, 'Adulto'),
]

# Condição Física
BOA = 'BOA'
OTIMA = 'ÓTIMA'
REGULAR = 'REGULAR'
RUIM = 'RUIM'
PESSIMA = 'PÉSSIMA'
CONDICAO_FISICA_CHOICES = [
    (BOA, 'Boa'),
    (OTIMA, 'Ótima'),
    (REGULAR, 'Regular'),
    (RUIM, 'Ruim'),
    (PESSIMA, 'Péssima'),
]

# Ecdise
COMPLETA = 'COMPLETA'
INCOMPLETA = 'INCOMPLETA'
ECDISE_CHOICES = [
    (COMPLETA, 'Completa'),
    (INCOMPLETA, 'Incompleta'),
]

# Unidade de Media
KG = 'kg'
GRAMAS = 'g'
MG = 'mg'
LITROS = 'l'
ML = 'ml'
UNIDADE_DE_MEDIDA_CHOICES = [
    (KG, 'kg'),
    (GRAMAS, 'g'),
    (MG, 'mg'),
    (LITROS, 'l'),
    (ML, 'ml'),
]