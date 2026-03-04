package com.example.service;

public class JogoService {

    @Autowired
    private ApostaRepository apostaRepository;

    @Autowired
    private JogadaRepository jogadaRepository;

    @Autowired
    private UsuarioRepository usuarioRepository;

    // INICIAR APOSTA
    @Transactional
    public Aposta iniciarAposta(String email, Double valorApostado) {
        Usuario usuario = usuarioRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));

        // Verificar se usuário está bloqueado
        if (usuario.getBloqueado()) {
            throw new RuntimeException("Usuário bloqueado");
        }

        // Verificar se já tem aposta ativa
        List<Aposta> ativas = apostaRepository.findByUsuarioAndStatus(usuario, "ATIVO");
        if (!ativas.isEmpty()) {
            throw new RuntimeException("Você já tem uma aposta em andamento");
        }

        // Gerar tabuleiro (5x5 com bombas e diamantes)
        String[][] tabuleiro = gerarTabuleiro();

        // Converter para JSON simples
        String tabuleiroJson = converterTabuleiroParaJson(tabuleiro);

        // Criar aposta
        Aposta aposta = new Aposta();
        aposta.setUsuario(usuario);
        aposta.setValorApostado(valorApostado);
        aposta.setStatus("ATIVO");
        aposta.setDiamantesEncontrados(0);
        aposta.setTabuleiro(tabuleiroJson);
        aposta.setDataHora(LocalDateTime.now());

        return apostaRepository.save(aposta);
    }

    // JOGAR (clicar em célula)
    @Transactional
    public Map<String, Object> jogar(String email, Long apostaId, Integer x, Integer y) {
        Usuario usuario = usuarioRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));

        Aposta aposta = apostaRepository.findByIdAndUsuario(apostaId, usuario)
                .orElseThrow(() -> new RuntimeException("Aposta não encontrada"));

        // Verificar se aposta está ativa
        if (!aposta.getStatus().equals("ATIVO")) {
            throw new RuntimeException("Esta aposta não está mais ativa");
        }

        // Verificar se célula já foi jogada
        if (jogadaRepository.existsByApostaAndPosicaoXAndPosicaoY(aposta, x, y)) {
            throw new RuntimeException("Esta célula já foi revelada");
        }

        // Recuperar tabuleiro
        String[][] tabuleiro = converterJsonParaTabuleiro(aposta.getTabuleiro());

        // Verificar o que tem na célula
        String tipo = tabuleiro[x][y];

        // Registrar jogada
        Jogada jogada = new Jogada();
        jogada.setAposta(aposta);
        jogada.setPosicaoX(x);
        jogada.setPosicaoY(y);
        jogada.setTipo(tipo);
        jogada.setDataHora(LocalDateTime.now());
        jogadaRepository.save(jogada);

        Map<String, Object> resultado = new HashMap<>();
        resultado.put("x", x);
        resultado.put("y", y);
        resultado.put("tipo", tipo);

        if (tipo.equals("BOMBA")) {
            // Perdeu tudo
            aposta.setStatus("ESTOUROU");
            aposta.setValorGanho(0.0);
            apostaRepository.save(aposta);

            resultado.put("fimDeJogo", true);
            resultado.put("mensagem", "💥 BOOM! Você encontrou uma bomba e perdeu tudo!");
            resultado.put("valorPerdido", aposta.getValorApostado());
        } else {
            // Achou diamante
            aposta.setDiamantesEncontrados(aposta.getDiamantesEncontrados() + 1);
            apostaRepository.save(aposta);

            Double valorAtual = calcularValorAtual(aposta);
            resultado.put("fimDeJogo", false);
            resultado.put("diamantes", aposta.getDiamantesEncontrados());
            resultado.put("valorAtual", valorAtual);
            resultado.put("mensagem", "💎 Parabéns! Você encontrou um diamante!");
        }

        return resultado;
    }

    // ENCERRAR APOSTA MANUALMENTE
    @Transactional
    public Map<String, Object> encerrarAposta(String email, Long apostaId) {
        Usuario usuario = usuarioRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));

        Aposta aposta = apostaRepository.findByIdAndUsuario(apostaId, usuario)
                .orElseThrow(() -> new RuntimeException("Aposta não encontrada"));

        if (!aposta.getStatus().equals("ATIVO")) {
            throw new RuntimeException("Esta aposta não está mais ativa");
        }

        Double valorGanho = calcularValorAtual(aposta);

        aposta.setStatus("ENCERRADO");
        aposta.setValorGanho(valorGanho);
        apostaRepository.save(aposta);

        Map<String, Object> resultado = new HashMap<>();
        resultado.put("mensagem", "Aposta encerrada com sucesso!");
        resultado.put("valorApostado", aposta.getValorApostado());
        resultado.put("diamantes", aposta.getDiamantesEncontrados());
        resultado.put("valorGanho", valorGanho);

        return resultado;
    }

    // CONSULTAR ESTADO DO JOGO
    public Map<String, Object> consultarEstado(String email, Long apostaId) {
        Usuario usuario = usuarioRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));

        Aposta aposta = apostaRepository.findByIdAndUsuario(apostaId, usuario)
                .orElseThrow(() -> new RuntimeException("Aposta não encontrada"));

        List<Jogada> jogadas = jogadaRepository.findByAposta(aposta);

        // Criar matriz 5x5 com células reveladas
        String[][] tabuleiroRevelado = new String[5][5];
        for (int i = 0; i < 5; i++) {
            Arrays.fill(tabuleiroRevelado[i], "?");
        }

        for (Jogada j : jogadas) {
            tabuleiroRevelado[j.getPosicaoX()][j.getPosicaoY()] = j.getTipo().equals("DIAMANTE") ? "💎" : "💥";
        }

        Map<String, Object> estado = new HashMap<>();
        estado.put("apostaId", aposta.getId());
        estado
    }
}