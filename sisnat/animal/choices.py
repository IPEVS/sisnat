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
UNI = 'unidade'
POR = 'porcao'
PED = 'pedaco'
UNIDADE_DE_MEDIDA_CHOICES = [
    (KG, 'kg'),
    (GRAMAS, 'g'),
    (MG, 'mg'),
    (LITROS, 'L'),
    (ML, 'ml'),
    (UNI, 'unidade'),
    (POR, 'porção'),
    (PED, 'pedaço'),
]

#Area
AREA_U = 'Área urbana'
AREA_R = 'Área rural'
AREA_RESGATE_CHOICES = [
    (AREA_U, 'Área urbana'),
    (AREA_R, 'Área rural')
]

#Status
P_IPEVS = "Plantel IPEVS"
P_IPEVS_R_O = "Plantel IPEVS – recuperacao/observacao"
P_IPEVS_ENC = "Plantel IPEVS – encaminhar para outro centro"
SOL = "Soltura"
OBI = "Obito"
STATUS_CHOICES = [
    (P_IPEVS, "Plantel IPEVS"),
    (P_IPEVS_R_O, "Plantel IPEVS – recuperação/observação "),
    (P_IPEVS_ENC, "Plantel IPEVS – encaminhar para outro centro"),
    (SOL, 'Soltura'),
    (OBI, 'Óbito'),
]