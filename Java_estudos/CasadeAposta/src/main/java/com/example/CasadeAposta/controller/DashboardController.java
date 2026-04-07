package com.example.CasadeAposta.controller;

import com.example.CasadeAposta.dtos.DashbAdminDTO;
import com.example.CasadeAposta.dtos.DashbUserDTO;
import com.example.CasadeAposta.model.User;
import com.example.CasadeAposta.service.DashboardService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;


@RequiredArgsConstructor
public class DashboardController {

    private final DashboardService dashboardService;

    @GetMapping("/dashboard/admin")
    @PreAuthorize("hasRole('ADMIN')")
    public DashbAdminDTO dashboardAdmin() {
        return dashboardService.getDashboardAdmin();
    }

    @GetMapping("/dashboard/usuario")
    public DashbUserDTO dashboardUsuario(@AuthenticationPrincipal User userDetails) {
        return dashboardService.getDashboardUsuario(userDetails);
    }
}

