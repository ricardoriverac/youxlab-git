package com.example.model;

import com.example.enuns.StatusJogo;
import com.example.enuns.TipoCelula;
import jakarta.persistence.*;

import java.math.BigDecimal;

import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.Random;

@Entity
@Table(name = "jogo")
public class Jogo {

        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Long id;

        @ManyToOne
        @JoinColumn(name = "user_id", nullable = false)
        private User user;

        @Column(name = "valor_aposta", nullable = false)
        private BigDecimal valorAposta;

        @Column(name = "valor_acumulado")
        private BigDecimal valorAcumulado;

        @Column(name = "valor_ganho")
        private BigDecimal valorGanho;

        @Enumerated(EnumType.STRING)
        @Column(nullable = false)
        private StatusJogo status;

        @Column(name = "diamantes_encontrados")
        private Integer diamantesEncontrados = 0;

        @Column(name = "jogadas_realizadas")
        private Integer jogadasRealizadas = 0;

        @Column(name = "data_inicio")
        private LocalDateTime dataInicio;

        @Column(name = "data_fim")
        private LocalDateTime dataFim;


        @Column(name = "tabuleiro", length = 50)
        private String tabuleiro;

        @Column(name = "revelados", length = 100)
        private String revelados;

        public Jogo() {}

        public Jogo(User user, BigDecimal valorAposta) {
            this.user = user;
            this.valorAposta = valorAposta;
            this.valorAcumulado = valorAposta;
            this.status = StatusJogo.EM_ANDAMENTO;
            this.diamantesEncontrados = 0;
            this.jogadasRealizadas = 0;
            this.dataInicio = LocalDateTime.now();
            this.tabuleiro = gerarTabuleiro();
            this.revelados = "";
        }

        private String gerarTabuleiro() {
            String[] celulas = new String[25];
            Arrays.fill(celulas, "B");

            Random random = new Random();
            int diamantesColocados = 0;
            while (diamantesColocados < 10) {
                int pos = random.nextInt(25);
                if (celulas[pos].equals("B")) {
                    celulas[pos] = "D";
                    diamantesColocados++;
                }
            }

            return String.join(",", celulas);
        }

        public TipoCelula processarJogada(int linha, int coluna) {
            String posicao = linha + "," + coluna;
            if (revelados.contains(posicao)) {
                return TipoCelula.JA_REVELADO;
            }

            int indice = (linha * 5) + coluna;

            String[] celulas = tabuleiro.split(",");
            String tipo = celulas[indice];

            if (revelados.isEmpty()) {
                revelados = posicao;
            } else {
                revelados = revelados + ";" + posicao;
            }

            jogadasRealizadas++;

            if (tipo.equals("D")) {
                diamantesEncontrados++;
                double multiplicador = 1 + (diamantesEncontrados * 0.33);
                valorAcumulado = valorAposta.multiply(BigDecimal.valueOf(multiplicador));

                if (diamantesEncontrados >= 10) {
                    status = StatusJogo.GANHOU;
                    valorGanho = valorAcumulado;
                    dataFim = LocalDateTime.now();
                    return TipoCelula.DIAMANTE_VITORIA;
                }

                return TipoCelula.DIAMANTE;
            }
            else {
                status = StatusJogo.PERDEU;
                valorGanho = BigDecimal.ZERO;
                valorAcumulado = BigDecimal.ZERO;
                dataFim = LocalDateTime.now();
                return TipoCelula.BOMBA;
            }
        }

        public void encerrar() {
            this.status = StatusJogo.ENCERRADO;
            this.valorGanho = this.valorAcumulado;
            this.dataFim = LocalDateTime.now();
        }

    public String[][] getTabuleiroVisivel() {
        String[][] visivel = new String[5][5];
        String[] celulas = tabuleiro.split(",");
        String[] reveladosArray = revelados.split(";");

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                visivel[i][j] = "?";
            }
        }

        for (String pos : reveladosArray) {
            if (!pos.isEmpty()) {
                String[] coord = pos.split(",");
                int l = Integer.parseInt(coord[0]);
                int c = Integer.parseInt(coord[1]);
                int indice = (l * 5) + c;

                if (celulas[indice].equals("D")) {
                    visivel[l][c] = "D";
                } else {
                    visivel[l][c] = "X";
                }
            }
        }

        return visivel;
    }


        public Long getId() {
            return id;
        }

        public void setId(Long id) {
            this.id = id;
        }

        public User getUser() {
            return user;
        }

        public void setUser(User user) {
            this.user = user;
        }

        public BigDecimal getValorAposta() {
            return valorAposta;
        }


        public BigDecimal getValorAcumulado() {
            return valorAcumulado;
        }


        public BigDecimal getValorGanho() {
            return valorGanho;
        }


        public StatusJogo getStatus() {
            return status;
        }

        public void setStatus(StatusJogo status) {
            this.status = status;
        }

        public Integer getDiamantesEncontrados() {
            return diamantesEncontrados;
        }


        public Integer getJogadasRealizadas() {
            return jogadasRealizadas;
        }


        public LocalDateTime getDataInicio() {
            return dataInicio;
        }

    }

