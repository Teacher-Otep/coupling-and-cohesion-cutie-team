package com.coffeeshop.clean;

public class ReceiptFormatter {
    public String format(Order order) {
        StringBuilder sb = new StringBuilder();
        sb.append("===== COFFEE SHOP RECEIPT =====\n");
        sb.append("Customer: ").append(order.getCustomerName()).append('\n');
        sb.append("Beverage: ").append(order.getItem()).append('\n');
        sb.append(String.format("Base Price: PHP %.2f\n", order.getBasePrice()));
        sb.append(String.format("Tax: PHP %.2f\n", order.getTaxAmount()));
        sb.append(String.format("Total Amount (incl. Tax): PHP %.2f\n", order.getFinalPrice()));
        sb.append("================================\n");
        return sb.toString();
    }
}
