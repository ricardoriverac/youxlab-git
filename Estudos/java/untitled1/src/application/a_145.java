package application;

import application.entities.Contribuinte;
import application.entities.PessoaFisica;
import application.entities.PessoaJuridica;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class a_145 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Contribuinte> contribuintes = new ArrayList<>();

        System.out.print("Caro usuário, por favor insira quantos contribuintes serão cadastrados: ");
        int quantidadeContribuintes = sc.nextInt();

        for (int i = 0; i < quantidadeContribuintes; i++) {
            System.out.print("Caro usuário, este contribuinte é Físico ou Júridico? ");
            char tipoContribuinte = sc.next().charAt(0);
            System.out.print("Caro usuário, qual o nome do contribuinte? ");
            String nomeContribuinte = sc.next();
            System.out.print("Caro usuário, qual a renda anual do contribuinte? ");
            Double rendaAnual = sc.nextDouble();
            if(tipoContribuinte == 'F' || tipoContribuinte == 'f'){
                System.out.print("Caro usuário, qual foi o gasto anual com saúde deste contribuinte? ");
                Double gastoSaude = sc.nextDouble();
                contribuintes.add(new PessoaFisica(nomeContribuinte, rendaAnual, gastoSaude));
            }
            else{
                System.out.print("Caro usuário, quantos funcionários tem esta companhia?");
                Integer quantidadeFuncionarios = sc.nextInt();
                contribuintes.add(new PessoaJuridica(nomeContribuinte, rendaAnual, quantidadeFuncionarios));
            }
        }
        System.out.print("Taxas de imposto: \n");
        for(Contribuinte c : contribuintes){
            System.out.print(c);
        }

        System.out.print("Total de taxas: ");
        Double soma = 0.0;
        for(Contribuinte c : contribuintes){
            soma += c.taxa();
        }
        System.out.printf("%.2f", soma);
    }
}
