package application.entities;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Aluno {
    private String nomeAluno;
    private Integer ID;
    List<Curso> cursos = new ArrayList<>();


    public Aluno(String nomeAluno, Integer ID, List<Curso> cursos) {
        this.nomeAluno = nomeAluno;
        this.ID = ID;
        this.cursos = cursos;
    }

    public List<Curso> getCursos() {
        return cursos;
    }

    public void setCursos(List<Curso> cursos) {
        this.cursos = cursos;
    }

    public String getNomeAluno() {
        return nomeAluno;
    }

    public void setNomeAluno(String nomeAluno) {
        this.nomeAluno = nomeAluno;
    }

    public Integer getID() {
        return ID;
    }

    public void setID(Integer ID) {
        this.ID = ID;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Aluno aluno = (Aluno) o;
        return Objects.equals(ID, aluno.ID);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(ID);
    }
}
