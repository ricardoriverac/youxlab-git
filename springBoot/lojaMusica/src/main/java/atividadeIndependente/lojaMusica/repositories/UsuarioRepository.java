package atividadeIndependente.lojaMusica.repositories;

import atividadeIndependente.lojaMusica.model.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface UsuarioRepository extends JpaRepository<Usuario, UUID> {
}
