package Secao12.aula133;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Date;

public class Cliente {
    public String name;
    public String email;
    public LocalDate birthDate;

    public Cliente(String name, String email, LocalDate birthDate) {
        this.name = name;
        this.email = email;
        this.birthDate = birthDate;
    }
    public String toString() {
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        return  name + " (" + birthDate.format(fmt) + ") - " + email;
    }
}
