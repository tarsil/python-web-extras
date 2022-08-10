-- upgrade --
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(150) NOT NULL,
    "last_name" VARCHAR(150) NOT NULL,
    "username" VARCHAR(150) NOT NULL UNIQUE,
    "email" VARCHAR(120) NOT NULL UNIQUE,
    "password" VARCHAR(128) NOT NULL,
    "last_login" TIMESTAMPTZ,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "is_staff" BOOL NOT NULL  DEFAULT False,
    "is_superuser" BOOL NOT NULL  DEFAULT False
);
COMMENT ON COLUMN "users"."first_name" IS 'First name';
COMMENT ON COLUMN "users"."last_name" IS 'Last name';
COMMENT ON COLUMN "users"."username" IS 'Username';
COMMENT ON COLUMN "users"."email" IS 'Email address';
COMMENT ON COLUMN "users"."password" IS 'Password';
COMMENT ON COLUMN "users"."last_login" IS 'Last login';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
