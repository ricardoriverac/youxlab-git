package Vetores.Desafio.entities;

public class BoardingHouse {
    private String estudante;
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
        return estudante;
    }

    public void setEstudante(String estudante) {
        this.estudante = estudante;
    }

    public String toString() {
        return getRooms()
              + ": "
              + getEstudante()
              + ", "
              + getEmail();
    }
}
