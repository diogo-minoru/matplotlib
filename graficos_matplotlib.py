import matplotlib.pyplot as plt

plt.style.available

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#for estilo in plt.style.available:

# Gráfico de linha
plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 4)

# Definindo título dos eixos
ax.set_title("Square Numbers", fontsize = 16)
ax.set_xlabel("Value", fontsize = 12)
ax.set_ylabel("Square of Value", fontsize = 12)

# Definindo o tamanho do rótulo do eixo de marcação
ax.tick_params(labelsize = 8)

plt.show()

# Gráfico de dispersão
plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
ax.scatter(input_values, squares, s = 500)

# Definindo título dos eixos
ax.set_title("Square Numbers", fontsize = 16)
ax.set_xlabel("Value", fontsize = 12)
ax.set_ylabel("Square of Value", fontsize = 12)

# Definindo o tamanho do rótulo do eixo de marcação
ax.tick_params(labelsize = 8)

plt.show()


# Criando valores de 1 a 1000 e para cada valor, o seu valor ao quadrado
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s = 1, color = "red")

# Configurando os intervalos do eixo
ax.axis([0, 1100, 0, 1100000])

# Configurar para utilizar a notação simples para representar os valores nos eixos
ax.ticklabel_format(style = "plain")

plt.show()