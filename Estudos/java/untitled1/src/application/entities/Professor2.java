package application.entities;

import java.util.ArrayList;
import java.util.List;

public class Professor2 {
    String nomeProfessor;
    List<Curso> cursos = new ArrayList<>();

    public Professor2(String nomeProfessor, List<Curso> cursos) {
        this.nomeProfessor = nomeProfessor;
        this.cursos = cursos;
    }

    public String getNomeProfessor() {
        return nomeProfessor;
    }

    public void setNomeProfessor(String nomeProfessor) {
        this.nomeProfessor = nomeProfessor;
    }

    public List<Curso> getCursos() {
        return cursos;
    }

    public void setCursos(List<Curso> cursos) {
        this.cursos = cursos;
    }
}
