package application;

import application.entities.Funcionarios;
import application.entities.Funcionarios2;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class a_106 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);
        List<Funcionarios2> ListadeFuncionarios = new ArrayList<>();

        System.out.print("Caro usuário, por favor insira quantos funcionários serão cadastrados: ");
        int quantidadeFuncionarios = sc.nextInt();

        for (int i = 0; i < quantidadeFuncionarios; i++) {
            System.out.printf("\nCaro usuário, por favor insira o id do %do funcionário cadastrado: ", i+1);
            Integer idFuncionario = sc.nextInt();
            sc.nextLine();
            if (idExiste(ListadeFuncionarios, idFuncionario)){
                System.out.print("\nId ja existente. Usuário não cadastrado!");
                continue;
            }
            System.out.printf("\nCaro usuário, por favor insira agora o nome do %do funcionário cadastrado: ", i+1);
            String nomeFuncionario = sc.nextLine();
            System.out.printf("\nCaro usuário, por favor insira o salário do funcionário %s: ", nomeFuncionario);
            Double salario = sc.nextDouble();
            Funcionarios2 funcionario = new Funcionarios2(idFuncionario, nomeFuncionario, salario);
            ListadeFuncionarios.add(funcionario);
        }
        System.out.print("\nCaro usuário, por favor insira o id do funcionário que você deseja aumentar o salario: ");
        Integer idVerificado = sc.nextInt();
        Funcionarios2 funcionarioBusca  = ListadeFuncionarios.stream().filter(x -> x.getId().equals(idVerificado)).findFirst().orElse(null);
        if(funcionarioBusca == null){
            System.out.println("Caro usuário, este id não existe");
        }
        else{
            System.out.printf("\nCaro usuário, quantos %% de aumento você deseja atribuir ao salário do funcionário de id %d: ", idVerificado);
            Double porcentagem = sc.nextDouble();
            funcionarioBusca.AumentarSalario(porcentagem);
        }
        for(Funcionarios2 f : ListadeFuncionarios){
            System.out.println(f);
        }


    }
    public static  boolean idExiste(List<Funcionarios2> list, Integer id){
        return list.stream().anyMatch(f -> f.getId().equals(id));

    }
}
