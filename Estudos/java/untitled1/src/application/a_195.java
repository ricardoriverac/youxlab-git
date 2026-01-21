package application;
import java.util.*;

public class a_195 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> cursos = Arrays.asList("Curso Java completo", "Banco de dados e PostgreSQL", "Curso JavaScript");
        Set<Integer> alunosProfessor = new HashSet<>();
        int i = cursos.size();
        for (int j = 0; j < i; j++) {
            System.out.println("Caro usuário, quantos alunos tem no curso " + cursos.get(j));
            int quantidadeAlunos = sc.nextInt();
            for (int k = 0; k < quantidadeAlunos; k++) {
                System.out.printf("Caro usuário, qual o id do %do(a) aluno(a?)", k + 1);
                Integer idAluno = sc.nextInt();
                alunosProfessor.add(idAluno);
            }
        }
        int soma = 0;
        for(Integer aluno : alunosProfessor){
            soma+=1;
        }
        System.out.print("Total de alunos: " + soma);
    }
}
