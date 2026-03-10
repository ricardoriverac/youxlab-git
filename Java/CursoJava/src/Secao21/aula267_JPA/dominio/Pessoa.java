package Secao21.aula267_JPA.dominio;

import java.io.Serializable;

public class Pessoa implements Serializable {
    private static final long serialVersionUID = 1L;
    private Integer id;
    private String nome;
    private String email;

    public Pessoa(){
    }
    public Pessoa(Integer id, String nome, String email){
        super();
        this.id = id;
        this.nome = nome;
        this.email = email;
    }
    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getEmaail() {
        return email;
    }
    public void setEmaail(String emaail) {
        this.email = emaail;
    }

    @Override
    public String toString() {
        return "Pessoa{" +
                "id=" + id +
                ", nome='" + nome + '\'' +
                ", email='" + email + '\'' +
                '}';
    }
}
