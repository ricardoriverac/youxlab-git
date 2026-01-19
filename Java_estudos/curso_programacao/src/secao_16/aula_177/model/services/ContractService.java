package secao_16.aula_177.model.services;

import secao_16.aula_177.model.entities.Contract;
import secao_16.aula_177.model.entities.Installment;

import java.time.LocalDate;

public class ContractService  {

        private OnlinePaymentService onlinePaymentService;

        public ContractService(OnlinePaymentService onlinePaymentService) {
            this.onlinePaymentService = onlinePaymentService;
        }

        public void processContract(Contract contract, int months) {
            double basic = contract.getTotalValue() / months;
            for (int i = 1; i <= months; i++) {
                LocalDate dueDate = contract.getDate().plusMonths(i);
                double interest = onlinePaymentService.interest(basic, i);
                double fee = onlinePaymentService.paymentFee(basic + interest);
                double quantia = basic + interest + fee;
                contract.getInstallments().add(new Installment(dueDate, quantia));
            }
        }
}
