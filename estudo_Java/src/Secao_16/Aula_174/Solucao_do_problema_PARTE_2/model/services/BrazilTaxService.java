package Secao_16.Aula_174.Solucao_do_problema_PARTE_2.model.services;

public class BrazilTaxService {

    public double tax(double amount){
        if (amount <= 100.0) {
            return amount * 0.2;
        }
        else {
            return amount * 0.15;
        }
    }
}
