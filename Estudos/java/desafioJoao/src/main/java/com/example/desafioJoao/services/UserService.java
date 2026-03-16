package com.example.desafioJoao.services;

import com.example.desafioJoao.dtos.*;
import com.example.desafioJoao.enums.BetStatus;
import com.example.desafioJoao.models.Bet;
import com.example.desafioJoao.models.User;
import com.example.desafioJoao.enums.UserRole;
import com.example.desafioJoao.models.VerificationToken;
import com.example.desafioJoao.repositories.BetRepository;
import com.example.desafioJoao.repositories.UserRepository;
import com.example.desafioJoao.repositories.VerificationTokenRepository;
import org.springframework.http.HttpStatus;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Period;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Service
public class UserService {
    private final UserRepository repository;
    private final PasswordEncoder passwordEncoder;
    private final VerificationTokenRepository verificationTokenRepository;
    private final EmailService emailService;
    private final BetRepository betRepository;

    public UserService(UserRepository repository, PasswordEncoder passwordEncoder, VerificationTokenRepository verificationTokenRepository, EmailService emailService, BetRepository betRepository) {
        this.repository = repository;
        this.passwordEncoder = passwordEncoder;
        this.verificationTokenRepository = verificationTokenRepository;
        this.emailService = emailService;
        this.betRepository = betRepository;
    }

    public RegisterResponseDTO createUser(RegisterDTO data){
        UserDetails user = repository.findByEmail(data.email());
        User newUser = new User();

        if (user != null){
            throw new ResponseStatusException(
                    HttpStatus.CONFLICT,
                    "Este email já possui conta cadastrada"
            );
        }
        newUser.setEmail(data.email().trim().toLowerCase());
        newUser.setName(data.name().trim());
        if (!data.confirmPassword().equals(data.password())){
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Esta senha não condiz com a senha cadastrada"
            );
        }
        newUser.setPassword(passwordEncoder.encode(data.password()));
        if(data.birthDate() == null){
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Data de nascimento é obrigatória"
            );
        }
        if(data.birthDate().isAfter(LocalDate.now())){
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Data de nascimento não pode ser futura"
            );
        }
        int age = Period.between(data.birthDate(), LocalDate.now()).getYears();
        if(age < 18){
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Usuário deve ter pelo menos 18 anos"
            );
        }
        newUser.setBirthDate(data.birthDate());
        newUser.setRole(UserRole.USER);

        newUser.setEnabled(false);

        repository.save(newUser);

        String token = UUID.randomUUID().toString();

        VerificationToken verificationToken = new VerificationToken();
        verificationToken.setToken(token);
        verificationToken.setUser(newUser);
        verificationToken.setTokenExpiration(LocalDateTime.now().plusHours(24));
        verificationTokenRepository.save(verificationToken);

        emailService.sendVerificationEmail(newUser.getEmail(), token);
        return new RegisterResponseDTO(
                newUser.getName(),
                newUser.getEmail()
        );
    }
    public void confirmToken(String token){

        VerificationToken verificationToken =
                verificationTokenRepository.findByToken(token)
                        .orElseThrow(() -> new ResponseStatusException(
                                HttpStatus.NOT_FOUND,
                                "Token inválido"
                        ));

        if(verificationToken.getTokenExpiration().isBefore(LocalDateTime.now())){
            throw new ResponseStatusException(
                    HttpStatus.BAD_REQUEST,
                    "Token expirado"
            );
        }

        User user = verificationToken.getUser();
        user.setEnabled(true);

        repository.save(user);
    }

    public User getUser(){
        var authentication = SecurityContextHolder.getContext().getAuthentication();
        User user = (User) authentication.getPrincipal();
        user = repository.findById(user.getId()).orElseThrow();
        return user;
    }

    public List<User> getAll(){
        return repository.findAll();
    }

    public void accountStatus(UUID id){
        User user = repository.findById(id).orElseThrow(() ->
                new ResponseStatusException(
                        HttpStatus.NOT_FOUND,
                        "Id inexistente"
                )
        );
        user.setEnabled(!user.isEnabled());
        repository.save(user);

    }

    public UserDashboardDTO getUserDashboard() {
        User userLogado = (User) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        List<Bet> bets = betRepository.findByUser(userLogado);
        int total = bets.size();
        int wins = 0;
        int lost = 0;

        for (Bet bet : bets) {
            if (bet.getStatus() == BetStatus.WON) {
                wins += 1;
            } else if (bet.getStatus() == BetStatus.LOST) {
                lost += 1;
            }
        }
        return new UserDashboardDTO(total, wins, lost);
    }

    public List<AdminUserDashboardDTO> getAdminUserDashboard(){
        List<User> users = repository.findAll();
        List<AdminUserDashboardDTO> dashboard = new ArrayList<>();
        for(User user : users){
            List<Bet> bets= betRepository.findByUser(user);
            int totalGame = bets.size();
            BigDecimal gainValue = BigDecimal.ZERO;
            for(Bet bet : bets){
                if(bet.getStatus() == BetStatus.WON){
                    gainValue = gainValue.add(bet.getGainValue());
                }
            }
            dashboard.add(new AdminUserDashboardDTO(user.getName(), totalGame, gainValue));
        }
        return dashboard;
    }

}
