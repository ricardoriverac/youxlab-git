package Secao_13.Aula_144.Classes_Abstratas.application;

import Secao_13.Aula_144.Classes_Abstratas.entities.Desenvolvedor;
import Secao_13.Aula_144.Classes_Abstratas.entities.Funcionario;
import Secao_13.Aula_144.Classes_Abstratas.entities.Gerente;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Main {
    public static void main(String[] args) {

        List<Funcionario> funcionarioList = new ArrayList<>();

        funcionarioList.add(new Gerente("Otto", 1500.00, 500.00));
        funcionarioList.add(new Desenvolvedor("Raicony", 1200.00, 8, 30.00));

        for (Funcionario f : funcionarioList) {
            f.exibirDados();
        }


    }
}
