# Coupling and Cohesion Refactoring Project

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hjOhe93i)

## Project Overview

This project demonstrates the transformation of a **tightly-coupled, monolithic coffee shop order processing system** into a **clean, loosely-coupled architecture** following SOLID principles.

### Objective
Refactor the naive implementation to achieve:
- ✅ **Low Coupling:** Components are independent
- ✅ **High Cohesion:** Each class has a single responsibility
- ✅ **SOLID Principles:** Proper object-oriented design
- ✅ **Testability:** Easy to unit test components
- ✅ **Extensibility:** Easy to add new features

## Project Structure

```
src/com/coffeeshop/
├── naive/                          ← Original tightly-coupled code
│   ├── Main.java                   ← Entry point
│   └── OrderProcessor.java         ← Monolithic class with 3 responsibilities
│
└── clean/                          ← Refactored low-coupling, high-cohesion code
    ├── Main.java                   ← Entry point (orchestrates components)
    ├── Order.java                  ← Data model
    ├── OrderProcessor.java         ← Orchestrates the workflow
    ├── TaxCalculator.java          ← Interface for tax strategies
    ├── DefaultTaxCalculator.java   ← Default tax implementation
    ├── ReceiptFormatter.java       ← Formats receipts
    ├── OrderRepository.java        ← Interface for data storage
    └── FileOrderRepository.java    ← File-based storage implementation
```

## The Problem (Naive Implementation)

### Issues with `naive/OrderProcessor.java`

The monolithic `OrderProcessor` class violates the **Single Responsibility Principle (SRP)** by handling **3 mixed concerns**:

#### 1. Business Logic (Tax Calculation)
```java
double localTax = 0.12; // Hardcoded 12% VAT
double finalPrice = price + (price * localTax);
```
- Hardcoded tax rate
- Cannot use different tax strategies
- Tax logic mixed with other concerns

#### 2. Presentation (Receipt Formatting)
```java
System.out.println("\n===== COFFEE SHOP RECEIPT =====");
System.out.println("Customer: " + customerName);
// ... more println calls
```
- Direct output to console
- Cannot change output format
- Formatting logic scattered throughout method

#### 3. Data Persistence (File I/O)
```java
FileWriter writer = new FileWriter("orders_log.txt", true);
writer.write("Customer: " + customerName + ...);
```
- Hardcoded file path
- File I/O mixed with business logic
- Cannot easily change storage backend

### Consequences
- ❌ **High Coupling:** OrderProcessor depends on implementation details
- ❌ **Low Cohesion:** Unrelated code in same class
- ❌ **Hard to Test:** Cannot test without actual file I/O
- ❌ **Hard to Extend:** Adding new features requires modifying OrderProcessor
- ❌ **Hard to Maintain:** Multiple reasons to change one class

## The Solution (Clean Architecture)

### Separation of Concerns

#### 1. **Order.java** - Data Model
```java
public class Order {
    private final String customerName;
    private final String item;
    private final double basePrice;
    private double taxAmount;
    private double finalPrice;
    
    public void applyTax(double taxRate) { ... }
}
```
**Responsibility:** Encapsulate order data  
**Benefit:** Single responsibility, immutable

#### 2. **TaxCalculator.java** - Tax Strategy Interface
```java
public interface TaxCalculator {
    double calculateTax(double basePrice);
}
```
**Responsibility:** Abstract tax calculation  
**Benefit:** Enables different tax strategies without modifying OrderProcessor

#### 3. **DefaultTaxCalculator.java** - Default Tax Implementation
```java
public class DefaultTaxCalculator implements TaxCalculator {
    private final double taxRate;
    
    public DefaultTaxCalculator(double taxRate) { ... }
    
    @Override
    public double calculateTax(double basePrice) {
        return basePrice * taxRate;
    }
}
```
**Responsibility:** Implement standard tax calculation  
**Benefit:** Configurable tax rate, can be replaced with other strategies

#### 4. **ReceiptFormatter.java** - Presentation Logic
```java
public class ReceiptFormatter {
    public String format(Order order) {
        StringBuilder sb = new StringBuilder();
        sb.append("===== COFFEE SHOP RECEIPT =====\n");
        // ... format order details
        return sb.toString();
    }
}
```
**Responsibility:** Format order as string  
**Benefit:** Separated from business logic, reusable, can create variants (HTML, PDF, etc.)

