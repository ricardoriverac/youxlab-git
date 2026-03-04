package com.example.controller;



@RestController
@RequestMapping("/auth")
@CrossOrigin(origins = "*")
public class AuthController {

    @Autowired
    private AuthService authService;

    // CADASTRO DE USUÁRIO
    @PostMapping("/cadastro")
    public ResponseEntity<Map<String, Object>> cadastrar(@Valid @RequestBody UsuarioRequestDTO request) {
        UsuarioResponseDTO response = authService.cadastrar(request);

        Map<String, Object> resposta = new HashMap<>();
        resposta.put("mensagem", "Usuário cadastrado com sucesso! Verifique seu email para confirmar o cadastro.");
        resposta.put("usuario", response);

        return ResponseEntity.status(HttpStatus.CREATED).body(resposta);
    }

    // CONFIRMAR EMAIL
    @GetMapping("/confirmar-email")
    public ResponseEntity<Map<String, String>> confirmarEmail(@RequestParam("token") String token) {
        authService.confirmarEmail(token);

        Map<String, String> resposta = new HashMap<>();
        resposta.put("mensagem", "Email confirmado com sucesso! Agora você pode fazer login.");

        return ResponseEntity.ok(resposta);
    }

    // LOGIN
    @PostMapping("/login")
    public ResponseEntity<LoginResponseDTO> login(@Valid @RequestBody LoginRequestDTO request) {
        LoginResponseDTO response = authService.login(request);
        return ResponseEntity.ok(response);
    }

    // ESQUECI SENHA
    @PostMapping("/esqueci-senha")
    public ResponseEntity<Map<String, String>> esqueciSenha(@RequestBody Map<String, String> request) {
        String email = request.get("email");
        authService.esqueciSenha(email);

        Map<String, String> resposta = new HashMap<>();
        resposta.put("mensagem", "Se o email existir, você receberá um link para redefinir sua senha.");

        return ResponseEntity.ok(resposta);
    }

    // REDEFINIR SENHA
    @PostMapping("/redefinir-senha")
    public ResponseEntity<Map<String, String>> redefinirSenha(@RequestBody Map<String, String> request) {
        String token = request.get("token");
        String novaSenha = request.get("novaSenha");
        String confirmacaoSenha = request.get("confirmacaoSenha");

        authService.redefinirSenha(token, novaSenha, confirmacaoSenha);

        Map<String, String> resposta = new HashMap<>();
        resposta.put("mensagem", "Senha redefinida com sucesso! Agora você pode fazer login com sua nova senha.");

        return ResponseEntity.ok(resposta);
    }

    // VERIFICAR TOKEN (para o front-end validar se token é válido)
    @GetMapping("/verificar-token")
    public ResponseEntity<Map<String, Object>> verificarToken() {
        // Se chegou aqui é porque o token é válido (filtro JWT já validou)
        Map<String, Object> resposta = new HashMap<>();
        resposta.put("valido", true);
        resposta.put("mensagem", "Token válido");

        return ResponseEntity.ok(resposta);
    }
}
