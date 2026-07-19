package com.coffeeshop.clean;

public class OrderProcessor {
    private final TaxCalculator taxCalculator;
    private final ReceiptFormatter formatter;
    private final OrderRepository repository;

    public OrderProcessor(TaxCalculator taxCalculator, ReceiptFormatter formatter, OrderRepository repository) {
        this.taxCalculator = taxCalculator;
        this.formatter = formatter;
        this.repository = repository;
    }

    public void processOrder(String customerName, String coffeeType, double price) {
        Order order = new Order(customerName, coffeeType, price);

        // Calculate tax using the injected calculator
        double taxAmount = taxCalculator.calculateTax(order.getBasePrice());
        double taxRate = taxAmount / order.getBasePrice();
        order.applyTax(taxRate);

        // Format and display receipt
        String receipt = formatter.format(order);
        System.out.println(receipt);

        // Save order to repository
        try {
            repository.save(order);
            System.out.println("[Repository] Order saved successfully.");
        } catch (Exception e) {
            System.out.println("[Repository ERROR] " + e.getMessage());
        }
    }
}
