# Exercício 01

# 1) Classifique as variáveis sexo, idade, tempo_experiencia, tamanho_empresa, trabalho_remoto, salario da base
# de dados em relação a qualitativa (nominal/ordinal) e quantitativa (discreta/contínua);

# sexo              -> qualitativa nominal
# idade             -> quantitativa discreta
# tempo_experiencia -> quantitativa discreta
# tamanho_empresa   -> qualitativa ordinal
# trabalho_remoto   -> qualitativa nominal
# salario           -> quantitativa contínua

# 2) Retire uma amostra de 400 observações utilizando a sintaxe abaixo:

# Amostra
base = read.csv2("salarios.csv")
set.seed(27072005)
base1 = base[sample(nrow(base), 400),]

# 3) Faça um gráfico para a variável tamanho_empresa e tire conclusões. No gráfico, o eixo y tem que estar em
# porcentagem e o gráfico deve conter um título geral e títulos nos eixos x e y.

# Tabela de frequência relativa (%)
freq <- prop.table(table(base1$tamanho_empresa)) * 100

# Gráfico de barras
barplot(
  freq,
  main = "Distribuição do tamanho das empresas",
  xlab = "Tamanho da empresa",
  ylab = "Percentual (%)",
  col = "lightblue"
)

# 4) Faça um gráfico para analisar a relação das duas variáveis qualitativas tamanho_empresa e trabalho_remoto,
# coloque os valores do eixo y do gráfico em porcentagem e tire conclusões.

tab <- prop.table(table(base1$tamanho_empresa, base1$trabalho_remoto), 1) * 100

barplot(
  t(tab),
  col = c("lightblue", "lightgreen"),
  main = "Trabalho remoto por tamanho da empresa",
  xlab = "Tamanho da empresa",
  ylab = "Percentual (%)",
  legend.text = c("Não", "Sim")
)

# 5) Faça um gráfico de densidade para a variável salario e tire conclusões.

plot(
  density(base1$salario),
  main = "Densidade do salário",
  xlab = "Salário",
  ylab = "Densidade",
  col = "black",
  lwd = 2
)

# 6) Faça um gráfico de densidade para a variável salario apresentando uma curva para cada trabalho_remoto no
# mesmo gráfico e tire conclusões.

# Curva para "Não"
lines(
  density(base1$salario[base1$trabalho_remoto == "Nao"]),
  col = "red",
  lwd = 2
)

# Curva para "Sim"
lines(
  density(base1$salario[base1$trabalho_remoto == "Sim"]),
  col = "blue",
  lwd = 2
)

# Legenda
legend(
  "topright",
  legend = c("Geral", "Não remoto", "Remoto"),
  col = c("black", "red", "blue"),
  lwd = 2
)