package com.example.controller;

@RestController
@RequestMapping("/admin")
@CrossOrigin(origins = "*")
@PreAuthorize("hasAuthority('ADMIN')")
public class adminController {

    @Autowired
    private UsuarioRepository usuarioRepository;

    // 1. LISTAR TODOS OS USUÁRIOS (COM PAGINAÇÃO)
    @GetMapping("/usuarios")
    public ResponseEntity<Map<String, Object>> listarUsuarios(
            @RequestParam(defaultValue = "0") int pagina,
            @RequestParam(defaultValue = "10") int tamanho,
            @RequestParam(required = false) String busca) {

        Page<Usuario> pageUsuarios;

        if (busca != null && !busca.isEmpty()) {
            // Se tiver busca, filtra por nome ou email
            pageUsuarios = usuarioRepository.findAll(
                    PageRequest.of(pagina, tamanho, Sort.by("id").descending())
            ); // Idealmente teria um método de busca personalizado
        } else {
            pageUsuarios = usuarioRepository.findAll(
                    PageRequest.of(pagina, tamanho, Sort.by("id").descending())
            );
        }

        // Converter para DTO
        List<UsuarioResponseDTO> dtos = pageUsuarios.getContent().stream()
                .map(u -> new UsuarioResponseDTO(
                        u.getId(),
                        u.getNome(),
                        u.getEmail(),
                        u.getDataNascimento(),
                        u.getEmailConfirmado(),
                        u.getPerfil(),
                        u.getBloqueado()
                ))
                .collect(Collectors.toList());

        Map<String, Object> response = new HashMap<>();
        response.put("usuarios", dtos);
        response.put("paginaAtual", pageUsuarios.getNumber());
        response.put("totalItens", pageUsuarios.getTotalElements());
        response.put("totalPaginas", pageUsuarios.getTotalPages());
        response.put("tamanhoPagina", pageUsuarios.getSize());

        return ResponseEntity.ok(response);
    }

    // 2. BUSCAR USUÁRIO POR ID
    @GetMapping("/usuarios/{id}")
    public ResponseEntity<UsuarioResponseDTO> buscarUsuario(@PathVariable Long id) {
        Usuario usuario = usuarioRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado com ID: " + id));

        UsuarioResponseDTO dto = new UsuarioResponseDTO(
                usuario.getId(),
                usuario.getNome(),
                usuario.getEmail(),
                usuario.getDataNascimento(),
                usuario.getEmailConfirmado(),
                usuario.getPerfil(),
                usuario.getBloqueado()
        );

        return ResponseEntity.ok(dto);
    }

    // 3. BLOQUEAR/DESBLOQUEAR USUÁRIO
    @PutMapping("/usuarios/{id}/bloquear")
    public ResponseEntity<Map<String, Object>> bloquearUsuario(@PathVariable Long id) {
        Usuario usuario = usuarioRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado com ID: " + id));

        // Inverter status de bloqueio
        usuario.setBloqueado(!usuario.getBloqueado());
        usuarioRepository.save(usuario);

        String mensagem = usuario.getBloqueado() ?
                "Usuário bloqueado com sucesso" :
                "Usuário desbloqueado com sucesso";

        Map<String, Object> response = new HashMap<>();
        response.put("mensagem", mensagem);
        response.put("status", usuario.getBloqueado() ? "BLOQUEADO" : "ATIVO");
        response.put("usuarioId", usuario.getId());
        response.put("usuarioNome", usuario.getNome());

        return ResponseEntity.ok(response);
    }

    // 4. ATUALIZAR PERFIL DO USUÁRIO (opcional)
    @PutMapping("/usuarios/{id}/perfil")
    public ResponseEntity<Map<String, String>> atualizarPerfil(
            @PathVariable Long id,
            @RequestBody Map<String, String> request) {

        Usuario usuario = usuarioRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));

        String novoPerfil = request.get("perfil");
        if (novoPerfil != null && (novoPerfil.equals("ADMIN") || novoPerfil.equals("USER"))) {
            usuario.setPerfil(novoPerfil);
            usuarioRepository.save(usuario);
        }

        Map<String, String> response = new HashMap<>();
        response.put("mensagem", "Perfil atualizado para: " + usuario.getPerfil());

        return ResponseEntity.ok(response);
    }

    // 5. ESTATÍSTICAS RÁPIDAS (versão simplificada do dashboard)
    @GetMapping("/estatisticas")
    public ResponseEntity<Map<String, Object>> getEstatisticasRapidas() {
        long totalUsuarios = usuarioRepository.count();
        long usuariosBloqueados = usuarioRepository.findAll().stream()
                .filter(Usuario::getBloqueado)
                .count();
        long usuariosAtivos = totalUsuarios - usuariosBloqueados;

        Map<String, Object> stats = new HashMap<>();
        stats.put("totalUsuarios", totalUsuarios);
        stats.put("usuariosAtivos", usuariosAtivos);
        stats.put("usuariosBloqueados", usuariosBloqueados);

        return ResponseEntity.ok(stats);
    }
}
