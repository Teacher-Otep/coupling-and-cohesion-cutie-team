/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.coffeeshop.naive;

import com.coffeeshop.clean.DefaultTaxCalculator;
import com.coffeeshop.clean.FileOrderRepository;
import com.coffeeshop.clean.OrderProcessor;
import com.coffeeshop.clean.ReceiptFormatter;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Starting Clean Coffee Shop System ===");

        DefaultTaxCalculator taxCalculator = new DefaultTaxCalculator();
        ReceiptFormatter formatter = new ReceiptFormatter();
        FileOrderRepository repository = new FileOrderRepository("orders_log.txt");

        OrderProcessor processor = new OrderProcessor(taxCalculator, formatter, repository);

        // Simulating a customer ordering a Java Chip Frappe
        processor.processOrder("Juan Dela Cruz", "Java Chip Frappe", 150.0);

        System.out.println("\n=== Order Processing Complete ===");
    }
}
