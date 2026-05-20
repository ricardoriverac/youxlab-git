package Interfaces.ExercicioFixacao.model.services;

import Interfaces.ExercicioFixacao.model.entities.Contract;
import Interfaces.ExercicioFixacao.model.entities.Installment;

import java.time.LocalDate;

public class ContractService {

    private OnlinePaymentService onlinePaymentService;

    public ContractService(OnlinePaymentService onlinePaymentService) {
        this.onlinePaymentService = onlinePaymentService;
    }

    public void processContract(Contract contract, int months){
        double monthsContract = contract.getTotalValue() / months;
        for (int i = 1; i < months+1; i++) {
            LocalDate dueDate = contract.getDate().plusMonths(i);
            double interest = onlinePaymentService.interest(monthsContract, i);
            double paymentFee = onlinePaymentService.paymentFee(monthsContract + interest);
            double quantia = monthsContract + paymentFee + interest;
            contract.getInstallments().add(new Installment(dueDate, quantia));

        }
    }
}
