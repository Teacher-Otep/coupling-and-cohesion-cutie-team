package com.coffeeshop.clean;

import java.io.FileWriter;
import java.io.IOException;

public class FileOrderRepository implements OrderRepository {
    private final String filePath;

    public FileOrderRepository(String filePath) {
        this.filePath = filePath;
    }

    @Override
    public void save(Order order) throws IOException {
        try (FileWriter writer = new FileWriter(filePath, true)) {
            writer.write(String.format("Customer: %s | Item: %s | Total: %.2f\n",
                    order.getCustomerName(), order.getItem(), order.getFinalPrice()));
        }
    }
}
