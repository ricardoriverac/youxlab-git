package application;


import application.entities.ServicoJuros;
import application.entities.ServicoJurosBrasileiro;

import java.util.Locale;
import java.util.Scanner;

public class a_183 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Caro usuário, por favor insira qual o valor de sua fatura: ");
        Double quantia = sc.nextDouble();
        System.out.println("Caro usuário, por favor insira quantas parcelas será: ");
        Integer quantidadeParcelas = sc.nextInt();

        ServicoJuros is = new ServicoJurosBrasileiro(2.0);
        Double pagamento = is.pagamento(quantia, quantidadeParcelas);

        System.out.println("Pagamento depois: " + quantidadeParcelas + " meses" );
        System.out.println(pagamento);

        sc.close();
    }
}
