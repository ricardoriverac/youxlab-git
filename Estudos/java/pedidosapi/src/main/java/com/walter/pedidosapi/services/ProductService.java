package com.walter.pedidosapi.services;

import com.walter.pedidosapi.dtos.PageResponseDTO;
import com.walter.pedidosapi.dtos.ProductRegisterDTO;
import com.walter.pedidosapi.dtos.ProductResponseDTO;
import com.walter.pedidosapi.dtos.UpdateProductDTO;
import com.walter.pedidosapi.models.Product;
import com.walter.pedidosapi.models.User;
import com.walter.pedidosapi.repositories.ProductRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.HttpStatus;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.server.ResponseStatusException;

import java.awt.print.Pageable;
import java.math.BigDecimal;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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
    public PageResponseDTO<ProductResponseDTO> getAll(int page, int size){
        size = Math.max(size, 1);
        size = Math.min(size, 50);

        Page<Product> pageResult = productRepository.findAll(PageRequest.of(page, size));
        return new PageResponseDTO<>(
                pageResult.getContent()
                                .stream()
                                        .map(p -> new ProductResponseDTO(
                                                p.getId(),
                                                p.getName(),
                                                p.getDescription(),
                                                p.getPrice(),
                                                p.getStockQuantity()
                                        ))
                                            .toList(),
                pageResult.getNumber(),
                pageResult.getTotalPages(),
                pageResult.getTotalElements(),
                pageResult.hasNext(),
                pageResult.hasPrevious()
        );
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
