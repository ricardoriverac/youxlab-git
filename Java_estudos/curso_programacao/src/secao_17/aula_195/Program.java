package secao_17.aula_195;

import java.util.*;

public class Program {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Set<Integer> todosAlunos = new HashSet<>();
        List<String> nameCourses = Arrays.asList("Curso Java", "Banco de dados e PostgreSQL", "Curso JavaScript");
        int idAluno;

        for (String curso : nameCourses){
            System.out.println("How many students for course " + curso +  " ?");
            int alunos = sc.nextInt();
            for (int i = 0; i < alunos; i++) {
                 idAluno = sc.nextInt();
                 todosAlunos.add(idAluno);
            }

        }
        System.out.println("Total students: " + todosAlunos.size());


    }
}
