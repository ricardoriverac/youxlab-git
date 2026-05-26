package atividadeIndependente.lojaMusica.DTO;

import atividadeIndependente.lojaMusica.model.Produto;

import java.util.UUID;

public record ProdutoDTO (
        UUID id,
        String nome,
        Double valor,
        Double quantity) {

    public Produto mappingProdut(){
        Produto produto = new Produto();
        produto.setNome(this.nome);
        produto.setValor(this.valor);
        produto.setQuantidade(this.quantity);
        return produto;
    }
}
