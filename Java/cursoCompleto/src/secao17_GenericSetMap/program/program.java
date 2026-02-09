package secao17_GenericSetMap.program;

import java.text.ParseException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class program {
    public static void main(String[] args) throws ParseException {
            //Declarando o Scanner
            Scanner sc = new Scanner(System.in);
            //Setando os vetores de HashSet para cada curso, não permitindo códigos duplicados
            Set<Integer> a = new HashSet<>();
            Set<Integer> b = new HashSet<>();
            Set<Integer> c = new HashSet<>();
            /*Estrutura de repetição para cada estudante
            define quantos estudantes tem e seta um código para cada estudante
             */
            System.out.print("How many students for course A? ");
            int n = sc.nextInt();
            for (int i=0; i<n; i++) {
                int number = sc.nextInt();
                a.add(number);
            }

            System.out.print("How many students for course B? ");
            n = sc.nextInt();
            for (int i=0; i<n; i++) {
                int number = sc.nextInt();
                b.add(number);
            }

            System.out.print("How many students for course C? ");
            n = sc.nextInt();
            for (int i=0; i<n; i++) {
                int number = sc.nextInt();
                c.add(number);
            }
            //Declarando um novo Hashset "total" para o valor total, já adicionando o valor embutido em "a"
            Set<Integer> total = new HashSet<>(a);
            //Utilizando de métodos de HashSet para calcular o total de alunos
            total.addAll(b);
            total.addAll(c);
            //Printando o tamanho do hashset "total"
            System.out.println("Total students: " + total.size());

            sc.close();
    }
}
