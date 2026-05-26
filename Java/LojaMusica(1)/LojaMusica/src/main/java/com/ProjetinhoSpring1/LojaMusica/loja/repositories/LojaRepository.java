package com.ProjetinhoSpring1.LojaMusica.loja.repositories;

import com.ProjetinhoSpring1.LojaMusica.loja.entities.LojaEntity;
import com.ProjetinhoSpring1.LojaMusica.loja.entities.UsuarioEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface LojaRepository extends JpaRepository<LojaEntity, Integer> {
}
