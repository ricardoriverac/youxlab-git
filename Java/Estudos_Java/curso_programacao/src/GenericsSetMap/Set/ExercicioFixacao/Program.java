package GenericsSetMap.Set.ExercicioFixacao;

import java.util.*;

public class Program {

    static void main() {

        Scanner sc = new Scanner(System.in);

        Set<Integer> alunos = new HashSet<>();
        List<String> cursos = Arrays.asList("A", "B", "C");

        int totalAlunos = 0;
        for (String s : cursos){
            System.out.print("How many students for course " + s + ": ");
            int qntAlunos = sc.nextInt();
            for (int i = 0; i < qntAlunos; i++) {
                int idAluno = sc.nextInt();
                alunos.add(idAluno);
                totalAlunos = alunos.size();
            }

        }
        System.out.println("Total alunos: " + totalAlunos);

        sc.close();
    }
}
