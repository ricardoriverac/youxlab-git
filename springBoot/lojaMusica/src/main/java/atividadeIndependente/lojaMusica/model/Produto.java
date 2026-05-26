package atividadeIndependente.lojaMusica.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;
import java.util.UUID;

@Entity
@NoArgsConstructor
@AllArgsConstructor
@Data
public class Produto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private UUID id;

    private String nome;

    private Double valor;

    private Double quantidade;

    @OneToMany(mappedBy = "produto")
    private List<Carrinho> carrinho;
}
