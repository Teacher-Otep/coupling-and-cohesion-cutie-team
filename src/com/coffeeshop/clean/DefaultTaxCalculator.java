package com.coffeeshop.clean;

public class DefaultTaxCalculator implements TaxCalculator {
    private final double taxRate;

    public DefaultTaxCalculator() {
        this(0.12); // default 12%
    }

    public DefaultTaxCalculator(double taxRate) {
        this.taxRate = taxRate;
    }

    @Override
    public double calculateTax(double basePrice) {
        return basePrice * taxRate;
    }
}
