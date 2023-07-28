from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your models here.

class LinksData(models.Model):
    """Return all links data"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="123456789", verbose_name="criado pelo usuário:")
    link_id = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    access_mode = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    refresh_rate = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    last_accessed_at = models.CharField(max_length=100)
    external_id = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    institution_user_id = models.CharField(max_length=255)
    credentials_storage = models.CharField(max_length=100)
    fetch_historical = models.BooleanField()



# personalizando o model de usuário para incluir o campo whatsapp
def validate_cpf_cnpj(value):
    if not value.isdigit():
        raise ValidationError('O campo CPF/CNPJ deve conter apenas números')


def validate_uf(value): 
    if value.isdigit():
        raise ValidationError('O campo UF deve conter apenas letras')

def validate_num(value):
    if not value.isdigit():
        raise ValidationError('O campo Número deve conter apenas números')

def validate_city(value):
    if value.isdigit():
        raise ValidationError('O campo Cidade deve conter apenas letras')

def validate_cep(value):
    if not value.isdigit():
        raise ValidationError('O campo CEP deve conter apenas números')
    

BankChoices = (
    ('341', 'Itaú Unibanco'),
    ('033', 'Banco Santander'),
    ('237', 'Banco Bradesco'),
    ('104', 'Caixa Econômica'),
    ('001', 'Banco do Brasil'),
    ('118', 'Sicredi'),
    ('311', 'Sicoob')
)

   
# modelo de dados para cadastro de novos clientes do escritório

class OfficeClientModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="123456789", verbose_name="criado pelo usuário:")  
    cpfCnpj = models.CharField(max_length=14, verbose_name='CPF/CNPJ', validators=[validate_cpf_cnpj])
    name = models.CharField(max_length=100, verbose_name='Razão Social') 
    street = models.CharField(max_length=250, verbose_name='Endereço')   
    addressNumber = models.CharField(max_length=10, verbose_name='Número', validators=[validate_num])
    addressComplement = models.CharField(max_length=100, verbose_name='Complemento', blank=True)
    neighborhood = models.CharField(max_length=255, verbose_name='Bairro')
    city = models.CharField(max_length=255, verbose_name='Cidade', validators=[validate_city])
    state = models.CharField(max_length=2, verbose_name='UF', validators=[validate_uf])
    zipcode = models.CharField(max_length=9, verbose_name='CEP', validators=[validate_cep])
    token = models.CharField(max_length=100, verbose_name='token')
    whatsapp = models.CharField(max_length=20, verbose_name='Whatsapp', default="123456789")

    class Meta:
        verbose_name_plural = 'Cliente dos escritórios'
        unique_together = [['cpfCnpj', 'name', 'street', 'addressNumber', 'addressComplement', 'neighborhood', 'city', 'state', 'zipcode']]
        

    def __str__(self):
        return self.name
    

class BankAccountModels(models.Model):
    bankCode_choices = (
        ("341", "Itaú Unibanco"),
        ("033", "Banco Santander"),
        ("237", "Banco Bradesco"),
        ("104", "Caixa Econômica"),
        ("001", "Banco do Brasil"),
        ("118", "Sicredi"),
        ("311", "Sicoob")
    )

    accountType_choices = (
        ("Corrente", "Conta Corrente"),
        ("Poupança", "Conta Poupança"),
        ("Investimento", "Conta Investimento"),
        ("Salário", "Conta Salário"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="123456789", verbose_name="criado pelo usuário:")
    customer = models.ForeignKey(OfficeClientModel, on_delete=models.CASCADE, verbose_name='Cliente')
    cpfCnpj = models.CharField(max_length=18, verbose_name='CPF/CNPJ', validators=[validate_cpf_cnpj])
    bankCode = models.CharField(max_length=3, choices=bankCode_choices, verbose_name='Código do banco')
    agency = models.CharField(max_length=10, verbose_name='Agência')
    agencyDigits = models.CharField(max_length=2, verbose_name='Dígito da agência')
    accountType = models.CharField(max_length=15, choices=accountType_choices, verbose_name='Tipo de conta')
    accountNumber = models.CharField(max_length=12, verbose_name='Número da conta')
    accountNumberDigit = models.CharField(max_length=2, verbose_name='Dígito da conta')
    accountHash = models.CharField(max_length=100, verbose_name='Hash da conta')

    class Meta:
        verbose_name_plural = 'Contas bancárias'
        unique_together = [['bankCode', 'agency', 'agencyDigits', 'accountNumber', 'accountNumberDigit']]

    def __str__(self):
        return self.customer.name



# modelos de dados para receber extrato bancário
class BankStatementModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="123456789", verbose_name="criado pelo usuário:")
    bankStatement = models.ForeignKey(OfficeClientModel, on_delete=models.CASCADE, verbose_name='Cliente')    
    bankCode = models.CharField(max_length=3, verbose_name='Código do banco')
    bank = models.CharField(max_length=100, verbose_name='Banco')
    currency = models.CharField(max_length=3, verbose_name='Moeda')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Saldo')
    date = models.DateField(verbose_name='Data')
    typee = models.CharField(max_length=100, verbose_name='Tipo')
    totalTransactions = models.IntegerField(verbose_name='Total de transações')
    accountHash = models.CharField(max_length=100, verbose_name='Hash da conta')
    dateStart = models.CharField(max_length=100, verbose_name='Data inicial')
    dateEnd = models.CharField(max_length=100, verbose_name='Data final')
    # transactions credits
    sequence_credit = models.IntegerField(verbose_name='Sequência', default=0)
    code_credit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Código', default=0)
    description_credit = models.CharField(max_length=100, verbose_name='Descrição', default="")
    amount_credit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor', default=0)
    date_credit = models.CharField(max_length=100, verbose_name='Data', default="")
    fitid_credit = models.CharField(max_length=100, verbose_name='Fitid', default=0)
    # transactions debits
    sequence_debit = models.IntegerField(verbose_name='Sequência', default=0)
    code_debit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Código', default=0)
    description_debit = models.CharField(max_length=100, verbose_name='Descrição', default=" ")
    amount_debit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor', default=0)
    date_debit = models.CharField(max_length=100, verbose_name='Data', default="")
    fitid_debit = models.CharField(max_length=100, verbose_name='Fitid', default=0)
    # balance initial (saldo initial)
    date_balance_initial = models.CharField(max_length=100, verbose_name='Data', default="")
    balance_initial = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Saldo inicial', default=0)
    # balance final (saldo final)
    date_balance_final = models.CharField(max_length=100, verbose_name='Data', default="")
    balance_final = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Saldo final', default=0)
    
    
