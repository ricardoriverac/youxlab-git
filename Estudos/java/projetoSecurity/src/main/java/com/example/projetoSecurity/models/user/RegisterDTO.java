package com.example.projetoSecurity.models.user;

import com.example.projetoSecurity.models.enums.UserRole;

public record RegisterDTO(String login, String password, UserRole role) {

}
