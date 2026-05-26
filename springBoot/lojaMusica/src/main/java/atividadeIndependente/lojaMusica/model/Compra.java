package atividadeIndependente.lojaMusica.model;

import jakarta.persistence.*;

import java.util.UUID;

@Entity
public class Compra {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private UUID id;

    @ManyToOne
    @JoinColumn(name = "produto_comprado")
    private Produto produto;
}
