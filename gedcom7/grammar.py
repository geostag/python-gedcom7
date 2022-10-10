agebound = '[<>]'
d = '\\ '
integer = '[0-9]+'
years = f'{integer}y'
months = f'{integer}m'
weeks = f'{integer}w'
days = f'{integer}d'
ageduration = (
    f'({years}({d}{months})?({d}{weeks})?({d}{days})?|{months}({d}{weeks})?({d}'
    f'{days})?|{weeks}({d}{days})?|{days})'
)
age = f'({agebound}{d})?{ageduration}'
anychar = '[\t-\\U0010ffff]'
atsign = '@'
banned = (
    '[\\x00-\\x08\x0b-\x0c\\x0e-\\x1f\\x7f\\x80-\\x9f\\ud800-\\udfff'
    '\\ufffe-\\uffff]'
)
underscore = '_'
ucletter = '[A-Z]'
tagchar = f'({ucletter}|[0-9]|{underscore})'
exttag = f'{underscore}({tagchar})+'
calendar = f'(GREGORIAN|JULIAN|FRENCH_R|HEBREW|{exttag})'
day = f'{integer}'
stdtag = f'{ucletter}({tagchar})*'
month = f'({stdtag}|{exttag})'
year = f'{integer}'
epoch = f'(BCE|{exttag})'
date = f'({calendar}{d})?(({day}{d})?{month}{d})?{year}({d}{epoch})?'
dateapprox = f'(ABT|CAL|EST){d}{date}'
dateexact = f'{day}{d}{month}{d}{year}'
dateperiod = f'((TO{d}{date})?|FROM{d}{date}({d}TO{d}{date})?)'
daterange = f'(BET{d}{date}{d}AND{d}{date}|AFT{d}{date}|BEF{d}{date})'
daterestrict = '(FROM|TO|BET|AND|BEF|AFT|ABT|CAL|EST|BCE)'
datevalue = f'({date}|{dateperiod}|{daterange}|{dateapprox})?'
tag = f'({stdtag}|{exttag})'
enum = f'{tag}'
eol = '(\\\r(\\\n)?|\\\n)'
fraction = '[0-9]+'
hour = '([0-9]|[01][0-9]|2[0123])'
nonzero = '[1-9]'
level = f'(?P<level>0|{nonzero}[0-9]*)'
xref = f'{atsign}({tagchar})+{atsign}'
voidptr = '@VOID@'
pointer = f'(?P<pointer>{voidptr}|{xref})'
nonat = '[\t -?A-\\U0010ffff]'
noneol = '[\t -\\U0010ffff]'
linestr = f'(?P<linestr>({nonat}|{atsign}{atsign})({noneol})*)'
lineval = f'({pointer}|{linestr})'
line = f'{level}{d}((?P<xref>{xref}){d})?(?P<tag>{tag})({d}{lineval})?{eol}'
nocommasp = '[\t-\\x1d!-+\\--\\U0010ffff]'
nocomma = '[\t-+\\--\\U0010ffff]'
listitem = f'({nocommasp}|{nocommasp}({nocomma})*{nocommasp})?'
listdelim = f'({d})*,({d})*'
list = f'{listitem}({listdelim}{listitem})*'
list_enum = f'{enum}({listdelim}{enum})*'
list_text = f'{list}'
mt_char = "[ -!#-'*-+\\--.0-9A-Z^-~]"
mt_token = f'({mt_char})+'
mt_type = f'{mt_token}'
mt_subtype = f'{mt_token}'
mt_attribute = f'{mt_token}'
mt_qtext = '[\t-\n -!#-\\[\\]-~]'
mt_qpair = '\\\\[\t-~]'
mt_qstring = f'"({mt_qtext}|{mt_qpair})*"'
mt_value = f'({mt_token}|{mt_qstring})'
mt_parameter = f'{mt_attribute}={mt_value}'
mediatype = f'{mt_type}/{mt_subtype}(;{mt_parameter})*'
minute = '[012345][0-9]'
namechar = '[ -.0-\\U0010ffff]'
namestr = f'({namechar})+'
personalname = f'({namestr}|({namestr})?/(?P<surname>{namestr})?/({namestr})?)'
second = '[012345][0-9]'
text = f'({anychar})*'
special = f'{text}'
time = f'{hour}:{minute}(:{second}(\\.{fraction})?)?(Z)?'
