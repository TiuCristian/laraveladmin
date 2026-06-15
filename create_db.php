<?php
try {
    $pdo = new PDO('mysql:host=127.0.0.1;port=3306', 'root', '');
    $pdo->exec('CREATE DATABASE IF NOT EXISTS laravel_admin;');
    echo "Database created.\n";
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