#### 5. **OrderRepository.java** - Data Persistence Interface
```java
public interface OrderRepository {
    void save(Order order) throws Exception;
}
```
**Responsibility:** Abstract data storage  
**Benefit:** Can implement with different backends (file, database, API, etc.)

#### 6. **FileOrderRepository.java** - File-Based Storage
```java
public class FileOrderRepository implements OrderRepository {
    private final String filePath;
    
    @Override
    public void save(Order order) throws IOException {
        try (FileWriter writer = new FileWriter(filePath, true)) {
            writer.write(String.format("Customer: %s | Item: %s | Total: %.2f\n",
                    order.getCustomerName(), order.getItem(), order.getFinalPrice()));
        }
    }
}
```
**Responsibility:** Persist orders to file  
**Benefit:** Clean resource management, configurable path

#### 7. **OrderProcessor.java** - Orchestrator
```java
public class OrderProcessor {
    private final TaxCalculator taxCalculator;
    private final ReceiptFormatter formatter;
    private final OrderRepository repository;
    
    public OrderProcessor(TaxCalculator taxCalculator, 
                         ReceiptFormatter formatter, 
                         OrderRepository repository) {
        this.taxCalculator = taxCalculator;
        this.formatter = formatter;
        this.repository = repository;
    }
    
    public void processOrder(String customerName, String coffeeType, double price) {
        Order order = new Order(customerName, coffeeType, price);
        
        double taxAmount = taxCalculator.calculateTax(order.getBasePrice());
        double taxRate = taxAmount / order.getBasePrice();
        order.applyTax(taxRate);
        
        String receipt = formatter.format(order);
        System.out.println(receipt);
        
        try {
            repository.save(order);
        } catch (Exception e) {
            System.out.println("[Repository ERROR] " + e.getMessage());
        }
    }
}
```
**Responsibility:** Coordinate the order processing workflow  
**Benefit:** Only orchestrates, does not implement logic

### Benefits of Clean Architecture

| Aspect | Naive | Clean |
|--------|-------|-------|
| **Coupling** | High | Low |
| **Cohesion** | Low | High |
| **Testability** | Poor | Excellent |
| **Extensibility** | Difficult | Easy |
| **Maintainability** | Low | High |
| **Reusability** | None | High |

## Design Patterns Applied

### 1. **Dependency Injection**
Dependencies are injected through the constructor, making the class testable.

### 2. **Strategy Pattern**
TaxCalculator interface allows different tax calculation strategies.

### 3. **Repository Pattern**
OrderRepository abstracts data persistence, allowing multiple implementations.

### 4. **Data Transfer Object (DTO)**
Order class encapsulates order data.

### 5. **Composition Over Inheritance**
Uses composition instead of inheritance hierarchies.

## SOLID Principles

### Single Responsibility Principle (SRP)
- Each class has ONE reason to change
- OrderProcessor only changes if workflow changes
- TaxCalculator only changes if tax rules change
- ReceiptFormatter only changes if format changes
- OrderRepository only changes if storage changes

### Open/Closed Principle (OCP)
- Classes are open for extension, closed for modification
- Add new tax calculators without modifying OrderProcessor
- Add new repositories without modifying OrderProcessor

### Liskov Substitution Principle (LSP)
- Implementations can be substituted for interfaces
- Any TaxCalculator implementation works with OrderProcessor

### Interface Segregation Principle (ISP)
- Interfaces are minimal and focused
- TaxCalculator has single method
- OrderRepository has single method

### Dependency Inversion Principle (DIP)
- Depend on abstractions, not implementations
- OrderProcessor depends on interfaces
- Easy to swap implementations

## Extensibility Examples

### Add New Tax Strategy
```java
public class ProgressiveTaxCalculator implements TaxCalculator {
    @Override
    public double calculateTax(double basePrice) {
        if (basePrice > 500) return basePrice * 0.15;
        if (basePrice > 200) return basePrice * 0.12;
        return basePrice * 0.10;
    }
}

// Use it
OrderProcessor processor = new OrderProcessor(
    new ProgressiveTaxCalculator(),
    new ReceiptFormatter(),
    new FileOrderRepository("orders.txt")
);
```

