package TesteLoja.AtividadeIdenpendente.components.entities;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Entity
@Table(name = "tb_user")
@Data
@NoArgsConstructor
public class User implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String email;

    private String senha;

    @OneToOne(mappedBy = "user")
    private Carrinho carrinho;

    public User(Long id, String name, String email, String senha){
        this.id = id;
        this.name = name;
        this.email = email;
        this.senha = senha;
    }


}
