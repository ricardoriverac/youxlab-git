package secao_10.Aula_96.Exerciciofixa.DesafioVetores.EntidadeVET;

public class Estudante {

    private String estu;
    private String email;
    private int codeRooms;


    public int getRooms() {
        return codeRooms;
    }

    public void setRooms(int rooms) {
        this.codeRooms = rooms;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getEstudante() {
        return estu;
    }

    public void setEstudante(String estudante) {
        this.estu = estudante;
    }

    public String toString() {
        return getRooms()
                + ": "
                + getEstudante()
                + ", "
                + getEmail();
    }
}

