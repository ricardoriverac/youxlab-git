package com.example.dto;

public class JogadaRequestDTO {

    @NotNull(message = "Posição X é obrigatória")
    @Min(value = 0, message = "X deve ser entre 0 e 4")
    @Max(value = 4, message = "X deve ser entre 0 e 4")
    private Integer x;

    @NotNull(message = "Posição Y é obrigatória")
    @Min(value = 0, message = "Y deve ser entre 0 e 4")
    @Max(value = 4, message = "Y deve ser entre 0 e 4")
    private Integer y;

    // Getters e Setters
    public Integer getX() { return x; }
    public void setX(Integer x) { this.x = x; }

    public Integer getY() { return y; }
    public void setY(Integer y) { this.y = y; }
}
