create table users(
                      id UUID primary key not null,
                      name TEXT not null,
                      email TEXT unique not null,
                      birth_date date not null,
                      password TEXT not null,
                      role TEXT not null,
                      enabled BOOLEAN not null,
                      created_at timestamp not null
);

create table bets(
                     id UUID primary key not null,
                     bet_value decimal(10,2) not null,
                     gain_value decimal(10,2),
                     status TEXT not null,
                     number_of_diamonds INTEGER not null,
                     start_date timestamp not null,
                     end_date timestamp,
                     user_id UUID not null,

                     constraint fk_bet_user
                         foreign key (user_id)
                             references users(id)
);

create table bet_bomb_positions(
                                   bet_id UUID not null,
                                   bomb_positions INTEGER not null,

                                   constraint fk_bomb_bet
                                       foreign key (bet_id)
                                           references bets(id)
                                           on delete cascade
);

create table bet_revealed_positions(
                                       bet_id UUID not null,
                                       revealed_positions INTEGER not null,

                                       constraint fk_revealed_bet
                                           foreign key (bet_id)
                                               references bets(id)
                                               on delete cascade
);

create table verification_token(
                                   id UUID primary key not null,
                                   token TEXT not null,
                                   token_expiration timestamp not null,
                                   user_id UUID unique,

                                   constraint fk_token_user
                                       foreign key (user_id)
                                           references users(id)
                                           on delete cascade
);