package curso_completo_java.sessao_16.pratica.exemplo_pratica04.services;



public class BrazilInterestService implements InterestService {

    private double interestRate;

    public BrazilInterestService(double interestRate) {
        this.interestRate = interestRate;
    }

    @Override
    public double getInterestRate() {
        return interestRate;
    }
}

