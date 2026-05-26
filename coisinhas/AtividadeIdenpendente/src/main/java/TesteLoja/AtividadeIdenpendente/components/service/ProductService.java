package TesteLoja.AtividadeIdenpendente.components.service;

import TesteLoja.AtividadeIdenpendente.components.Repositories.ProductRepository;
import TesteLoja.AtividadeIdenpendente.components.entities.CarrinhoItem;
import TesteLoja.AtividadeIdenpendente.components.entities.Compra;
import TesteLoja.AtividadeIdenpendente.components.entities.Product;
import org.aspectj.weaver.ast.Var;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service

public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    @Autowired
    private Product product;

    public Product findProduct(Long id){
        Optional<Product> product1 = this.productRepository.findById(id);
        return product1.orElseThrow(() -> new RuntimeException("PRODUTO NÃO ENCONTRADA"));
    }

    public Product creatingProduct(Product product){
        product.setId(null);
        product = this.productRepository.save(product);
        return product;
    }

    public Product comprando(Product product, Long id){

        product = findProduct(id);
        product.setCarrinhoItems(product.getCarrinhoItems());
        return product;
    }
}
