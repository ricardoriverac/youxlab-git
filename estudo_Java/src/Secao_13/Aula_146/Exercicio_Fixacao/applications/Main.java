package Secao_13.Aula_146.Exercicio_Fixacao.applications;

import Secao_13.Aula_146.Exercicio_Fixacao.entities.Pessoa;
import Secao_13.Aula_146.Exercicio_Fixacao.entities.PessoaFisica;
import Secao_13.Aula_146.Exercicio_Fixacao.entities.PessoaJuridica;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);


        List<Pessoa> pessoaList = new ArrayList<>();

        System.out.print("Enter the number of tax payers: ");
        int quantidadeRegistro = sc.nextInt();

        for (int i = 0; i < quantidadeRegistro; i++) {
            System.out.printf("Tax payer #%d data:%n", (i + 1));

            System.out.print("Individual or company (i/c)? ");
            char ch = sc.next().charAt(0);

            System.out.print("Name: ");
            String name = sc.next();

            System.out.print("Anual income: ");
            double rendaAnual = sc.nextDouble();

            if (ch == 'i') {
                System.out.print("Health expenditures: ");
                double gastoSaude = sc.nextDouble();

                pessoaList.add(new PessoaFisica(rendaAnual, name, gastoSaude));
            }
            else if (ch == 'c') {
                System.out.print("Number of employees: ");
                int numeroFuncionario = sc.nextInt();

                pessoaList.add(new PessoaJuridica(rendaAnual, name, numeroFuncionario));
            }
        }
        double sum = 0;
        System.out.println("\n TAXES PAID");
        for (Pessoa p : pessoaList) {
            sum += p.getCalculoImposto();
            p.exibirDados();

        }

        System.out.println("\nTOTAL TAXES: $" + sum);
    }
}
