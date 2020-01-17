from flask import Flask, jsonify, request

app_service = Flask('app_service')

# Quando nenhuma requisição é informada, o método GET é executado - default
@app_service.route('/')
def index():
	number = request.args.get('number')
	result = checkNumber(number)
	if result is None:
		result = translate(number)

	return jsonify(extenso=result)

def checkNumber(number):
	if number is None or number == "":
		return "Nenhum valor informado para o argumento 'number'."
		
	if not number.isdigit():
		if number.find("-") == 0:
			number = number[1:]
		
		if not number.isdigit():
			return "Argumento inválido. Digite um número inteiro."
			
	if int(number) > 99999 or int(number) < -99999:
		return "O número informado está fora da faixa de valores permitida [-99999, 99999]."
	
	return None
	
def translate(number):
	decimal_place = 0
	num_full = ""
	num_negative = False
	generate_tens = False
	
	# Verfica se valor é negativo
	if  number.find("-") == 0:
		num_negative = True
		number = number[1:]
	
	number = int(number)
		
	unit={1:'um', 2:'dois', 3:'três', 4:'quatro', 5:'cinco', 
		  6:'seis', 7:'sete', 8:'oito', 9:'nove'}
	
	tens={10: 'dez', 11:'onze', 12:'doze', 13:'treze', 14:'quatorze', 
		  15:'quinze', 16:'dezesseis', 17:'dezessete', 18:'dezoito', 
		  19:'dezenove', 20:'vinte', 30:'trinta', 40:'quarenta', 
		  50:'cinquenta', 60:'sessenta', 70:'setenta', 80:'oitenta', 90: 'noventa'}
	
	
	hundreds={100:'cem', 200:'duzentos', 300:'trezentos', 
			  400:'quatrocentos', 500:'quinhentos', 600:'seiscentos', 
			  700:'setecentos', 800:'oitocentos', 900:'novecentos'}
		
	if number > 10:
		value = number % 100
		if value > 10 and value < 20:
			num_full = tens[value]
			number = int((number - value)/100)
			decimal_place = 2
		
	while (number > 0):
		value = number % 10
		
		if value > 0 or decimal_place >= 3:	
			if decimal_place == 0:
				num_full = unit[value]
			
			elif decimal_place == 1:
				num_full = num_full and tens[value*10] + " e " + \
				num_full or tens[value*10]
			
			elif decimal_place == 2:
				if value == 1 and num_full:
					num_full = "cento e " + num_full
				else:
					num_full = num_full and hundreds[value*100] + " e " + \
					num_full or hundreds[value*100]
				
			else:
				if value == 0:
					num_full = num_full and tens[number] + " mil e " + \
					num_full or tens[number] + " mil" 
					value = number	
				
				elif number > 10 and number < 20:
					num_full = num_full and tens[number] + " mil e " + \
					num_full or tens[number] + " mil" 
					value = number
				
				else:
					if number > 10:
						num_full = num_full and unit[value] + " mil e " + \
						num_full or unit[value] + " mil"
						generate_tens = True
					
					else:
						if generate_tens == True:
							num_full = tens[value*10] + " e " + num_full
						else:
							num_full = num_full and unit[value] + " mil e " + \
							num_full or unit[value] + " mil"

		number = int((number - value)/10)
		decimal_place = decimal_place + 1
	
	if num_negative == True:
		num_full = "menos " + num_full
	
	return num_full

app_service.run(port=8000)
