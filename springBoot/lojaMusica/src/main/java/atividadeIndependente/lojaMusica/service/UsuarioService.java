package atividadeIndependente.lojaMusica.service;

import atividadeIndependente.lojaMusica.model.Usuario;
import atividadeIndependente.lojaMusica.repositories.UsuarioRepository;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class UsuarioService {

    private final UsuarioRepository repository;

    public UsuarioService(UsuarioRepository repository){
        this.repository = repository;
    }

    public Usuario salvando(Usuario usuario){
        UUID id = UUID.randomUUID();
        usuario.setId(id);
        return repository.save(usuario);
    }
}
