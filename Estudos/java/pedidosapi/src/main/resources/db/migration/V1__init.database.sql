    create table users (
        id UUID primary key not null,
        name TEXT not null,
        email TEXT unique not null,
        password TEXT not null,
        role TEXT not null,
        created_at TIMESTAMP not null
    );

    create table products (
        id UUID primary key not null,
        name TEXT not null,
        description TEXT not null,
        price DECIMAL(10,2) not null,
        stock_quantity INTEGER not null
    );

    create table orders (
        id UUID primary key not null,
        user_id UUID not null,
        order_date TIMESTAMP not null,
        total_value DECIMAL(10,2) not null,

        constraint fk_order_client
            foreign key (user_id)
                references users(id)
                on delete cascade
    );

    create table order_items (
         id UUID primary key not null,
         order_id UUID not null,
         product_id UUID not null,
         quantity INT not null,
         unit_price DECIMAL(10,2) not null,

         constraint fk_item_order
             foreign key (order_id)
                 references orders(id)
                 on delete cascade,

         constraint fk_item_product
             foreign key (product_id)
                 references products(id)
    );

    create table password_reset_token(
                                       id UUID primary key not null,
                                       token TEXT not null,
                                       token_expiration timestamp not null,
                                       user_id UUID unique,

                                       constraint fk_token_user
                                           foreign key (user_id)
                                               references users(id)
                                               on delete cascade
    );