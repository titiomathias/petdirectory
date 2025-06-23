-- -----------------------------------------------------
-- Schema petdir
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `petdir` DEFAULT CHARACTER SET utf8 ;
USE `petdir` ;

-- -----------------------------------------------------
-- Table `petdir`.`tutores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tutores` (
  `email` VARCHAR(64) NOT NULL,
  `nome` VARCHAR(64) NOT NULL,
  `senha` VARCHAR(64) NOT NULL,
  `telefone` VARCHAR(16) NOT NULL,
  PRIMARY KEY (`email`)
)
;


-- -----------------------------------------------------
-- Table `petdir`.`pets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pets` (
  `id` INT NOT NULL,
  `nome` VARCHAR(32) NOT NULL,
  `especie` VARCHAR(16) NOT NULL,
  `raca` VARCHAR(32) NOT NULL DEFAULT 'Desconhecido',
  `nascimento` DATE NULL,
  `peso` FLOAT NULL,
  `imagem` VARCHAR(128) NULL,
  `tutor_email` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`, `tutor_email`),
  INDEX `fk_pets_tutores_idx` (`tutor_email` ASC),
  CONSTRAINT `fk_pets_tutores`
    FOREIGN KEY (`tutor_email`)
    REFERENCES `tutores` (`email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `petdir`.`consultas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `consultas` (
  `id` INT NOT NULL,
  `data` DATE NOT NULL,
  `resultado` VARCHAR(512) NOT NULL,
  `pets_id` INT NOT NULL,
  `pets_tutor_email` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_consultas_pets1_idx` (`pets_id` ASC, `pets_tutor_email` ASC) VISIBLE,
  CONSTRAINT `fk_consultas_pets1`
    FOREIGN KEY (`pets_id` , `pets_tutor_email`)
    REFERENCES `pets` (`id` , `tutor_email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `petdir`.`profissional`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `profissional` (
  `nome` VARCHAR(32) NOT NULL,
  `email` VARCHAR(64) NULL,
  `telefone` VARCHAR(16) NOT NULL,
  `clinica` VARCHAR(64) NULL,
  `consultas_id` INT NOT NULL,
  INDEX `fk_profissional_consultas1_idx` (`consultas_id` ASC),
  CONSTRAINT `fk_profissional_consultas1`
    FOREIGN KEY (`consultas_id`)
    REFERENCES `consultas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;


-- -----------------------------------------------------
-- Table `petdir`.`diagnosticos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `diagnosticos` (
  `id` INT NOT NULL,
  `nome` VARCHAR(32) NOT NULL,
  `detalhamento` VARCHAR(256) NOT NULL,
  `data` DATE NOT NULL,
  `pets_id` INT NOT NULL,
  `pets_tutor_email` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`, `pets_id`, `pets_tutor_email`),
  INDEX `fk_diagnosticos_pets1_idx` (`pets_id` ASC, `pets_tutor_email` ASC),
  CONSTRAINT `fk_diagnosticos_pets1`
    FOREIGN KEY (`pets_id` , `pets_tutor_email`)
    REFERENCES `pets` (`id` , `tutor_email`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
;
