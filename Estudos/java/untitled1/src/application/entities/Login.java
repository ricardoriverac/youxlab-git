package application.entities;

import java.util.Date;
import java.util.Objects;

public class Login {
    private String nomeUsuario;
    private Date dataLogin;

    public Login(Date dataLogin, String nomeUsuario) {
        this.dataLogin = dataLogin;
        this.nomeUsuario = nomeUsuario;
    }

    public String getNomeUsuario() {
        return nomeUsuario;
    }

    public void setNomeUsuario(String nomeUsuario) {
        this.nomeUsuario = nomeUsuario;
    }

    public Date getDataLogin() {
        return dataLogin;
    }

    public void setDataLogin(Date dataLogin) {
        this.dataLogin = dataLogin;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Login login = (Login) o;
        return Objects.equals(nomeUsuario, login.nomeUsuario);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(nomeUsuario);
    }
}
