package TesteLoja.AtividadeIdenpendente.components.entities;

import TesteLoja.AtividadeIdenpendente.components.enuns.Status;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.io.Serializable;

@Entity
@Getter
@Setter
@NoArgsConstructor
@Table(name = "tb_compra")
public class Compra implements Serializable {

    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long Id;

    @ManyToOne
    @JoinColumn(name = "produto_id")
    private Product productCompra;

    private Status status;

    public Compra(Long id, Status status){
        this.Id = id;
        this.status = status;
    }
}
