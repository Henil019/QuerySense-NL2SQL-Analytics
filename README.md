# QuerySense – AI-Powered Sales & E-Commerce Analytics Platform

## Overview

QuerySense is an AI-powered analytics platform that enables users to analyze e-commerce business data using natural language instead of writing SQL queries manually.

The system converts business questions into SQL using a locally hosted Large Language Model (LLM) running through Ollama, executes the generated query on SQL Server, and dynamically displays the results in a reusable analytics grid.

---

## Problem Statement

Traditional analytics systems require users to learn SQL, navigate complex dashboards, or depend on technical teams for custom reports.

QuerySense solves this problem by allowing users to ask business questions in plain English. The system automatically generates SQL queries, retrieves data from SQL Server, and presents business insights instantly.

---

## Key Features

### AI-Powered Analytics

* Natural Language to SQL (NL2SQL)
* Local AI processing using Ollama
* Dynamic SQL query generation
* Real-time business analytics
* SQL validation before execution

### Dynamic Reporting Engine

* Single reusable analytics page
* Schema-agnostic dynamic data grid
* Dynamic column generation
* No hardcoded report pages

### Database Analytics

* Customer Analytics
* Product Analytics
* Revenue Analytics
* Category Analytics
* Order Analytics

### Security

* Read-only query execution
* Restriction to SELECT statements
* Prevention of destructive SQL commands

### Data Engineering

* Realistic dataset generation using Faker
* Synthetic customer, product, and order data
* Business-scale sample dataset

---

## Technology Stack

| Category        | Technologies                                            |
| --------------- | ------------------------------------------------------- |
| Frontend        | ASP.NET MVC, HTML5, CSS3, Bootstrap, JavaScript, jQuery |
| Backend         | Python Flask                                            |
| AI              | Ollama, Phi-3                                           |
| Database        | SQL Server                                              |
| Data Access     | ADO.NET                                                 |
| Data Generation | Faker                                                   |

---

## System Architecture

```text
User Question
      ↓
ASP.NET MVC Interface
      ↓
Python Flask API
      ↓
Prompt Engineering
      ↓
Ollama (Phi-3)
      ↓
SQL Generation
      ↓
SQL Validation
      ↓
SQL Server
      ↓
Dynamic Analytics Grid
      ↓
Business Insights
```

---

## Database Schema

### Customers

* CustomerId
* CustomerName
* Email
* City
* Country
* CreatedDate

### Categories

* CategoryId
* CategoryName

### Products

* ProductId
* ProductName
* CategoryId
* Price
* StockQuantity

### Orders

* OrderId
* CustomerId
* OrderDate
* TotalAmount

### OrderItems

* OrderItemId
* OrderId
* ProductId
* Quantity
* UnitPrice

---

## Engineering Highlights

### Dynamic Grid Architecture

Instead of creating separate report pages for each business report, QuerySense uses a single reusable dynamic grid that automatically renders any SQL result set returned by the AI-generated query.

### Local AI Processing

The entire AI workflow runs locally using Ollama and Phi-3, providing data privacy, offline capability, and zero cloud inference cost.

### Synthetic Data Generation

Large-scale realistic e-commerce datasets were generated using the Faker library, including customers, products, orders, and order items for testing business analytics scenarios.

### AI-Driven Query Generation

Business users can interact with the database using conversational English rather than SQL, making analytics accessible to non-technical users.

---

