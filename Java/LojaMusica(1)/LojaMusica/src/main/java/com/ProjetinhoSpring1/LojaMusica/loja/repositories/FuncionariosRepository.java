package com.ProjetinhoSpring1.LojaMusica.loja.repositories;

import com.ProjetinhoSpring1.LojaMusica.loja.entities.FuncionariosEntity;
import com.ProjetinhoSpring1.LojaMusica.loja.entities.UsuarioEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FuncionariosRepository extends JpaRepository<FuncionariosEntity, String> {
}
