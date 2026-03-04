package com.example.controller;

@RestController
@RequestMapping("/dashboard")
@CrossOrigin(origins = "*")
public class DashboardController {

    @Autowired
    private DashboardService dashboardService;

    // DASHBOARD DO USUÁRIO COMUM - qualquer usuário logado pode acessar
    @GetMapping("/usuario")
    public ResponseEntity<Map<String, Object>> getDashboardUsuario() {
        // Pega o email do usuário logado (vindo do JWT)
        String email = SecurityContextHolder.getContext().getAuthentication().getName();
        System.out.println("📊 Usuário acessando dashboard: " + email);

        Map<String, Object> dashboard = dashboardService.getDashboardUsuario(email);
        return ResponseEntity.ok(dashboard);
    }

    // DASHBOARD DO ADMINISTRADOR - só admin pode acessar
    @GetMapping("/admin")
    @PreAuthorize("hasAuthority('ADMIN')")
    public ResponseEntity<Map<String, Object>> getDashboardAdmin() {
        System.out.println("👑 Admin acessando dashboard administrativo");

        Map<String, Object> dashboard = dashboardService.getDashboardAdmin();
        return ResponseEntity.ok(dashboard);
    }

    // ENDPOINT PARA TESTE - verificar se o usuário está logado
    @GetMapping("/teste")
    public ResponseEntity<Map<String, String>> teste() {
        String email = SecurityContextHolder.getContext().getAuthentication().getName();
        String perfil = SecurityContextHolder.getContext().getAuthentication().getAuthorities().toString();

        Map<String, String> response = Map.of(
                "mensagem", "Usuário autenticado com sucesso!",
                "email", email,
                "perfil", perfil
        );

        return ResponseEntity.ok(response);
    }
}
