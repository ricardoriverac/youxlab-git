package application;

import application.entities.ContratoHora;
import application.entities.Departamento;
import application.entities.NivelExperiencia;
import application.entities.Trabalhador;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class a_129_ex1 {
    public static void main(String[] args) throws ParseException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat data = new SimpleDateFormat("dd/MM/yyyy");

        System.out.print("Caro usuário, qual o departamento do funcionário? ");
        String departamento = sc.nextLine();
        Departamento departamentoFuncionario = new Departamento(departamento);

        System.out.print("Caro usuário, qual o nome do funcionário? ");
        String nomeFuncionario = sc.nextLine();
        System.out.print("Caro usuário, qual o nivel de experiência do funcionário? ");
        String experiencia = sc.nextLine();
        NivelExperiencia experienciaFuncionario = NivelExperiencia.valueOf(experiencia);
        System.out.print("Caro usuário, qual o salário base do funcionário? ");
        Double salarioBase = sc.nextDouble();
        Trabalhador funcionario = new Trabalhador(nomeFuncionario, experienciaFuncionario, salarioBase);
        System.out.printf("Caro usuário, quantos contratos o funcionário %s tem?", nomeFuncionario);
        Integer quantidadeContratos = sc.nextInt();
        for (int i = 0; i < quantidadeContratos; i++) {
            System.out.print("Caro usuário, qual a data do contrato deste funcionário? ");
            Date dataContrato = data.parse(sc.next());
            System.out.print("Caro usuário, qual o valor da hora desse funcionário? ");
            Double valorHora = sc.nextDouble();
            System.out.print("Caro usuário, qual a carga horária desse funcionário? ");
            Integer cargaHoraria = sc.nextInt();
            ContratoHora contratoFuncionario = new ContratoHora(dataContrato, valorHora, cargaHoraria);
            funcionario.addContract(contratoFuncionario);
        }
        System.out.print("Caro usuário, por favor insira o mês e ano que você deseja calcular a renda (MM/YYYY): ");
        String dataRenda = sc.next();
        int mes = Integer.parseInt(dataRenda.substring(0, 2));
        int ano = Integer.parseInt(dataRenda.substring(3));
        System.out.printf("Nome: %s", nomeFuncionario);
        System.out.printf("\nDepartamento %s", departamento);
        System.out.print("\nRenda:" + funcionario.renda(ano, mes));
        sc.close();
    }
}
