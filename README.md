# dbt Ecommerce Pipeline

An end-to-end ELT data pipeline built from scratch.

## Tech Stack
- Python (requests, psycopg2)
- PostgreSQL
- dbt-core + dbt-postgres

## Pipeline Architecture
Fake Store API → Python (extract + load) → PostgreSQL → dbt (transform) → Business Insights

## What it does
- Extracts products, users, and orders from Fake Store API
- Loads raw data into PostgreSQL using psycopg2
- Transforms data through staging and mart layers using dbt
- Answers business questions with SQL models

## Business Questions Answered
- Who are the top 5 customers by lifetime spend?
- Which product category generates the most revenue?

## Project Structure
ecommerce_analytics/
├── models/
│   ├── staging/        ← cleans and renames raw data
│   └── marts/          ← answers business questions
└── tests/              ← data quality checks
