package com.walter.pedidosapi.services;

import com.walter.pedidosapi.dtos.ProductRegisterDTO;
import com.walter.pedidosapi.dtos.ProductResponseDTO;
import com.walter.pedidosapi.dtos.UpdateProductDTO;
import com.walter.pedidosapi.models.Product;
import com.walter.pedidosapi.repositories.ProductRepository;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.server.ResponseStatusException;

import java.math.BigDecimal;
import java.util.List;
import java.util.UUID;

@Service
public class ProductService {
    private final ProductRepository productRepository;

    public ProductService(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    @Transactional
    public ProductResponseDTO registerProduct(ProductRegisterDTO data){
        String normalizedName = data.name().toLowerCase().trim();
        if(productRepository.existsByName(normalizedName)){
            throw new ResponseStatusException(
                    HttpStatus.CONFLICT,
                    "Já existe produto com este nome"
            );
        }

        Product newProduct = new Product();
        newProduct.setName(normalizedName);
        newProduct.setDescription(data.description());
        if (data.price().compareTo(new BigDecimal("100000")) > 0){
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Preço inválido");
        }
        newProduct.setPrice(data.price());
        newProduct.setStockQuantity(data.stockQuantity());
        productRepository.save(newProduct);
        ProductResponseDTO response = new ProductResponseDTO(newProduct.getId(), newProduct.getName(), newProduct.getDescription(),newProduct.getPrice(), newProduct.getStockQuantity());
        return response;
    }

    @Transactional(readOnly = true)
    public List<ProductResponseDTO> getAll(){
        List<ProductResponseDTO> response = productRepository.findAll()
                .stream()
                .map(product -> new ProductResponseDTO(product.getId(), product.getName(), product.getDescription(), product.getPrice(), product.getStockQuantity()))
                .toList();
        return response;
    }

    @Transactional(readOnly = true)
    public ProductResponseDTO getById(UUID id){
        Product product = productRepository.findById(id).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Produto não encontrado"));
        ProductResponseDTO response = new ProductResponseDTO(product.getId(), product.getName(), product.getDescription(), product.getPrice(), product.getStockQuantity());
        return response;
    }

    @Transactional
    public ProductResponseDTO updateProduct(UUID id, UpdateProductDTO data){
        Product product = productRepository.findById(id).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Produto não encontrado"));
        String normalizedName = data.name().toLowerCase().trim();
        if(productRepository.existsByName(normalizedName) && !product.getName().equals(normalizedName)){
            throw new ResponseStatusException(HttpStatus.CONFLICT, "Já possui um produto com este nome");
        }
        product.setName(normalizedName);
        product.setDescription(data.description());
        if (data.price().compareTo(new BigDecimal("100000")) > 0){
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Preço inválido");
        }
        product.setPrice(data.price());
        product.setStockQuantity(data.stockQuantity());

        return new ProductResponseDTO(product.getId(), product.getName(), product.getDescription(), product.getPrice(), product.getStockQuantity());

    }

    @Transactional
    public void deleteProduct(UUID id){
        Product product = productRepository.findById(id).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Produto não encontrado"));
        productRepository.delete(product);
    }
}
