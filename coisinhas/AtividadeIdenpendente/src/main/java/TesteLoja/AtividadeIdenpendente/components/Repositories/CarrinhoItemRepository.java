package TesteLoja.AtividadeIdenpendente.components.Repositories;

import TesteLoja.AtividadeIdenpendente.components.entities.CarrinhoItem;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CarrinhoItemRepository extends JpaRepository<CarrinhoItem, Long> {
}
