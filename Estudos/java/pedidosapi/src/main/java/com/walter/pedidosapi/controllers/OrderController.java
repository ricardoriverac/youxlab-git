package com.walter.pedidosapi.controllers;

import com.walter.pedidosapi.dtos.OrderRegisterDTO;
import com.walter.pedidosapi.dtos.OrderResponseDTO;
import com.walter.pedidosapi.dtos.PageResponseDTO;
import com.walter.pedidosapi.dtos.UserResponseDTO;
import com.walter.pedidosapi.models.Order;
import com.walter.pedidosapi.services.OrderService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/orders")
@Tag(name = "Pedidos")
public class OrderController {
    private final OrderService orderService;

    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @PostMapping("/register")
    @Operation(summary = "Registrar pedido", description = "Criar novo pedido")
    @ApiResponses({
            @ApiResponse(responseCode = "201", description = "Pedido criado com sucesso"),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "404", description = "Produto não encontrado", content = @Content),
            @ApiResponse(responseCode = "409", description = "Quantidade maior que o estoque ou concorrência ao realizar pedido", content = @Content)
    })
    public ResponseEntity<OrderResponseDTO> registerOrder(@RequestBody @Valid OrderRegisterDTO data){
        OrderResponseDTO response = orderService.createOrder(data);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @GetMapping()
    @Operation(summary = "Buscar todos", description = "Buscar todos os pedidos")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Pedidos buscados"),
            @ApiResponse(responseCode = "403", description = "Não permitido", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
    public ResponseEntity<PageResponseDTO<OrderResponseDTO>> getAll(@RequestParam(defaultValue = "0") int page, @RequestParam(defaultValue = "20") int size){
        return ResponseEntity.ok(orderService.getAll(page, size));
    }

    @GetMapping("/{id}")
    @Operation(summary = "Buscar por id", description = "Buscar um pedido por id")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Pedido encontrado"),
            @ApiResponse(responseCode = "403", description = "Não permitido", content = @Content),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "404", description = "Pedido não encontrado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
    public ResponseEntity<OrderResponseDTO> getById(@PathVariable UUID id){
        return ResponseEntity.ok(orderService.getById(id));
    }

    @GetMapping("/me")
    @Operation(summary = "Buscar meus pedidos", description = "Buscar meus pedidos")
    @ApiResponses({
            @ApiResponse(responseCode = "200", description = "Pedido encontrado"),
            @ApiResponse(responseCode = "401", description = "Não autenticado", content = @Content),
            @ApiResponse(responseCode = "500", description = "Erro inesperado no servidor", content = @Content)
    })
    public ResponseEntity<List<OrderResponseDTO>> getOrdersMe(){
        return ResponseEntity.ok(orderService.getOrdersMe());
    }
}