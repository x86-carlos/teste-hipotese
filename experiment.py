from statistics import mean
from statistics import median
from statistics import mode
from scipy.stats import ttest_ind

tempo_com_copilot = [100, 59, 98, 103, 130, 70, 109, 88, 76, 123]
tempo_sem_copilot = [205, 188, 130, 98, 100, 174, 207, 198, 172, 209]

tempo_com_copilot_ordenado = sorted(tempo_com_copilot)
tempo_sem_copilot_ordenado = sorted(tempo_sem_copilot)

media_com_copilot = mean(tempo_com_copilot_ordenado)
media_sem_copilot = mean(tempo_sem_copilot_ordenado)

mediana_com_copilot = median(tempo_com_copilot_ordenado)
mediana_sem_copilot = median(tempo_sem_copilot_ordenado)

moda_com_copilot = mode(tempo_com_copilot_ordenado)
moda_sem_copilot = mode(tempo_sem_copilot_ordenado)

print("Medidas de tendência central para tempo com o copilot")
print(f"Média: {media_com_copilot}")
print(f"Mediana: {mediana_com_copilot}")
print(f"Moda: {moda_com_copilot}")

print()

print("Medidas de tendência central para tempo sem o copilot")
print(f"Média: {media_sem_copilot}")
print(f"Mediana: {mediana_sem_copilot}")
print(f"Moda: {moda_sem_copilot}")

# Teste de hipótese t-test
stat, p = ttest_ind(tempo_com_copilot_ordenado, tempo_sem_copilot_ordenado)

print()
print("Teste de hipótese")
print(f"p-value = {p}")

if p > 0.05:
	print('Provavelmente distribuições iguais')
else:
	print('Provavelmente distribuições diferentes')
