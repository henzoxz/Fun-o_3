# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.

raio = float(input("Digite o Raio do Círculo: "))
numeropi = 3.14

def calcular_area_base(raio):
    calculo = (raio * raio) * numeropi
    area = calculo

    return(area)

areadc = calcular_area_base(raio)
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

altura = float(input("Digite a Altura do Cilindro: "))


def calcular_volume_cilindro(areadc):
    calculo = numeropi * (raio * raio) * altura
    return(calculo)

volumecilindro = calcular_volume_cilindro(areadc)
print(f"A Área do Círculo é: {areadc}")
print(f"O Volume do Cilindro é: {volumecilindro}")


