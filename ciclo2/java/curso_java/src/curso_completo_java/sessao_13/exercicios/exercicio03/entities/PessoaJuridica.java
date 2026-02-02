package curso_completo_java.sessao_13.exercicios.exercicio03.entities;

public class PessoaJuridica extends Contribuinte {

        private Integer numeroFuncionarios;

        public PessoaJuridica(String nome, Double rendaAnual, Integer numeroFuncionarios) {
            super(nome, rendaAnual);
            this.numeroFuncionarios = numeroFuncionarios;
        }

        @Override
        public Double imposto() {
            if (numeroFuncionarios > 10) {
                return getRendaAnual() * 0.14;
            } else {
                return getRendaAnual() * 0.16;
            }
        }
    }

