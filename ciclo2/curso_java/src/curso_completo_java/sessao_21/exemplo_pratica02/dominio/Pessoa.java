package curso_completo_java.sessao_21.exemplo_pratica02.dominio;

import java.io.Serializable;

public class Pessoa implements Serializable {
        private static final long serialVersionUID = 1L;

        //@Id
        //@GeneratedValue(strategy=GenerationType.IDENTITY)
        private Integer id;

        //@Column(name="nomecompleto")
        private String nome;
        private String email;

        public Pessoa() {
        }
        public Pessoa (Integer id, String nome, String email) {
            super();
            this.id = id;
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

        public Integer getId() {
            return id;
        }

        public void setId(Integer id) {
            this.id = id;
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

