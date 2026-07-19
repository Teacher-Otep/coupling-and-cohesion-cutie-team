#!/usr/bin/env python3
"""
Generate PowerPoint presentation for Coupling and Cohesion Refactoring Project
This script creates a professional presentation documenting the refactoring work.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_title_slide(prs, title, subtitle):
    """Create a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    title_shape = slide.shapes.title
    subtitle_shape = slide.placeholders[1]
    
    title_shape.text = title
    subtitle_shape.text = subtitle
    
    # Format title
    title_frame = title_shape.text_frame
    title_frame.paragraphs[0].font.size = Pt(54)
    title_frame.paragraphs[0].font.bold = True
    title_frame.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)
    
    return slide

def create_bullet_slide(prs, title, bullets):
    """Create a slide with bullet points"""
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title_shape = slide.shapes.title
    content_shape = slide.placeholders[1]
    
    title_shape.text = title
    title_frame = title_shape.text_frame
    title_frame.paragraphs[0].font.size = Pt(44)
    title_frame.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)
    
    text_frame = content_shape.text_frame
    text_frame.clear()
    
    for bullet_text in bullets:
        p = text_frame.add_paragraph()
        p.text = bullet_text
        p.level = 0
        p.font.size = Pt(18)
    
    return slide

def create_two_column_slide(prs, title, left_title, left_bullets, right_title, right_bullets):
    """Create a slide with two columns"""
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    
    # Add title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = title
    title_frame.paragraphs[0].font.size = Pt(44)
    title_frame.paragraphs[0].font.bold = True
    title_frame.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)
    
    # Left column
    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(4.5), Inches(5))
    left_frame = left_box.text_frame
    left_frame.word_wrap = True
    
    left_title_p = left_frame.paragraphs[0]
    left_title_p.text = left_title
    left_title_p.font.size = Pt(24)
    left_title_p.font.bold = True
    left_title_p.font.color.rgb = RGBColor(51, 102, 153)
    
    for bullet in left_bullets:
        p = left_frame.add_paragraph()
        p.text = bullet
        p.font.size = Pt(16)
        p.level = 0
    
    # Right column
    right_box = slide.shapes.add_textbox(Inches(5.2), Inches(1.5), Inches(4.5), Inches(5))
    right_frame = right_box.text_frame
    right_frame.word_wrap = True
    
    right_title_p = right_frame.paragraphs[0]
    right_title_p.text = right_title
    right_title_p.font.size = Pt(24)
    right_title_p.font.bold = True
    right_title_p.font.color.rgb = RGBColor(51, 102, 153)
    
    for bullet in right_bullets:
        p = right_frame.add_paragraph()
        p.text = bullet
        p.font.size = Pt(16)
        p.level = 0
    
    return slide

