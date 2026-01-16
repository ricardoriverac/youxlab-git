package curso_completo_java.sessao_14.exercicios.exercicio02.exception;

    public class BusinessException extends RuntimeException {


        private static final long serialVersionUID = 1L;

        public BusinessException(String msg) {
            super(msg);
        }
    }

