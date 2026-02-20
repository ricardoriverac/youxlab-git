package Aula_105.Listas.Exercicio_Fixacao;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        List<Dados> list = new ArrayList<>();

        int c = 0;
        int id;
        String nome;
        double credito;

        System.out.print("Quantos funcionários serão registrados? ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            c++;
            System.out.printf("%nFuncionário  nº %d%n", c);

            System.out.print("Id: ");
            id = sc.nextInt();

            System.out.print("Nome: ");
            sc.nextLine();
            nome = sc.nextLine();


            System.out.print("Salário: ");
            credito = sc.nextDouble();

            list.add(new Dados(id, nome, credito));
        }

        boolean jaAcomteceu = false;
        System.out.print("Digite o ID do funcionário que terá aumento salarial: ");
        int aumentoSalario = sc.nextInt();

        for (int i = 0; i < list.size(); i++) {
            Dados dados = list.get(i);
            if (dados.getId() == aumentoSalario) {
                System.out.print("Digite a porcentagem: ");
                double porcentagem = sc.nextDouble();
                double novoSalario = (dados.getCredito() * (1 + porcentagem / 100));
                dados.setCredito(novoSalario);
                System.out.println("Aumento realizado");
            } else {
                if (jaAcomteceu == false) {
                    jaAcomteceu = true;
                    System.out.println("Algo deu errado");
                }
            }
        }

        for (int i = 0; i < list.size(); i++) {
            Dados dado = list.get(i);
            System.out.println(dado.getId() + ", " + dado.getNome() + ", " + dado.getCredito());
        }
    }
}

                                                            