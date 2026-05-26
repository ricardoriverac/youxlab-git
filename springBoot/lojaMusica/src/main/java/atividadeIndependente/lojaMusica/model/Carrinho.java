package atividadeIndependente.lojaMusica.model;

import jakarta.persistence.*;

import java.util.UUID;

@Entity
public class Carrinho {

    @ManyToOne
    @JoinColumn(name = "carrinho_produto")
    private Produto produto;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private UUID id;

}
