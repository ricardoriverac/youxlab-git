package secao10_Java.listas.atividade.aplicacao;

import secao10_Java.listas.atividade.metodos.metodos;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;


public class aplicação {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        List<metodos> list = new ArrayList<>();

        int n = sc.nextInt();
        int id = 0;
        for (int i = 0; i < n; i++) {
            id = sc.nextInt();
            while (hasId(list, id)) {
                System.out.print("ID em uso, tente outro: ");
                id = sc.nextInt();
            }
            String nome = sc.next();
            double salario = sc.nextDouble();
            list.add(new metodos(id, nome, salario));
        }
        id = sc.nextInt();
        int finalId = id;
        metodos metodos = list.stream().filter(x -> x.getId() == finalId).findFirst().orElse(null);
        if (metodos != null) {
                System.out.print("Adicione o aumento: ");
                double aumento = sc.nextDouble();
                metodos.aumentarSalario(aumento);
            } else {
                System.out.print("ID inválido.");
            }

        for(metodos x: list){
            System.out.print(x + " \n");

        }

    }

    public static boolean hasId(List<metodos> list, int id){
        metodos metodos = list.stream().filter(x -> x.getId() == id).findFirst().orElse(null);
        return metodos != null;
    }
}


