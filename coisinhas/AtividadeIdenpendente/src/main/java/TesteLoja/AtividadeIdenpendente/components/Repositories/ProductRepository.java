package TesteLoja.AtividadeIdenpendente.components.Repositories;

import TesteLoja.AtividadeIdenpendente.components.entities.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> {
}
