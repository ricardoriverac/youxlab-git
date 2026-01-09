package secao_12.exerciciofixacao132.model.entities;

import java.util.Date;

public class Client {
    private String name;
    private String email;
    private Date birthDate;



    public Client(){

    }


    public Client(String email, String name, Date birthDate) {
        this.email = email;
        this.name = name;
        this.birthDate = birthDate;
    }


    public String getEmail() {
        return email;
    }


    public void setEmail(String email) {
        this.email = email;
    }


    public String getName() {
        return name;
    }


    public void setName(String name) {
        this.name = name;
    }


    public Date getBirthDate() {
        return birthDate;
    }


    public void setBirthDate(Date birthDate) {
        this.birthDate = birthDate;
    }
}
