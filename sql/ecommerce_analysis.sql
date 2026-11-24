-- Active: 1795143349553@@127.0.0.1@5432@ecommerce_analysis
CREATE DATABASE ecommerce_analysis;

SELECT current_database();

SELECT table_name 
FROM information_schema.tables
WHERE table_schema = 'public';