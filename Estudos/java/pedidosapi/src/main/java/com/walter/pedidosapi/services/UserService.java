package com.walter.pedidosapi.services;

import com.walter.pedidosapi.dtos.*;
import com.walter.pedidosapi.models.PasswordResetToken;
import com.walter.pedidosapi.models.User;
import com.walter.pedidosapi.models.UserRole;
import com.walter.pedidosapi.repositories.PasswordResetTokenRepository;
import com.walter.pedidosapi.repositories.UserRepository;
import org.springframework.http.HttpStatus;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.server.ResponseStatusException;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class UserService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final PasswordResetTokenRepository passwordResetTokenRepository;
    private final EmailService emailService;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder, PasswordResetTokenRepository passwordResetTokenRepository, EmailService emailService) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.passwordResetTokenRepository = passwordResetTokenRepository;
        this.emailService = emailService;
    }

    @Transactional
    public RegisterResponseDTO registerUser(RegisterDTO data){
        String normalizedEmail = data.email().toLowerCase().trim();
        Optional<User> user = userRepository.findByEmail(normalizedEmail);
        if (user.isPresent()){
            throw new ResponseStatusException(
                    HttpStatus.CONFLICT,
                    "Este email ja possui uma conta cadastrada"
            );
        }
        User newUser = new User();
        newUser.setName(data.name().trim());
        newUser.setEmail(normalizedEmail);
        newUser.setPassword(passwordEncoder.encode(data.password()));
        newUser.setRole(UserRole.USER);
        newUser.setCreatedAt(LocalDateTime.now());

        userRepository.save(newUser);

        return new RegisterResponseDTO(newUser.getName(), newUser.getEmail());
    }

    @Transactional(readOnly = true)
    public List<UserResponseDTO> getAll(){
       return userRepository.findAll()
                .stream()
                .map(user -> new UserResponseDTO(user.getId(), user.getName(), user.getEmail(), user.getRole().toString(), user.getCreatedAt()))
                .toList();


    }

    @Transactional(readOnly = true)
    public UserResponseDTO getById(UUID id){
        User user = userRepository.findById(id).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Usuário não encontrado"));
        return new UserResponseDTO(user.getId(), user.getName(), user.getEmail(), user.getRole().toString(), user.getCreatedAt());
    }

    @Transactional(readOnly = true)
    public UserResponseDTO getMe(){
        User auth = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        return new UserResponseDTO(auth.getId(), auth.getName(), auth.getEmail(), auth.getRole().toString(), auth.getCreatedAt());
    }

    @Transactional
    public UserResponseDTO updateUser(UUID id, UpdateUserDTO data){
        User user = userRepository.findById(id).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Usuario não encontrado"));
        user.setName(data.name().trim());
        String normalizedEmail = data.email().toLowerCase().trim();
        if(userRepository.findByEmail(normalizedEmail).isPresent() && !user.getEmail().equals(normalizedEmail)){
            throw new ResponseStatusException(HttpStatus.CONFLICT, "Esse email já possui uma conta cadastrada");
        }
        user.setEmail(data.email().toLowerCase().trim());
        return new UserResponseDTO(user.getId(), user.getName(), user.getEmail(), user.getRole().toString(), user.getCreatedAt()
        );
    }

    @Transactional
    public void deleteUser(UUID id){
        User user = userRepository.findById(id).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Usuario não encontrado"));
        userRepository.delete(user);
    }

    @Transactional
    public void forgotPassword(ForgotEmailDTO data){
        String normalizedEmail = data.email().toLowerCase().trim();
        User user = userRepository.findByEmail(normalizedEmail).orElseThrow(() -> new ResponseStatusException(HttpStatus.NOT_FOUND, "Usuário não encontrado"));
        passwordResetTokenRepository.deleteByUser(user);
        passwordResetTokenRepository.flush();
        String token = UUID.randomUUID().toString();
        PasswordResetToken passwordResetToken = new PasswordResetToken();
        passwordResetToken.setToken(token);
        passwordResetToken.setUser(user);
        passwordResetToken.setTokenExpiration(LocalDateTime.now().plusHours(24));
        passwordResetTokenRepository.save(passwordResetToken);
        emailService.sendResetPassword(user.getEmail(), token);
    }

    @Transactional(readOnly = true)
    public PasswordResetToken validateToken(String token) {
        PasswordResetToken resetToken = passwordResetTokenRepository.findByToken(token).orElseThrow(() -> new ResponseStatusException(HttpStatus.BAD_REQUEST, "Token inválido"));

        if (resetToken.getTokenExpiration().isBefore(LocalDateTime.now())) {
            throw new ResponseStatusException(
                    HttpStatus.GONE, "Token expirado"
            );
        }

        return resetToken;
    }


        @Transactional
        public void resetPassword(ResetPasswordDTO data){
            PasswordResetToken token = validateToken(data.token());

            User user = token.getUser();
            user.setPassword(passwordEncoder.encode(data.newPassword()));

            userRepository.save(user);
            passwordResetTokenRepository.delete(token);
        }

    }