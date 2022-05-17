CREATE TABLE IF NOT EXISTS `flask_sample`.`users` (
    `id` INT AUTO_INCREMENT NOT NULL COMMENT 'UserID',
    `email` VARCHAR(100) NOT NULL COMMENT 'User Email',
    `password` VARCHAR(100) NOT NULL COMMENT 'Password',
    `name` VARCHAR(50) NOT NULL COMMENT 'Username',
    PRIMARY KEY (`id`)
)
ENGINE = InnoDB;