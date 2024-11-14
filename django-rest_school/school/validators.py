import re	
from django.utils import timezone
from validate_docbr import CPF

def cpf_invalid(number_cpf):
    cpf = CPF()
    cpf_valid = cpf.validate(number_cpf)
    return not cpf_valid

def name_invalid(name):
	return not name.replace(" ", "").isalpha()

def cellphone_invalid(cellphone):
    model = r"[0-9]{2} [0-9]{5}-[0-9]{4}"
    response = re.findall(model, cellphone)
    
    return not response
 
def data_birth_invalid(data_birth):
	return data_birth >= timezone.now().date()
