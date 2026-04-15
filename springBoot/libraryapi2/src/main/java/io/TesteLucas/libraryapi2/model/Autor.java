package io.TesteLucas.libraryapi2.model;

import jakarta.persistence.*;
import lombok.*;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;
import java.util.List;
import java.util.UUID;

@Entity
@Table(name = "autor", schema = "public")
@NoArgsConstructor
@AllArgsConstructor
@Data
@ToString(exclude = {"Livros"})
@EntityListeners(AuditingEntityListener.class)
public class Autor {

    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID ID;

    @Column(name = "nome", length = 100, nullable = false)
    private String name;

    @Column(name = "nacionalidade", length = 50, nullable = false)
    private String nacionalidade;


    @Column(name = "dataNascimento")
    private LocalDate dataNascimento;

    @Transient
    //@OneToMany(mappedBy = "autor")
    private List<Livro> livros;

    //data_cadastro timestamp,
    //    data_atualizacao timestamp,
    //    id_usuario uuid

    @CreatedDate
    @Column(name = "data_cadastro")
    private LocalDateTime dataCadastro;

    @LastModifiedDate
    @Column(name = "data_atualizacao")
    private LocalDateTime dataAtualizacao;

    @Column(name = "id_usuario")
    private UUID idUsuario;
}
