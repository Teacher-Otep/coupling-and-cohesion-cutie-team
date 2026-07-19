package com.coffeeshop.clean;

public interface OrderRepository {
    void save(Order order) throws Exception;
}
