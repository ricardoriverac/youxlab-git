package com.example.service;

public class DashboardService {

    @Autowired
    private ApostaRepository apostaRepository;

    @Autowired
    private UsuarioRepository usuarioRepository;

    // =============== DASHBOARD DO USUÁRIO COMUM ===============
    public Map<String, Object> getDashboardUsuario(String email) {
        Usuario usuario = usuarioRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado: " + email));

        // Buscar todas as apostas do usuário
        List<Aposta> apostas = apostaRepository.findByUsuario(usuario);

        // Se não tiver apostas, retorna dashboard vazio
        if (apostas.isEmpty()) {
            return criarDashboardVazio(usuario);
        }

        // 1. ESTATÍSTICAS GERAIS
        long totalJogos = apostas.size();

        // Jogos ganhos: encerrados com valorGanho > valorApostado
        long jogosGanhos = apostas.stream()
                .filter(a -> a.getStatus().equals("ENCERRADO") &&
                        a.getValorGanho() != null &&
                        a.getValorGanho() > a.getValorApostado())
                .count();

        // Jogos perdidos: estourou OU encerrou com valorGanho < valorApostado
        long jogosPerdidos = apostas.stream()
                .filter(a -> a.getStatus().equals("ESTOUROU") ||
                        (a.getStatus().equals("ENCERRADO") &&
                                a.getValorGanho() != null &&
                                a.getValorGanho() < a.getValorApostado()))
                .count();

        // Jogos em andamento
        long jogosAndamento = apostas.stream()
                .filter(a -> a.getStatus().equals("ATIVO"))
                .count();

        // 2. VALORES MONETÁRIOS
        double totalApostado = apostas.stream()
                .mapToDouble(Aposta::getValorApostado)
                .sum();

        double totalGanho = apostas.stream()
                .filter(a -> a.getValorGanho() != null)
                .mapToDouble(Aposta::getValorGanho)
                .sum();

        double saldo = totalGanho - totalApostado;

        // 3. MÉDIAS
        double mediaAposta = totalApostado / totalJogos;
        double maiorGanho = apostas.stream()
                .filter(a -> a.getValorGanho() != null)
                .mapToDouble(Aposta::getValorGanho)
                .max()
                .orElse(0);

        // 4. DIAMANTES
        int totalDiamantes = apostas.stream()
                .mapToInt(Aposta::getDiamantesEncontrados)
                .sum();

        double mediaDiamantes = (double) totalDiamantes / totalJogos;

        // 5. HISTÓRICO DETALHADO (últimas 20 apostas)
        List<Map<String, Object>> historico = apostas.stream()
                .sorted((a1, a2) -> a2.getDataHora().compareTo(a1.getDataHora()))
                .limit(20)
                .map(a -> {
                    Map<String, Object> item = new LinkedHashMap<>();
                    item.put("id", a.getId());
                    item.put("data", a.getDataHora().toString());
                    item.put("dataFormatada", formatarData(a.getDataHora()));
                    item.put("valorApostado", a.getValorApostado());
                    item.put("valorGanho", a.getValorGanho());
                    item.put("status", a.getStatus());
                    item.put("diamantes", a.getDiamantesEncontrados());

                    // Calcular lucro/prejuízo
                    if (a.getValorGanho() != null) {
                        double lucro = a.getValorGanho() - a.getValorApostado();
                        item.put("lucro", lucro);
                        item.put("resultado", lucro > 0 ? "GANHOU" : lucro < 0 ? "PERDEU" : "EMPATE");

                        // Calcular multiplicador
                        double multiplicador = a.getValorGanho() / a.getValorApostado();
                        item.put("multiplicador", Math.round(multiplicador * 100.0) / 100.0);
                    } else {
                        item.put("lucro", 0);
                        item.put("resultado", a.getStatus().equals("ATIVO") ? "EM ANDAMENTO" : "PENDENTE");
                        item.put("multiplicador", 0);
                    }
                    return item;
                })
                .collect(Collectors.toList());

        // 6. ESTATÍSTICAS POR MÊS (para gráficos)
        Map<String, Object> estatisticasMensais = calcularEstatisticasMensais(apostas);

        // Montar resposta completa
        Map<String, Object> dashboard = new LinkedHashMap<>();
        dashboard.put("usuario", usuario.getNome());
        dashboard.put("email", usuario.getEmail());
        dashboard.put("dataCadastro", usuario.getDataNascimento());

        // Estatísticas resumidas
        Map<String, Object> resumo = new LinkedHashMap<>();
        resumo.put("totalJogos", totalJogos);
        resumo.put("jogosGanhos", jogosGanhos);
        resumo.put("jogosPerdidos", jogosPerdidos);
        resumo.put("jogosAndamento", jogosAndamento);
        resumo.put("totalApostado", totalApostado);
        resumo.put("totalGanho", totalGanho);
        resumo.put("saldo", saldo);
        resumo.put("mediaAposta", Math.round(mediaAposta * 100.0) / 100.0);
        resumo.put("maiorGanho", maiorGanho);
        resumo.put("totalDiamantes", totalDiamantes);
        resumo.put("mediaDiamantes", Math.round(mediaDiamantes * 100.0) / 100.0);

        dashboard.put("resumo", resumo);
        dashboard.put("historico", historico);
        dashboard.put("estatisticasMensais", estatisticasMensais);

        return dashboard;
    }

