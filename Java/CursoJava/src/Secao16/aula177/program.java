package Secao16.aula177;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        DateTimeFormatter fmtData = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        System.out.println("Entre os dados do contrato:");
        System.out.print("Numero: ");
        Integer numero = sc.nextInt();
        sc.nextLine(); // Limpa buffer
        System.out.print("Data (dd/MM/yyyy): ");
        LocalDate data = LocalDate.parse(sc.nextLine(), fmtData);
        System.out.print("Valor do contrato: ");
        Double valorTotal = sc.nextDouble();
        System.out.print("Entre com o numero de parcelas: ");
        int numeroParcelas = sc.nextInt();

        Contrato contrato = new Contrato(numero, data, valorTotal);

        ServicoContrato servico = new ServicoContrato();
        List<Parcela> parcelas = servico.gerarParcelas(contrato, numeroParcelas);

        System.out.println("\nParcelas:");
        for (Parcela p : parcelas) {
            System.out.printf("%s - %.2f%n", p.getDataVencimento().format(fmtData), p.getValor());
        }

        sc.close();
    }
}
