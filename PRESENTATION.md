# Presentation: Coupling and Cohesion Refactoring

## Slide 1: Title
**Coffee Shop Order System Refactoring**
- Reducing Coupling, Increasing Cohesion
- July 20, 2026

---

## Slide 2: The Problem
**Original Design Issues**
- One OrderProcessor class doing 3 things:
  - Tax calculations
  - Receipt formatting
  - File I/O operations
- Result: Hard to test, modify, and extend

---

## Slide 3: Our Solution
**Separated Components**
- Order: Data model
- TaxCalculator: Tax logic
- ReceiptFormatter: Formatting
- OrderRepository: Persistence
- OrderProcessor: Orchestrator

---

## Slide 4: Code Comparison
**Before:** 30+ lines, mixed concerns
**After:** 7 classes, single responsibilities

Benefits:
- Easier to test
- Easier to modify
- Easier to extend

---

## Slide 5: Design Patterns
- Dependency Injection
- Strategy Pattern (tax calculation)
- Repository Pattern (storage)
- Single Responsibility Principle

---

## Slide 6: Results
- Coupling: High → Low
- Cohesion: Low → High
- Code Quality: Improved
- Testability: Much Better

---

## Slide 7: Team Members
- **Gilbert Fatiig** - 40%
- **Samo Dinnao** - 30%
- **Eirohnjan Balino** - 30%
