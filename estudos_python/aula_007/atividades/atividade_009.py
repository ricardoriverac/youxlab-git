#Escreva um programa que converta uma temperatura digitada em °C a comverter para °F

#Resposta 

temperatura_em_c = float(input('Digite o a temperatura em °C : ')) 
converter_para_F = ((temperatura_em_c * 9/5) + 32)
print(f'A temperatura em °F : {converter_para_F}')
