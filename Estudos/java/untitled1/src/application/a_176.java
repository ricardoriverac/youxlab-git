package application;

import application.entities.Contrato;
import application.entities.ContratoServico;
import application.entities.Parcelas;
import application.entities.PayPal;

import java.sql.SQLOutput;
import java.text.ParseException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;
import java.util.Scanner;

public class a_176 {
    public static void main(String[] args) throws ParseException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        System.out.print("Caro usuário, por favor insira o número de seu contrato: ");
        int numeroContrato = sc.nextInt();
        System.out.println("Caro usuário, por favor insira a data de seu contrato: ");
        LocalDate date = LocalDate.parse(sc.next(), fmt);
        System.out.print("Caro usuário, por favor insira o valor de seu contrato: ");
        Double valorContrato = sc.nextDouble();
        Contrato contrato = new Contrato(numeroContrato, date, valorContrato);

        System.out.print("Caro usuário, por favor insira o  número de parcelas do seu contrao: ");
        Integer quantidadeParcelas = sc.nextInt();

        ContratoServico paypal = new ContratoServico(new PayPal());

        paypal.processContrato(contrato, quantidadeParcelas);
        System.out.println("Parcelas: ");
        for(Parcelas parcelas : contrato.getParcelas()){
            System.out.println(parcelas);
        }
        sc.close();

    }
}
