create table "user"
(
    id    text not null
        constraint user_pk
            primary key,
    name  text,
    email text
);

alter table "user"
    owner to django_api;


create table board
(
    idx     serial
        constraint board_pk
            primary key,
    title   text,
    content text,
    id      text
        constraint board_fk
            references "user"
);

alter table board
    owner to django_api;
