package com.example.enuns;

public enum PerfilUser {

        ADMIN("admin", "Administrador da plataforma"),
        USER("user", "Usuário comum");

        private final String tipo;
        private final String descricao;

            PerfilUser(String tipo, String descricao) {
            this.tipo = tipo;
            this.descricao = descricao;
        }

        public String getTipo() {
            return tipo;
        }

        public String getDescricao() {
            return descricao;
        }

        public boolean isAdmin() {
            return this == ADMIN;
        }

        public boolean isUser() {
            return this == USER;
        }

        public static String[] getNomes() {
            PerfilUser[] values = PerfilUser.values();
            String[] nomes = new String[values.length];
            for (int i = 0; i < values.length; i++) {
                nomes[i] = values[i].name();
            }
            return nomes;
        }
    }