    // =============== DASHBOARD DO ADMINISTRADOR ===============
    public Map<String, Object> getDashboardAdmin() {
        // 1. ESTATÍSTICAS DE USUÁRIOS
        List<Usuario> todosUsuarios = usuarioRepository.findAll();
        long totalUsuarios = todosUsuarios.size();
        long usuariosBloqueados = todosUsuarios.stream()
                .filter(Usuario::getBloqueado)
                .count();
        long usuariosConfirmados = todosUsuarios.stream()
                .filter(Usuario::getEmailConfirmado)
                .count();

        // 2. ESTATÍSTICAS DE APOSTAS
        List<Aposta> todasApostas = apostaRepository.findAll();
        long totalApostas = todasApostas.size();

        long apostasAtivas = todasApostas.stream()
                .filter(a -> "ATIVO".equals(a.getStatus()))
                .count();

        long apostasEncerradas = todasApostas.stream()
                .filter(a -> "ENCERRADO".equals(a.getStatus()))
                .count();

        long apostasEstouradas = todasApostas.stream()
                .filter(a -> "ESTOUROU".equals(a.getStatus()))
                .count();

        // 3. VALORES FINANCEIROS
        double totalApostadoGeral = todasApostas.stream()
                .mapToDouble(Aposta::getValorApostado)
                .sum();

        double totalPagoUsuarios = todasApostas.stream()
                .filter(a -> a.getValorGanho() != null && a.getStatus().equals("ENCERRADO"))
                .mapToDouble(Aposta::getValorGanho)
                .sum();

        double totalPerdidoUsuarios = todasApostas.stream()
                .filter(a -> a.getStatus().equals("ESTOUROU"))
                .mapToDouble(Aposta::getValorApostado)
                .sum();

        double lucroCasa = totalPerdidoUsuarios - (totalPagoUsuarios - (totalApostadoGeral - totalPerdidoUsuarios));

        // 4. TOP USUÁRIOS
        List<Map<String, Object>> topUsuarios = todosUsuarios.stream()
                .map(u -> {
                    List<Aposta> apostasUsuario = apostaRepository.findByUsuario(u);
                    double totalApostado = apostasUsuario.stream()
                            .mapToDouble(Aposta::getValorApostado)
                            .sum();
                    double totalGanho = apostasUsuario.stream()
                            .filter(a -> a.getValorGanho() != null)
                            .mapToDouble(Aposta::getValorGanho)
                            .sum();
                    long qtdApostas = apostasUsuario.size();

                    Map<String, Object> dados = new LinkedHashMap<>();
                    dados.put("id", u.getId());
                    dados.put("nome", u.getNome());
                    dados.put("email", u.getEmail());
                    dados.put("totalApostado", totalApostado);
                    dados.put("totalGanho", totalGanho);
                    dados.put("saldo", totalGanho - totalApostado);
                    dados.put("quantidadeApostas", qtdApostas);
                    dados.put("bloqueado", u.getBloqueado());
                    return dados;
                })
                .sorted((u1, u2) -> Double.compare(
                        (Double) u2.get("totalApostado"),
                        (Double) u1.get("totalApostado")
                ))
                .limit(10)
                .collect(Collectors.toList());

        // 5. APOSTAS RECENTES
        List<Map<String, Object>> apostasRecentes = todasApostas.stream()
                .sorted((a1, a2) -> a2.getDataHora().compareTo(a1.getDataHora()))
                .limit(20)
                .map(a -> {
                    Map<String, Object> item = new LinkedHashMap<>();
                    item.put("id", a.getId());
                    item.put("usuario", a.getUsuario().getNome());
                    item.put("usuarioId", a.getUsuario().getId());
                    item.put("data", a.getDataHora().toString());
                    item.put("dataFormatada", formatarData(a.getDataHora()));
                    item.put("valorApostado", a.getValorApostado());
                    item.put("valorGanho", a.getValorGanho());
                    item.put("status", a.getStatus());
                    item.put("diamantes", a.getDiamantesEncontrados());

                    if (a.getValorGanho() != null && a.getValorApostado() > 0) {
                        double multiplicador = a.getValorGanho() / a.getValorApostado();
                        item.put("multiplicador", Math.round(multiplicador * 100.0) / 100.0);
                    }
                    return item;
                })
                .collect(Collectors.toList());

        // 6. ESTATÍSTICAS POR DIA (últimos 7 dias)
        Map<String, Object> estatisticasDiarias = calcularEstatisticasDiarias(todasApostas);

        // Montar dashboard admin
        Map<String, Object> dashboard = new LinkedHashMap<>();

        // Resumo geral
        Map<String, Object> resumoGeral = new LinkedHashMap<>();
        resumoGeral.put("totalUsuarios", totalUsuarios);
        resumoGeral.put("usuariosAtivos", totalUsuarios - usuariosBloqueados);
        resumoGeral.put("usuariosBloqueados", usuariosBloqueados);
        resumoGeral.put("usuariosConfirmados", usuariosConfirmados);
        resumoGeral.put("totalApostas", totalApostas);
        resumoGeral.put("apostasAtivas", apostasAtivas);
        resumoGeral.put("apostasEncerradas", apostasEncerradas);
        resumoGeral.put("apostasEstouradas", apostasEstouradas);

        dashboard.put("resumoGeral", resumoGeral);

        // Financeiro
        Map<String, Object> financeiro = new LinkedHashMap<>();
        financeiro.put("totalApostadoGeral", totalApostadoGeral);
        financeiro.put("totalPagoUsuarios", totalPagoUsuarios);
        financeiro.put("totalPerdidoUsuarios", totalPerdidoUsuarios);
        financeiro.put("lucroCasa", lucroCasa);

        dashboard.put("financeiro", financeiro);
        dashboard.put("topUsuarios", topUsuarios);
        dashboard.put("apostasRecentes", apostasRecentes);
        dashboard.put("estatisticasDiarias", estatisticasDiarias);

        return dashboard;
    }

