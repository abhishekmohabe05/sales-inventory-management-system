-- =========================================
-- DATABASE: sales_inventory
-- =========================================
CREATE DATABASE IF NOT EXISTS sales_inventory;
USE sales_inventory;

-- =========================================
-- TABLE: users
-- =========================================
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- =========================================
-- TABLE: products
-- =========================================
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0
);

-- =========================================
-- TABLE: sales
-- =========================================
CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME NOT NULL
);

-- =========================================
-- TABLE: sale_items
-- =========================================
CREATE TABLE IF NOT EXISTS sale_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sale_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES sales(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- =========================================
-- SAMPLE DATA (OPTIONAL)
-- =========================================

-- Sample Users
INSERT INTO users (username, password_hash, is_active) VALUES
('admin', '$pbkdf2-sha256$29000$dummyhash', TRUE);

-- Sample Products
INSERT INTO products (name, price, stock_quantity) VALUES
('Product A', 100.00, 10),
('Product B', 200.00, 8),
('Product C', 50.00, 3); -- Low stock example