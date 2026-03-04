package com.example.controller;

@RestController
@RequestMapping("/apostas")
@CrossOrigin(origins = "*")
public class ApostaController {

    @Autowired
    private JogoService jogoService;

    // Iniciar nova aposta
    @PostMapping("/iniciar")
    public ResponseEntity<Map<String, Object>> iniciarAposta(@Valid @RequestBody ApostaRequestDTO request) {
        String email = SecurityContextHolder.getContext().getAuthentication().getName();

        Aposta aposta = jogoService.iniciarAposta(email, request.getValorApostado());

        Map<String, Object> response = Map.of(
                "mensagem", "Aposta iniciada com sucesso!",
                "apostaId", aposta.getId(),
                "valorApostado", aposta.getValorApostado(),
                "status", aposta.getStatus()
        );

        return ResponseEntity.ok(response);
    }

    // Jogar (revelar célula)
    @PostMapping("/{id}/jogar")
    public ResponseEntity<Map<String, Object>> jogar(
            @PathVariable Long id,
            @Valid @RequestBody JogadaRequestDTO request) {

        String email = SecurityContextHolder.getContext().getAuthentication().getName();

        Map<String, Object> resultado = jogoService.jogar(email, id, request.getX(), request.getY());

        return ResponseEntity.ok(resultado);
    }

    // Encerrar aposta manualmente
    @PostMapping("/{id}/encerrar")
    public ResponseEntity<Map<String, Object>> encerrarAposta(@PathVariable Long id) {
        String email = SecurityContextHolder.getContext().getAuthentication().getName();

        Map<String, Object> resultado = jogoService.encerrarAposta(email, id);

        return ResponseEntity.ok(resultado);
    }

    // Consultar estado do jogo
    @GetMapping("/{id}/estado")
    public ResponseEntity<Map<String, Object>> consultarEstado(@PathVariable Long id) {
        String email = SecurityContextHolder.getContext().getAuthentication().getName();

        Map<String, Object> estado = jogoService.consultarEstado(email, id);

        return ResponseEntity.ok(estado);
    }
}
