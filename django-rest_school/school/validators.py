import re	
from django.utils import timezone

def cpf_invalid(cpf):
    return len(cpf) != 11 or not cpf.isdigit()

def name_invalid(name):
	return not name.replace(" ", "").isalpha()

def cellphone_invalid(cellphone):
    model = f"[0-9]{2} [0-9]{5}-[0-9]{4}"
	response = re.findall(model, cellphone)
 
	return not response
 
def data_birth_invalid(data_birth):
	return data_birth >= timezone.now().date()