def create_presentation():
    """Create the full presentation"""
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    
    # Slide 1: Title
    create_title_slide(prs, 
        "Coupling and Cohesion Refactoring",
        "Coffee Shop Order Processing System\nJuly 20, 2026"
    )
    
    # Slide 2: Project Overview
    create_bullet_slide(prs,
        "Project Overview",
        [
            "Refactored a tightly-coupled coffee shop ordering system",
            "Transformed from a monolithic design to a clean architecture",
            "Applied SOLID principles for better maintainability",
            "Reduced technical debt and improved code quality",
            "Increased testability and extensibility"
        ]
    )
    
    # Slide 3: Problem - Naive Implementation
    create_bullet_slide(prs,
        "Problem: Naive Implementation",
        [
            "Single OrderProcessor class with 3 mixed responsibilities:",
            "  • Tax calculations (Business Logic)",
            "  • Receipt formatting (Presentation)",
            "  • File I/O operations (Data Persistence)",
            "Hardcoded tax rate (12% VAT) - difficult to change",
            "Tightly coupled - difficult to test individual components",
            "High cohesion with wrong concerns - violates SRP"
        ]
    )
    
    # Slide 4: Solution - Clean Architecture
    create_two_column_slide(prs,
        "Solution: Clean Architecture Design",
        "Separated Concerns",
        [
            "TaxCalculator interface",
            "  - Handles tax logic",
            "ReceiptFormatter class",
            "  - Formats output",
            "OrderRepository interface",
            "  - Manages persistence",
            "Order data model",
            "  - Encapsulates order data"
        ],
        "Benefits Achieved",
        [
            "✓ Low Coupling",
            "  - Components independent",
            "✓ High Cohesion",
            "  - Each class has one job",
            "✓ SRP (Single Responsibility)",
            "  - Each class has one reason to change",
            "✓ DIP (Dependency Inversion)",
            "  - Depends on abstractions"
        ]
    )
    
    # Slide 5: Component Details
    create_bullet_slide(prs,
        "Key Components Refactored",
        [
            "Order: Immutable data model with tax calculation support",
            "TaxCalculator (interface): Abstraction for tax calculation logic",
            "DefaultTaxCalculator: Implements tax calculation with configurable rate",
            "ReceiptFormatter: Formats orders into readable receipt strings",
            "OrderRepository (interface): Abstraction for data storage",
            "FileOrderRepository: Implements file-based persistence with try-with-resources",
            "OrderProcessor: Orchestrates components using dependency injection"
        ]
    )
    
    # Slide 6: Code Improvements
    create_two_column_slide(prs,
        "Code Quality Improvements",
        "Coupling Reduction",
        [
            "Before: OrderProcessor knows about all details",
            "After: Dependencies injected via constructor",
            "Before: Hardcoded file paths",
            "After: Configurable through repository",
            "Before: Tightly coupled to tax logic",
            "After: Pluggable tax calculators"
        ],
        "Cohesion Increase",
        [
            "Tax logic isolated in TaxCalculator",
            "Formatting logic in ReceiptFormatter",
            "Persistence logic in OrderRepository",
            "Order data encapsulated in Order class",
            "Each class has single, clear purpose",
            "Each class is independently testable"
        ]
    )
    
    # Slide 7: Design Patterns Applied
    create_bullet_slide(prs,
        "Design Patterns Applied",
        [
            "Dependency Injection: Constructor injection of dependencies",
            "Strategy Pattern: TaxCalculator interface allows different tax strategies",
            "Repository Pattern: OrderRepository abstracts data storage",
            "Data Transfer Object: Order class encapsulates domain data",
            "Composition over Inheritance: Uses composition for flexibility",
            "Interface Segregation: Small, focused interfaces"
        ]
    )
    
    # Slide 8: Extensibility Example
    create_bullet_slide(prs,
        "Extensibility: Adding New Features is Easy",
        [
            "Add new tax calculator: Implement TaxCalculator interface",
            "Add new storage backend: Implement OrderRepository interface",
            "Add new receipt format: Create new ReceiptFormatter or add strategy",
            "Track discount logic: Add separate DiscountCalculator interface",
            "Add order validation: Create OrderValidator interface",
            "No changes needed to OrderProcessor!"
        ]
    )
    
    # Slide 9: Testing Benefits
    create_bullet_slide(prs,
        "Testing Improvements",
        [
            "Mock TaxCalculator for testing business logic",
            "Mock OrderRepository for testing without file I/O",
            "Mock ReceiptFormatter for testing output format",
            "Test tax calculations in isolation",
            "Test persistence separately from processing",
            "Unit tests are fast, simple, and focused"
        ]
    )
    
    # Slide 10: Metrics
    create_two_column_slide(prs,
        "Refactoring Metrics",
        "Code Organization",
        [
            "Classes before: 2 (naive + main)",
            "Classes after: 7+ components",
            "Methods per class: 1-2 avg (was 1)",
            "Cyclomatic complexity: Reduced",
            "Lines of code per responsibility: Clear separation",
            "Dependencies between classes: Minimal"
        ],
        "Quality Indicators",
        [
            "Testability: High → Very High",
            "Maintainability: Low → High",
            "Extensibility: Low → High",
            "Readability: Fair → Excellent",
            "Code duplication: Reduced",
            "Technical debt: Significantly reduced"
        ]
    )
    
    # Slide 11: Lessons Learned
    create_bullet_slide(prs,
        "Lessons Learned",
        [
            "Single Responsibility Principle is fundamental",
            "Dependency Injection enables loose coupling",
            "Interfaces provide extensibility without modification",
            "Cohesive classes are easier to test",
            "Clean architecture pays dividends over time",
            "Refactoring improves code quality continuously"
        ]
    )
    
    # Slide 12: Group Members and Contributions
    create_bullet_slide(prs,
        "Group Members and Contributions",
        [
            "Member 1: [Name] - Analysis & Design (25%)",
            "Member 2: [Name] - Implementation & Testing (35%)",
            "Member 3: [Name] - Documentation & Presentation (20%)",
            "Member 4: [Name] - Code Review & Refactoring (20%)",
            "",
            "Total contribution: 100%"
        ]
    )
    
    # Save presentation
    prs.save('Coupling_and_Cohesion_Refactoring.pptx')
    print("✓ Presentation created: Coupling_and_Cohesion_Refactoring.pptx")

if __name__ == "__main__":
    create_presentation()
