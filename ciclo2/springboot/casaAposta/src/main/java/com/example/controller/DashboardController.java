package com.example.controller;

import com.example.dto.DashboardAdminDTO;
import com.example.dto.DashboardUserDTO;
import com.example.service.DashboardService;
import com.example.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
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

        @GetMapping("/user/{userId}")
        public ResponseEntity dashboardUser(@PathVariable Long userId) {
            try {
                var user = userService.buscarPorId(userId);

                DashboardUserDTO dashboard = dashboardService.obterDadosUser(userId);

                return ResponseEntity.ok(dashboard);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao carregar dashboard do usuário: " + e.getMessage());
            }
        }




    }
