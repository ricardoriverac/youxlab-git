package application.entities;

public class Curso {
    private String nomeCurso;
//    private Professor2 professor;


    public Curso() {
    }

    public Curso(String nomeCurso) {
        this.nomeCurso = nomeCurso;
//        this.professor = professor;
    }

    public String getNomeCurso() {
        return nomeCurso;
    }

    public void setNomeCurso(String nomeCurso) {
        this.nomeCurso = nomeCurso;
    }

//    public Professor2 getProfessor() {
//        return professor;
//    }
//
//    public void setProfessor(Professor2 professor) {
//        this.professor = professor;
//    }
}