    // =============== MÉTODOS AUXILIARES ===============

    private Map<String, Object> criarDashboardVazio(Usuario usuario) {
        Map<String, Object> dashboard = new LinkedHashMap<>();
        dashboard.put("usuario", usuario.getNome());
        dashboard.put("email", usuario.getEmail());

        Map<String, Object> resumo = new LinkedHashMap<>();
        resumo.put("totalJogos", 0);
        resumo.put("jogosGanhos", 0);
        resumo.put("jogosPerdidos", 0);
        resumo.put("jogosAndamento", 0);
        resumo.put("totalApostado", 0);
        resumo.put("totalGanho", 0);
        resumo.put("saldo", 0);
        resumo.put("mensagem", "Você ainda não fez nenhuma aposta. Comece agora!");

        dashboard.put("resumo", resumo);
        dashboard.put("historico", Collections.emptyList());

        return dashboard;
    }

    private String formatarData(java.time.LocalDateTime data) {
        java.time.format.DateTimeFormatter formatter =
                java.time.format.DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
        return data.format(formatter);
    }

    private Map<String, Object> calcularEstatisticasMensais(List<Aposta> apostas) {
        Map<String, Object> resultado = new LinkedHashMap<>();

        // Agrupar por mês/ano
        Map<String, List<Aposta>> porMes = apostas.stream()
                .collect(Collectors.groupingBy(
                        a -> a.getDataHora().getYear() + "-" +
                                String.format("%02d", a.getDataHora().getMonthValue())
                ));

        List<String> meses = new ArrayList<>();
        List<Long> quantidades = new ArrayList<>();
        List<Double> valores = new ArrayList<>();

        porMes.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .forEach(entry -> {
                    meses.add(entry.getKey());
                    quantidades.add((long) entry.getValue().size());

                    double totalMes = entry.getValue().stream()
                            .mapToDouble(Aposta::getValorApostado)
                            .sum();
                    valores.add(totalMes);
                });

        resultado.put("meses", meses);
        resultado.put("quantidades", quantidades);
        resultado.put("valores", valores);

        return resultado;
    }

    private Map<String, Object> calcularEstatisticasDiarias(List<Aposta> apostas) {
        Map<String, Object> resultado = new LinkedHashMap<>();

        // Últimos 7 dias
        java.time.LocalDate hoje = java.time.LocalDate.now();
        List<String> dias = new ArrayList<>();
        List<Long> apostasDia = new ArrayList<>();
        List<Double> valoresDia = new ArrayList<>();

        for (int i = 6; i >= 0; i--) {
            java.time.LocalDate data = hoje.minusDays(i);
            dias.add(data.format(java.time.format.DateTimeFormatter.ofPattern("dd/MM")));

            long count = apostas.stream()
                    .filter(a -> a.getDataHora().toLocalDate().equals(data))
                    .count();

            double total = apostas.stream()
                    .filter(a -> a.getDataHora().toLocalDate().equals(data))
                    .mapToDouble(Aposta::getValorApostado)
                    .sum();

            apostasDia.add(count);
            valoresDia.add(total);
        }

        resultado.put("dias", dias);
        resultado.put("apostasDia", apostasDia);
        resultado.put("valoresDia", valoresDia);

        return resultado;
    }
}
