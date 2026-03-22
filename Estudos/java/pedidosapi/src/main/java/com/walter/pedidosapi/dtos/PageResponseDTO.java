package com.walter.pedidosapi.dtos;


import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;

import java.util.List;

@Schema(name = "PageResponse")
public record PageResponseDTO<T>(
        @Schema(name = "dados")
        @JsonProperty("dados")
        List<T> data,
        @Schema(name = "paginaAtual")
        @JsonProperty("paginaAtual")
        int currentPage,
        @Schema(name = "totalPaginas")
        @JsonProperty("totalPaginas")
        int totalPages,
        @Schema(name = "totalItens")
        @JsonProperty("totalItens")
        long totalItems,
        @Schema(name = "temProxima")
        @JsonProperty("temProxima")
        boolean hasNext,
        @Schema(name = "temAnterior")
        @JsonProperty("temAnterior")
        boolean hasPrevious
) {
}
