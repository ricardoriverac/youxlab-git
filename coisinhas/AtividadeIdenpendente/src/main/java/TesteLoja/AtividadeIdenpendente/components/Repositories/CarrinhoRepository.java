package TesteLoja.AtividadeIdenpendente.components.Repositories;

import TesteLoja.AtividadeIdenpendente.components.entities.Carrinho;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CarrinhoRepository extends JpaRepository<Carrinho, Long> {
}
