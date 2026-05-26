package TesteLoja.AtividadeIdenpendente.components.Controllers;

import TesteLoja.AtividadeIdenpendente.components.Repositories.ProductRepository;
import TesteLoja.AtividadeIdenpendente.components.entities.Product;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RestController
@RequestMapping("/product")
public class ProductController {

    ProductRepository productRepository;

    public ProductController(ProductRepository productRepository){
        this.productRepository = productRepository;
    }

    @GetMapping("/{id}")
    public Product getando(@PathVariable Long id){
        return productRepository.findById(id).orElse(null);
    }

    @PostMapping
    public Product postando(@RequestBody Product product){
        System.out.println("Postando produto" + product);
        productRepository.save(product);
        return product;
    }

    @DeleteMapping("/{id}")
    public void deletando(@PathVariable Long id, Product product){
        productRepository.findById(id);
        productRepository.delete(product);

    }
}
