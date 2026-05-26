package com.ProjetinhoSpring1.LojaMusica.loja.repositories;

import com.ProjetinhoSpring1.LojaMusica.loja.entities.InstrumentosEntity;
import com.ProjetinhoSpring1.LojaMusica.loja.entities.UsuarioEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface InstrumentosRepository extends JpaRepository<InstrumentosEntity, Integer> {
}
