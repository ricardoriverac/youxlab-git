package Secao_12.Aula_129.Exercicio_Parte_1;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        //Objetos
        Scanner sc = new Scanner(System.in);
        Contrato obj = new Contrato(0, 0, LocalDate.of(1928, 4, 20));

        //Formatação de data
        DateTimeFormatter fmt1 = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        //Inserção de dados
        System.out.print("Digite o nome do departamento: ");
        String nomeDepartamento = sc.next();

        System.out.println("insira os dados do funcioniario: ");

        System.out.print("Nome: ");
        String nome = sc.next();
        sc.next();


        System.out.print("Nível: ");
        sc.next();

        System.out.print("Salário base: ");
        double salarioBase = sc.nextDouble();

        System.out.print("Quantos contrartos esse funcionário possui? ");
        int quantidadeContrato = sc.nextInt();

        //Declaração do vetor
        Contrato[] vect = new Contrato[quantidadeContrato];

        //Inserção dos dados do contrato
        for (int i=0; i < vect.length; i++) {

            System.out.printf("insira os dados do contrarto n°%d %n", i);

            System.out.print("Data (DD/MM/AAAA): ");
            LocalDate d01 = LocalDate.parse(sc.next(), fmt1);

            System.out.print("Valor por hora: ");
            double valorHora = sc.nextDouble();

            System.out.print("Duração(Horas): ");
            int duracaoHoras = sc.nextInt();

            vect[i] = new Contrato(duracaoHoras, valorHora, d01);

        }

        System.out.print("insira o mês e o ano para calcular a renda(MM/AAAA): ");
        String[] split = sc.next().split("/");

        int split0 = Integer.parseInt(split[0]);
        int split1 = Integer.parseInt(split[1]);

        double valorTotal;
        double sum = 0;

        for (int i = 0; i < vect.length; i++ ){
            if (vect[i].getData().getYear() == split1 && vect[i].getData().getMonthValue() == split0) {
                valorTotal = vect[i].getDucaoHoras() * vect[i].getValorHoras();
                sum += valorTotal;

            }
        }

        salarioBase += sum;


        System.out.printf("Nome: %s", nome);
        System.out.printf("%nDepartamento: %s%n", nomeDepartamento);
        System.out.println(salarioBase);

    }
}
