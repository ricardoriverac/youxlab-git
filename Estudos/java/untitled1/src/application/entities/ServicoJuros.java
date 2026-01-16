package application.entities;

import java.security.InvalidParameterException;

public interface ServicoJuros {
    double getTaxajuros();

    default Double pagamento(Double quantia, Integer parcelas){
        if(parcelas < 1){
            throw  new InvalidParameterException("Não é permitido faturas sem parcelas");
        }
        return  quantia * Math.pow(1.0 + getTaxajuros() / 100.0, parcelas);
    }

}
