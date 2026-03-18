package com.example.controller;


import com.example.dto.LoginRequestDTO;
import com.example.dto.LoginResponseDTO;
import com.example.dto.ResetSenhaRequestDTO;
import com.example.dto.UserRequestDTO;
import com.example.model.ResetSenhaToken;
import com.example.model.User;
import com.example.repository.ResetSenhaTokenRepository;
import com.example.repository.UserRepository;
import com.example.service.AuthService;
import com.example.service.EmailService;
import com.example.service.ResetSenhaService;
import com.example.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
public class AuthController {



    @Autowired
    private UserService userService;

    @Autowired
    private EmailService emailService;


    @Autowired
    private ResetSenhaTokenRepository resetSenhaTokenRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private ResetSenhaService resetSenhaService;

    @Autowired
    private AuthService authService;


        @PostMapping("/login")
        public ResponseEntity login(@RequestBody LoginRequestDTO dados) {
            try {
                LoginResponseDTO response = authService.autenticar(dados);
                return ResponseEntity.ok(response);
            } catch (Exception e) {
                return ResponseEntity.badRequest().body(e.getMessage());
            }
        }


        @GetMapping("/confirmar-email")
        public ResponseEntity confirmarEmail(@RequestParam String token) {
            try {
                userService.confirmarEmail(token);
                return ResponseEntity.ok("Email confirmado, você já pode fazer login.");
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao confirmar email: " + e.getMessage());
            }
        }

        @PostMapping("/esqueci-senha") //ok
        public ResponseEntity esqueciSenha(@RequestBody ResetSenhaRequestDTO dados) {
            try {
                User user = userRepository.findByEmail(dados.email()).orElse(null);

                if (user != null) {
                    ResetSenhaToken token = new ResetSenhaToken(user);

                    resetSenhaTokenRepository.save(token);

                    emailService.enviarEmailResetSenha(user.getEmail(), token.getToken());
                }

                return ResponseEntity.ok("Se o email existir, você receberá um link para resetar sua senha.");

            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao processar solicitação: " + e.getMessage());
            }
        }


        @PostMapping("/resetar-senha") //ok
        public ResponseEntity resetarSenha(@RequestBody ResetSenhaRequestDTO dados) {
            try {
                resetSenhaService.resetarSenha(dados.token(), dados.novaSenha());            return ResponseEntity.ok("Senha alterada com sucesso!");
            } catch (Exception e) {
                return ResponseEntity.badRequest().body("Erro ao resetar senha: " + e.getMessage());
            }
        }

}

