package com.example.CasadeAposta.service;

import com.example.CasadeAposta.dtos.DashbAdminDTO;
import com.example.CasadeAposta.dtos.DashbUserDTO;
import com.example.CasadeAposta.model.User;
import com.example.CasadeAposta.model.enums.ApostaStatus;
import com.example.CasadeAposta.repositories.ApostaRepository;
import lombok.RequiredArgsConstructor;

import java.math.BigDecimal;
import java.util.Optional;

@RequiredArgsConstructor
public class DashboardService {
    private final AuthService authService;
    private final ApostaRepository apostaRepository;

    public DashbUserDTO getDashboardUsuario(User userDetails) {

        User user = authService.buscarPorEmail(userDetails.getUsername());

        long total = apostaRepository.countByUsuario(user);
        long ganhos = apostaRepository.countByUsuarioAndStatus(user, ApostaStatus.FINALIZADA);
        long perdidos = total - ganhos;

        return new DashbUserDTO(total, ganhos, perdidos);
    }

    public DashbAdminDTO getDashboardAdmin() {

        long totalJogos = apostaRepository.count();

        BigDecimal totalGanhos = Optional.ofNullable(
                apostaRepository.totalGanhos()
        ).orElse(BigDecimal.ZERO);

        return new DashbAdminDTO(totalJogos, totalGanhos);
    }
}