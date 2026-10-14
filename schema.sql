CREATE DATABASE IF NOT EXISTS railway_coach_db;
USE railway_coach_db;
CREATE TABLE IF NOT EXISTS trains (
 id INT AUTO_INCREMENT PRIMARY KEY,
 train_number VARCHAR(20) NOT NULL UNIQUE,
 train_name VARCHAR(100) NOT NULL,
 source_station VARCHAR(100) NOT NULL,
 destination_station VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS coaches (
 id INT AUTO_INCREMENT PRIMARY KEY,
 coach_number VARCHAR(30) NOT NULL UNIQUE,
 coach_type VARCHAR(50) NOT NULL,
 current_station VARCHAR(100) NOT NULL,
 status ENUM('Available','Under Maintenance') NOT NULL DEFAULT 'Available'
);
CREATE TABLE IF NOT EXISTS requirements (
 id INT AUTO_INCREMENT PRIMARY KEY,
 train_id INT NOT NULL,
 coach_type VARCHAR(50) NOT NULL,
 quantity INT NOT NULL,
 CONSTRAINT fk_requirements_train FOREIGN KEY (train_id) REFERENCES trains(id),
 CONSTRAINT chk_requirement_quantity CHECK (quantity >= 1)
);
CREATE TABLE IF NOT EXISTS allocations (
 id INT AUTO_INCREMENT PRIMARY KEY,
 train_id INT NOT NULL,
 coach_id INT NOT NULL,
 allocation_status ENUM('Active','Released') NOT NULL DEFAULT 'Active',
 allocated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 CONSTRAINT fk_allocations_train FOREIGN KEY (train_id) REFERENCES trains(id),
 CONSTRAINT fk_allocations_coach FOREIGN KEY (coach_id) REFERENCES coaches(id)
);
