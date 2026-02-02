package curso_completo_java.sessao_13.exercicios.exercicio03.application;

import curso_completo_java.sessao_13.exercicios.exercicio03.entities.Contribuinte;
import curso_completo_java.sessao_13.exercicios.exercicio03.entities.PessoaFisica;
import curso_completo_java.sessao_13.exercicios.exercicio03.entities.PessoaJuridica;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class program {

        public static void main(String[] args) {

            Locale.setDefault(Locale.US);
            Scanner sc = new Scanner(System.in);

            List<Contribuinte> lista = new ArrayList<>();

            System.out.print("Digite o número de contribuintes: ");
            int n = sc.nextInt();

            for (int i = 1; i <= n; i++) {
                System.out.println("Dados do contribuinte #" + i);
                System.out.print("Pessoa física ou jurídica (f/j)? ");
                char tipo = sc.next().charAt(0);

                System.out.print("Nome: ");
                sc.nextLine();
                String nome = sc.nextLine();

                System.out.print("Renda anual: ");
                double renda = sc.nextDouble();

                if (tipo == 'f') {
                    System.out.print("Gastos com saúde: ");
                    double saude = sc.nextDouble();
                    lista.add(new PessoaFisica(nome, renda, saude));
                } else {
                    System.out.print("Número de funcionários: ");
                    int funcionarios = sc.nextInt();
                    lista.add(new PessoaJuridica(nome, renda, funcionarios));
                }
            }

            System.out.println();
            System.out.println("Impostos pagos:");
            double total = 0.0;

            for (Contribuinte c : lista) {
                double imposto = c.imposto();
                System.out.printf("%s: R$ %.2f%n", c.getNome(), imposto);
                total += imposto;
            }

            System.out.println();
            System.out.printf("Total de impostos: R$ %.2f%n", total);

            sc.close();
        }
    }

