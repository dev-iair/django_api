DO $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..10 LOOP
        INSERT INTO "user" (id, name, email)
        VALUES
            ('user_' || i, '유저' || i, 'user_' || i || '@example.com');
    END LOOP;
END $$;

DO $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..10 LOOP
        FOR j IN 1..10 LOOP
            INSERT INTO "board" (id, title, content)
            VALUES
                ('user_' || i, '유저' || i || '_제목_' || j, '유저' || i || '_내용_' || j);
        END LOOP;
    END LOOP;
END $$;