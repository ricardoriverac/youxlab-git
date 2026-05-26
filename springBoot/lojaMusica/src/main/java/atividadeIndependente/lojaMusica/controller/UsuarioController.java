package atividadeIndependente.lojaMusica.controller;

import atividadeIndependente.lojaMusica.DTO.UsuarioDTO;
import atividadeIndependente.lojaMusica.exceptions.RegistroDuplo;
import atividadeIndependente.lojaMusica.model.Usuario;
import atividadeIndependente.lojaMusica.repositories.UsuarioRepository;
import atividadeIndependente.lojaMusica.service.UsuarioService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping
@RequiredArgsConstructor
public class UsuarioController {
    private final UsuarioRepository repository;

    private final UsuarioService service;

    @PostMapping
    public ResponseEntity<Usuario> salvar (@RequestBody UsuarioDTO usuario){
        try {
            Usuario usuario1 = usuario.mapearParaUsuario();
            service.salvando(usuario1);

            return ResponseEntity.ok(usuario1);
        } catch (RegistroDuplo e){
            
            return ResponseEntity.status(HttpStatus.CONFLICT).build();
        }
    }

}
