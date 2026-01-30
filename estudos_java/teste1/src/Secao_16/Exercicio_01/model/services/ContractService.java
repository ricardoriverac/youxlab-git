package Secao_16.Exercicio_01.model.services;

import Secao_16.Exercicio_01.model.entities.Contract;
import Secao_16.Exercicio_01.model.entities.Installment;

import java.time.LocalDate;

public class ContractService {

    private OnlinePaymentService onlinePaymentService;

    public ContractService(OnlinePaymentService onlinePaymentService) {
        this.onlinePaymentService = onlinePaymentService;
    }

    public void processContract(Contract contract, int months) {
        double month = contract.getTotalValue()/months;
        for (int i=1 ; i<months+1 ; i++) {
            LocalDate dueDate = contract.getDate().plusMonths(i);
            double interest = onlinePaymentService.interest(month,i);
            double paymentFee = onlinePaymentService.paymentFee(month + interest);
            double total = month + interest + paymentFee;
            contract.getInstallments().add(new Installment(dueDate, total));
        }
    }
}
