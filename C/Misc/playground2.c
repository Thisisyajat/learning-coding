#include <stdio.h>
#include <stdlib.h> // For exit() in a more robust way if needed, though break is fine

// Global variables for simplicity in this example, but consider passing values in larger projects
float current_result = 0.0; // Stores the ongoing calculation result
char mode; // Stores the chosen operation mode

// Function Prototypes (Declarations) - Parameters are added to make them more functional
float addition(float operand);
float subtraction(float operand);
float multiplication(float operand);
float division(float operand);
float get_number(const char* prompt_text); // Function to get a number with a custom prompt
void reset_calculator();

int main(){
    printf("Welcome to the calculator.\n");

    // Get the initial number to start the calculation
    current_result = get_number("Enter the first number --> ");

    while (1){
        // Consume any leftover newline character from previous scanf operations
        // This is important to prevent issues with scanf("%c")
        int c;
        while ((c = getchar()) != '\n' && c != EOF);

        printf("\nCurrent Answer: %.2f\n", current_result); // Display current result
        printf("\nPlease select an operation:\n");
        printf("    - Addition (type +)\n");
        printf("    - Subtraction (type -)\n");
        printf("    - Multiplication (type *)\n");
        printf("    - Division (type /)\n");
        printf("    - Reset answer (type r)\n");
        printf("    - Exit (type e)\n\n");
        printf("Your response --> ");
        scanf(" %c", &mode); // Space before %c to skip any leading whitespace including newlines

        float next_operand; // Variable to store the next number for calculation

        switch (mode) {
            case '+':
                next_operand = get_number("Enter number to add --> ");
                current_result = addition(next_operand);
                break;
            case '-':
                next_operand = get_number("Enter number to subtract --> ");
                current_result = subtraction(next_operand);
                break;
            case '*':
                next_operand = get_number("Enter number to multiply by --> ");
                current_result = multiplication(next_operand);
                break;
            case '/':
                next_operand = get_number("Enter number to divide by --> ");
                if (next_operand != 0) { // Crucial check for division by zero
                    current_result = division(next_operand);
                } else {
                    printf("Error: Cannot divide by zero!\n");
                }
                break;
            case 'r':
                reset_calculator();
                printf("Calculator reset. Please enter a new first number.\n");
                current_result = get_number("Enter the first number --> "); // Get new starting number
                break;
            case 'e':
                printf("\nExiting calculator. Goodbye!\n");
                return 0; // Exit the program
            default:
                printf("Invalid input. Please choose a valid operation.\n");
                break;
        }
    }

    return 0; // Should not be reached if 'e' is pressed
}

// Helper function to get a number from the user with a dynamic prompt
float get_number(const char* prompt_text){
    float num_input;
    printf("%s", prompt_text); // Use the provided prompt text
    // Loop until valid float input is received
    while (scanf("%f", &num_input) != 1) {
        printf("Invalid input. Please enter a number: ");
        // Clear invalid input from the buffer
        while (getchar() != '\n');
    }
    return num_input;
}

// Function to reset the calculator
void reset_calculator(){
    current_result = 0.0; // Reset the result
}

/*--------------------Operations-------------------*/

float addition(float operand){
    return current_result + operand;
}

float subtraction(float operand){
    return current_result - operand;
}

float multiplication(float operand){
    return current_result * operand;
}

float division(float operand){
    return current_result / operand;
}