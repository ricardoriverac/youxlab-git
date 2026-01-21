# YouxLab 2025/2 - Ciclo 2 - Exercícios de Pandas para Análise de Dados - Rede Varejista 2025

## 🏪 Contexto de Negócio – Rede Varejista 2025

Você foi contratado como **Analista de Dados Júnior** de uma rede varejista fictícia que atua no interior e capital de São Paulo.
Durante todo o ano de **2025**, a empresa registrou suas vendas em arquivos CSV.

A diretoria deseja entender:
- O faturamento ao longo do ano
- O desempenho das lojas
- Os produtos mais vendidos
- O comportamento dos clientes
- Se as metas anuais foram atingidas

Seu papel é usar **Python + Pandas** para transformar dados brutos em informações úteis para o negócio.

---

## 📦 Bases de dados utilizadas

Durante a análise, você trabalhará com **três arquivos CSV**, simulando um cenário real de dados corporativos. Todos eles fazem parte do mesmo contexto de negócio e devem ser analisados de forma integrada.

### 📄 vendas_2025.csv

Arquivo principal do projeto. Contém o **registro detalhado de todas as vendas realizadas ao longo do ano de 2025**, incluindo informações comerciais, temporais e operacionais.  
É a base central para praticamente todas as análises realizadas ao longo do projeto.

### 📄 cadastro_lojas.csv

Base auxiliar com informações **cadastrais das lojas da rede**, utilizada para enriquecer a base de vendas, permitir análises comparativas entre unidades e avaliar o desempenho das lojas em relação às metas definidas pela empresa.

### 📄 cadastro_produtos.csv

Base auxiliar com o **cadastro dos produtos comercializados pela rede**, utilizada para complementar as análises de vendas, apoiar estudos por categoria e validar informações relacionadas aos produtos.

> ⚠️ Importante: não há instruções explícitas sobre colunas ou estrutura dos arquivos.  
> Parte do seu trabalho como analista de dados é **explorar, entender e validar os dados antes de iniciar qualquer análise**.


---

## 1️⃣ Aquecimento – Conhecendo os dados

1. Exiba as 5 primeiras linhas do DataFrame `vendas`.
2. Exiba as 5 últimas linhas.
3. Verifique quantas linhas e colunas existem.
4. Liste o nome das colunas.
5. Verifique os tipos de dados.

---

## 2️⃣ Exploração e inspeção

6. Utilize `describe()` para as colunas numéricas.
   7. Use `value_counts()` para: 
      - vendas por loja
      - vendas por forma de pagamento
8. Descubra:
   - maior preço unitário
   - quantidade total vendida
9. Verifique valores nulos por coluna.

---

## 3️⃣ Limpeza e tratamento de dados

10. pd.to_
11. Padronize a coluna `loja` (remova espaços e padronize texto).
12. Substitua valores nulos de `desconto` por 0.
13. Trate valores nulos da coluna `produto`.

---

## 4️⃣ Criação de métricas

14. Crie a coluna `preco_final`.
15. Crie a coluna `faturamento`.
16. Crie a coluna `teve_desconto`.
17. Crie a coluna `ticket_medio_item`.

---

## 5️⃣ Filtros e segmentações

18. Filtre vendas da loja Centro.
19. Filtre vendas com faturamento maior que 200.
20. Filtre vendas da categoria Roupas pagas no Pix.
21. Filtre vendas por intervalo de datas.

---

## 6️⃣ Groupby e estatísticas

22. Faturamento total por loja.
23. Faturamento por vendedor.
24. Quantidade total vendida por produto.
25. Ticket médio por loja.
26. Tabela resumo por categoria.

---

## 7️⃣ Rankings

27. Top 5 produtos mais vendidos.
28. Top 3 lojas por faturamento.
29. Ranking de vendedores.

---

## 8️⃣ Merge e análise de metas

30. Faça merge entre vendas e cadastro de lojas.
31. Calcule faturamento por cidade e região.
32. Compare faturamento real com a meta anual.

---

## 9️⃣ Análise temporal

33. Crie colunas de mês e dia da semana.
34. Faturamento mensal.
35. Faturamento por dia da semana.
36. c

---

## 📊 Gráficos

37. Gráfico de linha do faturamento mensal.
38. Gráfico de barras do faturamento por loja.
39. Gráfico dos produtos mais vendidos.

---

## 🏁 Desafio Final

Prepare um resumo executivo contendo:
- Faturamento total do ano
- Top 3 lojas
- Top 5 produtos
- Melhor vendedor
- Comparação Pix vs Cartão
   - Conclusão com sugestões de melhoria

📌 **Entrega:** Notebook `.ipynb` organizado, com títulos em Markdown e código comentado.
