package com.example.controller;

import com.example.dto.DashboardAdminDTO;
import com.example.dto.DashboardUserDTO;
import com.example.model.User;
import com.example.service.DashboardService;
import com.example.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/dashboard")
public class DashboardController {

        @Autowired
        private DashboardService dashboardService;

        @Autowired
        private UserService userService;

        @GetMapping("/dashboard-todos")
        public ResponseEntity dashboard() {
            try {
                DashboardAdminDTO dashboard = dashboardService.obterDadosAdmin();
                return ResponseEntity.ok(dashboard);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao carregar dashboard: " + e.getMessage());
            }
        }

        @GetMapping("/admin")
        public ResponseEntity dashboardAdmin() {
            try {
               DashboardAdminDTO dashboard = dashboardService.obterDadosAdmin();

                return ResponseEntity.ok(dashboard);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao carregar dashboard do admin: " + e.getMessage());
            }
        }

        @GetMapping("/meu-dashboard")
        public ResponseEntity meuDashboard(@AuthenticationPrincipal User userLogado) {
            try {
                DashboardUserDTO dashboard = dashboardService.obterDadosUser(userLogado.getId());
                return ResponseEntity.ok(dashboard);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao carregar dashboard: " + e.getMessage());
            }
        }




    }
