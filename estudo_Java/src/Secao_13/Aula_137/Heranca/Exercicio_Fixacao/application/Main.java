package Secao_13.Aula_137.Heranca.Exercicio_Fixacao.application;

import Secao_13.Aula_137.Heranca.Exercicio_Fixacao.entities.Desenvolvedor;
import Secao_13.Aula_137.Heranca.Exercicio_Fixacao.entities.Funcionario;
import Secao_13.Aula_137.Heranca.Exercicio_Fixacao.entities.Gerente;

public class Main {
    public static void main(String[] args) {

        Funcionario f1 = new Funcionario("Calor", 5000.00);
        Funcionario f2 = new Gerente("Luiz", 3000.00);
        Funcionario f3 = new Desenvolvedor("João Marcelo", 1000.00);

        System.out.println("\n" + f1.exibirDados());
        System.out.println("\n" + f2.exibirDados());
        System.out.println("\n" + f3.exibirDados());
    }
}