### Add New Storage Backend
```java
public class DatabaseRepository implements OrderRepository {
    @Override
    public void save(Order order) throws SQLException {
        // Database logic
    }
}

// Use it
OrderProcessor processor = new OrderProcessor(
    taxCalculator,
    formatter,
    new DatabaseRepository()
);
```

## Building and Running

### Prerequisites
- Java 8 or higher
- Apache Ant (for build.xml)

### Build
```bash
ant clean build
```

### Run the Clean Implementation
```bash
cd src
java com.coffeeshop.clean.Main
```

### Run the Naive Implementation
```bash
cd src
java com.coffeeshop.naive.Main
```

## Presentation

### Files
- `PRESENTATION_CONTENT.md` - Detailed presentation content
- `generate_presentation.py` - Python script to generate PPTX
- `generate_presentation.bat` - Batch file to run the generator
- `Coupling_and_Cohesion_Refactoring.pptx` - Generated presentation (if run)

### Generate Presentation

#### Option 1: Using Batch File (Windows)
```bash
generate_presentation.bat
```

#### Option 2: Using Python Script
```bash
# Install python-pptx
pip install python-pptx

# Generate presentation
python generate_presentation.py
```

#### Option 3: Manual Creation
Use `PRESENTATION_CONTENT.md` to manually create slides in PowerPoint, Google Slides, or LibreOffice Impress.

### Presentation Date
**July 20, 2026**

## Metrics

### Code Metrics
- **Classes (before):** 2
- **Classes (after):** 7+
- **Methods per class (before):** 3
- **Methods per class (after):** 1-2 average
- **Lines of code per responsibility:** Well-separated

### Quality Metrics
- **Testability:** Low → Very High
- **Maintainability:** Low → High
- **Extensibility:** Low → High
- **Coupling:** High → Low
- **Cohesion:** Low → High

## Testing

### Unit Test Opportunities
- `TaxCalculatorTest` - Test different tax rates
- `ReceiptFormatterTest` - Test receipt formatting
- `OrderRepositoryTest` - Test data persistence (with mocks)
- `OrderTest` - Test order properties
- `OrderProcessorTest` - Test workflow (with mocks)

### Example Test with Mocks
```java
@Test
public void testOrderProcessing() {
    TaxCalculator mockTax = mock(TaxCalculator.class);
    ReceiptFormatter mockFormatter = mock(ReceiptFormatter.class);
    OrderRepository mockRepo = mock(OrderRepository.class);
    
    OrderProcessor processor = new OrderProcessor(mockTax, mockFormatter, mockRepo);
    processor.processOrder("Juan", "Coffee", 150);
    
    verify(mockTax).calculateTax(150);
    verify(mockFormatter).format(any(Order.class));
    verify(mockRepo).save(any(Order.class));
}
```

## Key Learnings

1. **Identify Responsibilities Early** - Prevents mixing concerns
2. **Single Responsibility Principle is Fundamental** - Each class has one reason to change
3. **Dependency Injection Enables Testing** - Inject mocks for unit tests
4. **Interfaces Provide Flexibility** - Easy to add implementations
5. **Cohesive Classes are Easier to Understand** - Improved readability
6. **Clean Code is Not Extra Work** - Less work over time

## Team Members and Contributions

| Member | Contribution |
|--------|--------------|
| [Member 1] | 25% - Analysis & Design |
| [Member 2] | 35% - Implementation & Testing |
| [Member 3] | 20% - Documentation & Presentation |
| [Member 4] | 20% - Code Review & Refactoring |

**Total:** 100%

## Repository Information

**Assigned Repository:** [Your repository URL]  
**Submission Deadline:** July 20, 2026  
**Presentation Date:** July 20, 2026

## References

- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection)
- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)
- [Strategy Pattern](https://refactoring.guru/design-patterns/strategy)

## License

[Your License]

---

**Last Updated:** July 18, 2026  
**Project Status:** Ready for Presentation and Submission
