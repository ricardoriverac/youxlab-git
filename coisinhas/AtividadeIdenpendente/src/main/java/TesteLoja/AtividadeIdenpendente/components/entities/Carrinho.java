package TesteLoja.AtividadeIdenpendente.components.entities;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Entity
@Table(name = "tb_carrinho")
@Data
@NoArgsConstructor
public class Carrinho implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne
    @JoinColumn(name = "usuario_carrinho")
    private User user;

    @OneToOne(mappedBy = "carrinho")
    private CarrinhoItem carrinhoItem;

    public Carrinho(Long id){
        this.id = id;
    }
}

