package application.entities;

public class Quarto {
        private String nome;
        private String email;

        public Quarto(String nome, String email){
            this.nome = nome;
            this.email = email;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public String getNome() {
            return nome;
        }

        public void setNome(String nome) {
            this.nome = nome;
        }

    public String toString() {
        return nome + ", " + email;
    }

}

