package com.walter.pedidosapi.dtos;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.v3.oas.annotations.media.Schema;

@Schema(name = "ForgotEmail")
public record ForgotEmailDTO(
    @JsonProperty("email")
    String email
)
{}