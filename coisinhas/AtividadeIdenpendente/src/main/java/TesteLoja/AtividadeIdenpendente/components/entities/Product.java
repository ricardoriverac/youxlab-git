package TesteLoja.AtividadeIdenpendente.components.entities;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;
import java.util.List;

@Entity
@Table(name = "tb_product")
@Data
@NoArgsConstructor
public class Product implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "name")
    private String name;

    @Column(name = "preco")
    private Double preco;

    @OneToMany(mappedBy = "product")
    private List<CarrinhoItem> carrinhoItems;

    @OneToMany(mappedBy = "productCompra")
    private List<Compra> compras;

    public Product(Long id, String name, Double preco){
        this.id = id;
        this.name = name;
        this.preco = preco;
    }
}
