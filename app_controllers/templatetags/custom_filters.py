# arquivo para formatar o cpf e cnpj no template de cadastro de novas contas bancárias

from django import template

register = template.Library()

@register.filter
def format_cpf_cnpj(value):
    # Verifica se é CPF (11 dígitos) ou CNPJ (14 dígitos)
    if len(value) == 11:
        return f"{value[:2]}.{value[2:5]}.{value[5:8]}/{value[8:12]}-{value[12:]}"
    elif len(value) == 14:
        return f"{value[:2]}.{value[2:5]}.{value[5:8]}/{value[8:12]}-{value[12:14]}"
    
    # Retorna o valor original se não for CPF nem CNPJ válido
    return value