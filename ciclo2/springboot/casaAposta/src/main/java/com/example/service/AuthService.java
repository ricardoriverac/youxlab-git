package com.example.service;

import org.springframework.stereotype.Service;

@Service
public class AuthService {

    @Autowired
    private UsuarioRepository usuarioRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private EmailService emailService;

    @Autowired
    private JwtUtil jwtUtil;

    // CADASTRO
    public UsuarioResponseDTO cadastrar(UsuarioRequestDTO request) {
        // Verificar se senhas conferem
        if (!request.getSenha().equals(request.getConfirmacaoSenha())) {
            throw new RuntimeException("Senhas não conferem");
        }

        // Verificar se email já existe
        if (usuarioRepository.existsByEmail(request.getEmail())) {
            throw new RuntimeException("Email já cadastrado");
        }

        // Criar usuário
        Usuario usuario = new Usuario();
        usuario.setNome(request.getNome());
        usuario.setEmail(request.getEmail());
        usuario.setDataNascimento(request.getDataNascimento());
        usuario.setSenha(passwordEncoder.encode(request.getSenha()));
        usuario.setEmailConfirmado(false);

        // Gerar token de confirmação
        String token = UUID.randomUUID().toString();
        usuario.setTokenConfirmacao(token);
        usuario.setTokenExpiracao(LocalDateTime.now().plusHours(24));

        // Salvar
        Usuario salvo = usuarioRepository.save(usuario);

        // Enviar email
        emailService.enviarEmailConfirmacao(salvo.getEmail(), token);

        return new UsuarioResponseDTO(
                salvo.getId(), salvo.getNome(), salvo.getEmail(),
                salvo.getDataNascimento(), salvo.getEmailConfirmado(),
                salvo.getPerfil(), salvo.getBloqueado()
        );
    }

    // CONFIRMAR EMAIL
    public void confirmarEmail(String token) {
        Usuario usuario = usuarioRepository.findByTokenConfirmacao(token)
                .orElseThrow(() -> new RuntimeException("Token inválido"));

        if (usuario.getTokenExpiracao().isBefore(LocalDateTime.now())) {
            throw new RuntimeException("Token expirado");
        }

        usuario.setEmailConfirmado(true);
        usuario.setTokenConfirmacao(null);
        usuario.setTokenExpiracao(null);
        usuarioRepository.save(usuario);
    }

    // LOGIN
    public LoginResponseDTO login(LoginRequestDTO request) {
        Usuario usuario = usuarioRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> new RuntimeException("Email ou senha inválidos"));

        // Verificar senha
        if (!passwordEncoder.matches(request.getSenha(), usuario.getSenha())) {
            throw new RuntimeException("Email ou senha inválidos");
        }

        // Verificar se email foi confirmado
        if (!usuario.getEmailConfirmado()) {
            throw new RuntimeException("Email não confirmado. Verifique sua caixa de entrada.");
        }

        // Verificar se usuário está bloqueado
        if (usuario.getBloqueado()) {
            throw new RuntimeException("Usuário bloqueado. Contate o administrador.");
        }

        // Gerar token JWT
        String token = jwtUtil.generateToken(usuario.getEmail(), usuario.getPerfil());

        return new LoginResponseDTO(token, usuario.getEmail(), usuario.getPerfil(), usuario.getNome());
    }

    // ESQUECI SENHA
    public void esqueciSenha(String email) {
        Usuario usuario = usuarioRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("Email não encontrado"));

        String token = UUID.randomUUID().toString();
        usuario.setTokenConfirmacao(token);
        usuario.setTokenExpiracao(LocalDateTime.now().plusHours(1));
        usuarioRepository.save(usuario);

        emailService.enviarEmailRecuperacao(email, token);
    }

    // REDEFINIR SENHA
    public void redefinirSenha(String token, String novaSenha, String confirmacaoSenha) {
        if (!novaSenha.equals(confirmacaoSenha)) {
            throw new RuntimeException("Senhas não conferem");
        }

        Usuario usuario = usuarioRepository.findByTokenConfirmacao(token)
                .orElseThrow(() -> new RuntimeException("Token inválido"));

        if (usuario.getTokenExpiracao().isBefore(LocalDateTime.now())) {
            throw new RuntimeException("Token expirado");
        }

        usuario.setSenha(passwordEncoder.encode(novaSenha));
        usuario.setTokenConfirmacao(null);
        usuario.setTokenExpiracao(null);
        usuarioRepository.save(usuario);
    }
}
