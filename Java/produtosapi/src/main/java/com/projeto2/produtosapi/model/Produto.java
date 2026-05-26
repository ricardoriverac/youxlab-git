package com.projeto2.produtosapi.model;


import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;


@Entity
//Cria uma table no Banco de Dados
//Entretanto, caso haja uma tabela de mesmo nome, não se faz necessário o uso do @Table
@Table(name = "produto")
@AllArgsConstructor
@NoArgsConstructor
public class Produto {

    /*Adicionar @Column para cada coluna que formará dentro do Banco de Dados
     Entretanto, caso haja colunas com o mesmo nome dos atributos, não se faz necessária
     a aplicação do @Column
     EX: @Column(name = "nome da coluna")
     Assim, mapeará corretamente cada coluna*/
    @Id
    @Column(name = "id")
    private String id;
    @Column(name = "nome")
    private String nome;
    @Column(name = "descricao")
    private String descricao;
    @Column(name = "preco")
    private Double preco;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public Double getPreco() {
        return preco;
    }

    public void setPreco(Double preco) {
        this.preco = preco;
    }
}
