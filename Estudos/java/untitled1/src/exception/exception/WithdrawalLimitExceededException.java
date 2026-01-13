package exception.exception;

public class WithdrawalLimitExceededException extends RuntimeException{
    private static final long serialVersionUID = 1L;

    public WithdrawalLimitExceededException(String msg){
        super(msg);
    }
}
