# Exercício 03

library(dplyr)
library(ggplot2)

# 1) Retire uma amostra de 90 observações utilizando a sintaxe abaixo:

# Amostra
base = read.csv2("dados_alunos.csv")
set.seed(27072005)
base1 = base[sample(nrow(base), 90),]

# com a amostra retirada, faça a análise dos itens abaixo.

# 2) Renomeie as categorias das variáveis Sexo e Escola, onde:
# Sexo (1 = Masculino; 2 = Feminino)
# Escola (1 = Publica; 2 = Particular)

base1$Sexo <- ifelse(base1$Sexo == 1, "Masculino", "Feminino")
base1$Escola <- ifelse(base1$Escola == 1, "Publica", "Particular")

# 3) Crie a variável IMC, onde a fórmula do IMC é dada por: IMC = Peso/Altura²

base1$IMC <- base1$Peso / (base1$Altura^2)

# 4) Calcule a média, desvio padrão e coeficiente de variação para as seguintes variáveis:

# a) “IMC”, em função das categorias da variável “Sexo”;

base1 |>
  group_by(Sexo) |>
  summarise(
    media = mean(IMC, na.rm = TRUE),
    desvio_padrao = sd(IMC, na.rm = TRUE),
    coef_var = (sd(IMC, na.rm = TRUE) / mean(IMC, na.rm = TRUE)) * 100
  )

# b) “TR”, em função das categorias da variável “Sexo”;

base1 |>
  group_by(Sexo) |>
  summarise(
    media = mean(TR, na.rm = TRUE),
    desvio_padrao = sd(TR, na.rm = TRUE),
    coef_var = (sd(TR, na.rm = TRUE) / mean(TR, na.rm = TRUE)) * 100
  )

# c) “SB”, em função das categorias da variável “Escola”.

base1 |>
  group_by(Escola) |>
  summarise(
    media = mean(SB, na.rm = TRUE),
    desvio_padrao = sd(SB, na.rm = TRUE),
    coef_var = (sd(SB, na.rm = TRUE) / mean(SB, na.rm = TRUE)) * 100
  )

# Tire conclusões nas três análises.

# 5) Faça um gráfico adequado para medir variabilidade (não pode ser o gráfico de caixa) das
# análises dos itens 4a, 4b, 4c e tire conclusões.

# a) Item 4a

base1 |>
  ggplot(aes(x = IMC, fill = Sexo)) +
  geom_histogram(alpha = 0.6, position = "identity", bins = 20) +
  facet_wrap(~Sexo) +
  labs(title = "Distribuição do IMC por Sexo")

# b) Item 4b

base1 |>
  ggplot(aes(x = TR, fill = Sexo)) +
  geom_histogram(alpha = 0.6, position = "identity", bins = 20) +
  facet_wrap(~Sexo) +
  labs(title = "Distribuição de TR por Sexo")

# c) Item 4c

base1 |>
  ggplot(aes(x = SB, fill = Escola)) +
  geom_histogram(alpha = 0.6, position = "identity", bins = 20) +
  facet_wrap(~Escola) +
  labs(title = "Distribuição de SB por Escola")

# 6) Faça os gráficos de caixa das análises dos itens 4a, 4b, 4c e tire conclusões.

# a) Item 4a

base1 |>
  ggplot(aes(x = Sexo, y = IMC, fill = Sexo)) +
  geom_boxplot() +
  labs(title = "Boxplot do IMC por Sexo")

# b) Item 4b

base1 |>
  ggplot(aes(x = Sexo, y = TR, fill = Sexo)) +
  geom_boxplot() +
  labs(title = "Boxplot de TR por Sexo")

# c) Item 4c

base1 |>
  ggplot(aes(x = Escola, y = SB, fill = Escola)) +
  geom_boxplot() +
  labs(title = "Boxplot de SB por Escola")