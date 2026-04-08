# Exercício 02

library(dplyr)
library(ggplot2)

# Utilizando a base de dados “dados_salarios.csv” pede-se:

# 1) Retire uma amostra de 220 observações utilizando a sintaxe abaixo:

# Amostra
base = read.csv2("dados_salarios.csv")
set.seed(27072005)
base1 = base[sample(nrow(base), 220),]

# com a amostra retirada, faça a análise dos itens abaixo.

# 2) Para a variável “salario_USD” calcule a média, mediana, percentil5, percentil 25, percentil 75,
# percentil 95, mínimo e máximo. Tire conclusões sobre esses valores;

salario <- base1$salario_USD

media <- mean(salario, na.rm = TRUE)
mediana <- median(salario, na.rm = TRUE)

p5  <- quantile(salario, 0.05, na.rm = TRUE)
p25 <- quantile(salario, 0.25, na.rm = TRUE)
p75 <- quantile(salario, 0.75, na.rm = TRUE)
p95 <- quantile(salario, 0.95, na.rm = TRUE)

minimo <- min(salario, na.rm = TRUE)
maximo <- max(salario, na.rm = TRUE)

resultado <- data.frame(
  media = media,
  mediana = mediana,
  p5 = p5,
  p25 = p25,
  p75 = p75,
  p95 = p95,
  minimo = minimo,
  maximo = maximo
)

resultado

# 3) Calcule a média e a mediana da variável “salario_USD” para cada categoria (2020, 2021, 2022)
# da variável “ano”. Tire conclusões e indique se a mediana é mais apropriada do que a média na
# comparação.

resumo_ano <- base1 |>
  group_by(ano) |>
  summarise(
    media = mean(salario_USD, na.rm = TRUE),
    mediana = median(salario_USD, na.rm = TRUE)
  )

resumo_ano

# 4) Calcule a média e a mediana da variável “salario_USD” para cada categoria (EM, MI, SE, EX)
# da variável “experiencia”, porém antes da fazer a análise junte as categorias SE e EX, ou seja,
# analise a variável “experiencia” considerando 3 categorias. Tire conclusões e indique se a mediana
# é mais apropriada do que a média na comparação.

base1$experiencia2 <- base1$experiencia

base1$experiencia2[base1$experiencia %in% c("SE", "EX")] <- "SE_EX"

media_exp <- tapply(
  base1$salario_USD,
  base1$experiencia2,
  mean,
  na.rm = TRUE
)

mediana_exp <- tapply(
  base1$salario_USD,
  base1$experiencia2,
  median,
  na.rm = TRUE
)

media_exp
mediana_exp

# 5) Faça um gráfico de densidade da variável “salario_USD” separado para cada categoria (EM, MI,
# SE, EX) da variável “experiencia”, porém antes da fazer o gráfico junte as categorias SE e EX.
# Inclua a média e a mediana em cada gráfico. Tire conclusões sobre a assimetria das curvas.

ggplot(base1, aes(x = salario_USD)) +
  geom_density(fill = "lightblue", alpha = 0.5) +
  facet_wrap(~ experiencia2) +
  geom_vline(
    aes(xintercept = mean(salario_USD, na.rm = TRUE)),
    color = "red",
    linetype = "dashed"
  ) +
  geom_vline(
    aes(xintercept = median(salario_USD, na.rm = TRUE)),
    color = "blue",
    linetype = "solid"
  ) +
  labs(
    title = "Distribuição dos salários por nível de experiência",
    x = "Salário (USD)",
    y = "Densidade"
  )