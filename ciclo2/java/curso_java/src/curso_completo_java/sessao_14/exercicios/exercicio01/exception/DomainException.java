package curso_completo_java.sessao_14.exercicios.exercicio01.exception;

    public class DomainException extends RuntimeException {

        private static final long serialVersionUID = 1L;

        public DomainException(String msg) {
            super(msg);
        }
    }

