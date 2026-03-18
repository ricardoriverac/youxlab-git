package com.example.enuns;

public enum StatusJogo {

        EM_ANDAMENTO("em_andamento", "Jogo em andamento", "🔄"),
        GANHOU("ganhou", "Jogador ganhou (achou todos diamantes)", "🎉"),
        PERDEU("perdeu", "Jogador perdeu (achou bomba)", "💥"),
        ENCERRADO("encerrado", "Jogador encerrou manualmente", "🛑");

        private final String status;
        private final String descricao;
        private final String icone;

        StatusJogo(String status, String descricao, String icone) {
            this.status = status;
            this.descricao = descricao;
            this.icone = icone;
        }

        public String getStatus() {
            return status;
        }



    }

