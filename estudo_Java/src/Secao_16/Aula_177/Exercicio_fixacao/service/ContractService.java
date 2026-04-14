package Secao_16.Aula_177.Exercicio_fixacao.service;

import Secao_16.Aula_177.Exercicio_fixacao.entities.Contract;
import Secao_16.Aula_177.Exercicio_fixacao.entities.Installment;
import Secao_16.Aula_177.Exercicio_fixacao.interfece.OnlinePaymentService;

public class ContractService {

    private OnlinePaymentService ops;

    public ContractService(OnlinePaymentService ops) {
        this.ops = ops;
    }

    public OnlinePaymentService getOps() {
        return ops;
    }

    public void setOps(OnlinePaymentService ops) {
        this.ops = ops;
    }

    public void processContract(Contract contract, Integer months) {
        Double baseInstallmentValue = (contract.getTotalValue()/months);
        for (int i = 0; i < months; i ++) {
            double amount =  baseInstallmentValue + ops.interest(baseInstallmentValue, i + 1);
            amount += ops.paymentFee(amount);



            contract.getInstallmentList().add(new Installment(contract.getDate().plusMonths(i + 1), amount));
        }
    }
}