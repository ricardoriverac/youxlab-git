package TesteLoja.AtividadeIdenpendente.components.entities;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Entity
@Table(name = "tb_carrinhoitem")
@Data
@NoArgsConstructor
public class CarrinhoItem implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne
    @JoinColumn(name = "carrinho")
    private Carrinho carrinho;

    @ManyToOne
    @JoinColumn(name = "product")
    private Product product;

    public CarrinhoItem(Long id){
        this.id = id;
    }


}
