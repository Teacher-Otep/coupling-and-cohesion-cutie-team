# Coupling and Cohesion Refactoring Project

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hjOhe93i)

## What We Did

We refactored the coffee shop order processing system to separate concerns and reduce coupling between components.

### Original Problem
The `naive/OrderProcessor.java` had everything in one class:
- Tax calculation logic
- Receipt formatting 
- File I/O operations

This made it hard to test, modify, or extend.

### Our Solution
We created separate classes in the `clean/` package:

- `Order.java` - Model for order data
- `TaxCalculator.java` (interface) - Handles tax logic
- `DefaultTaxCalculator.java` - Implementation of tax calculation
- `ReceiptFormatter.java` - Handles receipt formatting
- `OrderRepository.java` (interface) - Handles saving orders
- `FileOrderRepository.java` - File-based storage
- `OrderProcessor.java` - Coordinates everything

## Changes Made

### Before (Naive)
```java
public void processOrder(String customerName, String coffeeType, double price) {
    // Tax calculation
    double localTax = 0.12;
    double finalPrice = price + (price * localTax);
    
    // Receipt formatting
    System.out.println("===== COFFEE SHOP RECEIPT =====");
    System.out.println("Customer: " + customerName);
    
    // File I/O
    FileWriter writer = new FileWriter("orders_log.txt", true);
    writer.write("Customer: " + customerName + ...);
}
```

### After (Clean)
```java
public void processOrder(String customerName, String coffeeType, double price) {
    Order order = new Order(customerName, coffeeType, price);
    
    double taxAmount = taxCalculator.calculateTax(order.getBasePrice());
    order.applyTax(taxAmount / order.getBasePrice());
    
    String receipt = formatter.format(order);
    System.out.println(receipt);
    
    repository.save(order);
}
```

## Benefits
- Each class has one job (Single Responsibility)
- Easier to test (can mock dependencies)
- Easier to extend (add new tax types, storage methods, etc.)
- Reduced coupling between components
- Increased code cohesion

## Running the Code

Clean version:
```bash
java com.coffeeshop.clean.Main
```

Naive version:
```bash
java com.coffeeshop.naive.Main
```
