package com.coffeeshop.clean;

public class Order {
    private final String customerName;
    private final String item;
    private final double basePrice;
    private double taxAmount;
    private double finalPrice;

    public Order(String customerName, String item, double basePrice) {
        this.customerName = customerName;
        this.item = item;
        this.basePrice = basePrice;
    }

    public String getCustomerName() {
        return customerName;
    }

    public String getItem() {
        return item;
    }

    public double getBasePrice() {
        return basePrice;
    }

    public double getTaxAmount() {
        return taxAmount;
    }

    public double getFinalPrice() {
        return finalPrice;
    }

    public void applyTax(double taxRate) {
        this.taxAmount = basePrice * taxRate;
        this.finalPrice = basePrice + taxAmount;
    }
}
