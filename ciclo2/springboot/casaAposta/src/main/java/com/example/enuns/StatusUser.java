package com.example.enuns;

public enum StatusUser {

        ATIVO("ativo"),
        BLOQUEADO("bloqueado"),
        PENDENTE("pendente");

        private final String status;

        StatusUser(String status) {
            this.status = status;
        }

        public String getStatus() {
            return status;
        }

        public static String[] getNomes() {
            StatusUser[] values = StatusUser.values();
            String[] nomes = new String[values.length];
            for (int i = 0; i < values.length; i++) {
                nomes[i] = values[i].name();
            }
            return nomes;
        }
    }

