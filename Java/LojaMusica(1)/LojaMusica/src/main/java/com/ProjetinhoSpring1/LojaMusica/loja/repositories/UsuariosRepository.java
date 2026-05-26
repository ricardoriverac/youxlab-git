package com.ProjetinhoSpring1.LojaMusica.loja.repositories;

import com.ProjetinhoSpring1.LojaMusica.loja.entities.UsuarioEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UsuariosRepository extends JpaRepository<UsuarioEntity, Integer> {
}
