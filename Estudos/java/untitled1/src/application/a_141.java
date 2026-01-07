package application;

import application.entities.Funcionarios3;
import application.entities.FuncionariosTerceirizados;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class a_141 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        List<Funcionarios3> funcionarios = new ArrayList<>();

        System.out.print("Caro usuário, quantos funcionários serão cadastrados? ");
        int quantidadeFuncionarios = sc.nextInt();

        for (int i = 0; i < quantidadeFuncionarios; i++) {
            System.out.print("Caro usuário, este funcionário é terceirizado? [S/N]");
            char verificacaoTerceirizado = sc.next().charAt(0);
            System.out.print("Caro usuário, qual o nome do funcionário? ");
            String nomeFuncionario = sc.next();
            System.out.print("Caro usuário, qual a carga horária do funcionário? ");
            Integer cargaHoria = sc.nextInt();
            System.out.print("Caro usuário, qual o valor da hora deste funcionário? ");
            Double valorHora = sc.nextDouble();
            if (verificacaoTerceirizado == 'S'){
                System.out.print("Caro usuário, qual o salário extra deste funcionário? ");
                Double salarioAdicional = sc.nextDouble();
                funcionarios.add(new FuncionariosTerceirizados(nomeFuncionario, cargaHoria, valorHora, salarioAdicional));
            }
            else{
                funcionarios.add(new Funcionarios3(nomeFuncionario, cargaHoria, valorHora));
            }
        }
        System.out.print("PAGAMENTOS - ");
        for (Funcionarios3 f : funcionarios){
            System.out.print(f.getNomeFuncionario() + " $ - " + f.pagamento() + "\n");
        }
    }
}
