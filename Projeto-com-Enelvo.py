# Projeto simples com Enelvo
from enelvo.normaliser import Normaliser

norm = Normaliser(tokenizer='readable')

normalizador = Normaliser(tokenizer='readable', capitalize_inis=True, 
                          capitalize_pns=True, capitalize_acs=True, 
                          sanitize=True)

texto = 'eu gosto d aprinder sobre proceçamento d linguage naturl.'
resultado = normalizador.normalise(texto)
print(resultado)