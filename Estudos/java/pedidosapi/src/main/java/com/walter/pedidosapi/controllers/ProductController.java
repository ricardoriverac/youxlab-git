package com.walter.pedidosapi.controllers;


import com.walter.pedidosapi.dtos.PageResponseDTO;
import com.walter.pedidosapi.dtos.ProductRegisterDTO;
import com.walter.pedidosapi.dtos.ProductResponseDTO;
import com.walter.pedidosapi.dtos.UpdateProductDTO;
import com.walter.pedidosapi.models.Product;
import com.walter.pedidosapi.services.ProductService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/products")
@Tag(name = "Produtos")
public class ProductController {
    private final ProductService productService;

    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    @PostMapping("/register")
    @Operation(summary = "Registrar produto", description = "Cadastrar novo produto")
    @ApiResponses({
            @ApiResponse(responseCode = "201", description = "Produto registrado com sucesso"),
            @ApiResponse(responseCode = "400", description = "Preço inválido", content = @Content),
            @ApiResponse(responseCode = "409", description = "Já existe produto com este nome", content = @Content)
    })
    public ResponseEntity<ProductResponseDTO> registerProduct(@RequestBody @Valid ProductRegisterDTO data){
        ProductResponseDTO response = productService.registerProduct(data);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @GetMapping()
    @Operation(summary = "Buscar todos", description = "Buscar todos os produtos por página")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Produtos buscados"),
            @ApiResponse(responseCode = "403", description = "Não permitido", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
        public ResponseEntity<PageResponseDTO<ProductResponseDTO>> getAll(@RequestParam(defaultValue = "0") int page, @RequestParam(defaultValue = "20") int size){
            return ResponseEntity.ok(productService.getAll(page , size));
        }

    @GetMapping("/{id}")
    @Operation(summary = "Buscar por id", description = "Buscar um produto por id")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Produto encontrado"),
            @ApiResponse(responseCode = "403", description = "Não permitido", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "404", description = "Produto não encontrado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
    public ResponseEntity<ProductResponseDTO> getById(@PathVariable UUID id){
        return ResponseEntity.ok(productService.getById(id));
    }

    @PatchMapping("/{id}")
    @Operation(summary = "Atualizar produto", description = "Atualizar dados do produto")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Dados atualizados"),
            @ApiResponse(responseCode = "403", description = "Não permitido", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "404", description = "Produto não encontrado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
    public ResponseEntity<ProductResponseDTO> updateProduct(@PathVariable UUID id, @RequestBody @Valid UpdateProductDTO data){
        return ResponseEntity.ok(productService.updateProduct(id, data));
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "Deletar produto", description = "Deletar produto")
    @ApiResponses({
            @ApiResponse(responseCode = "204", description = "Produto deletado com sucesso"),
            @ApiResponse(responseCode = "403", description = "Não permitido", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "404", description = "Produto não encontrado", content = @Content)
    })
    public ResponseEntity<Void> deleteProduct(@PathVariable UUID id){
        productService.deleteProduct(id);
        return ResponseEntity.noContent().build();
    }

}