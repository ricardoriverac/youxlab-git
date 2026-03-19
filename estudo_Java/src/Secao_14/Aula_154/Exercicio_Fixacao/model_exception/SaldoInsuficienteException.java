package Secao_14.Aula_154.Exercicio_Fixacao.model_exception;

public class SaldoInsuficienteException extends Exception{
    private static final long serialVersionUID = 1L;

    public SaldoInsuficienteException(String msg) {
        super(msg);
    }


}
