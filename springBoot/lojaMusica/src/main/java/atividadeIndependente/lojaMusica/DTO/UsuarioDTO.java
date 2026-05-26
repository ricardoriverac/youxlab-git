package atividadeIndependente.lojaMusica.DTO;

import atividadeIndependente.lojaMusica.model.Usuario;

import java.util.UUID;

public record UsuarioDTO(
    UUID id,
    String name,
    String email,
    String senha
) {
    public Usuario mapearParaUsuario(){
        Usuario user = new Usuario();
        user.setName(this.name);
        user.setEmail(this.email);
        user.setSenha(this.senha);
        return user;
    }
}
