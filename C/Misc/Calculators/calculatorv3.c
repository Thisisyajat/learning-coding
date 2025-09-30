#include <stdio.h>
float addition(float a, float b);
float subtraction(float a, float b);
float multiplication(float a, float b);
float division(float a, float b);
void run();

char mode;
float ans, num1, num2;
int count = 1;

void main(){
    printf("Welcome to the calculator.");
    //count++;
    printf("\nEnter number %d --> ",count);
    scanf("\n%f",&num1);
    while ((getchar()) != '\n');
    printf("\nPlease select an operation:\n     - Addition (type 1)\n     - Subtraction (type 2)\n     - Multiplication (type 3)\n     - Division (type 4) \n     - Exit (type e)\n\nYour response --> ");
    scanf("%c",&mode);
    if (mode == 'e')
    {
        printf("\nBye bye...");
        return;
    }  
    count++;
    printf("Enter number %d --> ",count);
    scanf("%f",&num2);
    if (mode == '1')
    {
        printf("\nAnswer --> %f\n", addition(num1,num2));
    }
    else if (mode == '2')
    {
        printf("\nAnswer --> %f\n", subtraction(num1,num2));
    }
    else if (mode == '3')
    {
        printf("\nAnswer --> %f\n", multiplication(num1,num2));
    }
    else if (mode == '4')
    {
        printf("\nAnswer --> %f\n", division(num1,num2));
    }  
    else printf("Invalid input. Exiting.\n\n");
    run();
}

void run(){
    int run = 1;
    while (run)
    {
        while ((getchar()) != '\n');
        printf("\nPlease select an operation:\n     - Addition (type 1)\n     - Subtraction (type 2)\n     - Multiplication (type 3)\n     - Division (type 4) \n     - Exit (type e)\n\nYour response --> ");
        scanf("%c",&mode);
        if (mode == 'e')
        {
            printf("\nBye bye...");
            run = 0;
            return;
        }
        count++;
        num1 = ans;
        while ((getchar()) != '\n');
        printf("Enter number %d --> ",count);
        scanf("%f",&num2);
        if (mode == '1')
        {
            printf("\nAnswer --> %f\n", addition(num1,num2));
        }
        else if (mode == '2')
        {
            printf("\nAnswer --> %f\n", subtraction(num1,num2));
        }
        else if (mode == '3')
        {
            printf("\nAnswer --> %f\n", multiplication(num1,num2));
        }
        else if (mode == '4')
        {
            if (num2 == 0)
            {
                printf("Division by zero not possible!");
            }
            else printf("\nAnswer --> %f\n", division(num1,num2));
        }    
        else {
                printf("Invalid input. Exiting.\n\n");
                run = 0;
                return;
                //break;
        }
        }
}

float addition(float a, float b){
    ans = a + b;
    return ans;
}
float subtraction(float a, float b){
    ans = a - b;
    return ans;
}
float multiplication(float a, float b){
    ans = a * b;
    return ans;
}
float division(float a, float b){
    ans = a / b;
    return ans;
}


/*

IDEAL CODE BELOW:

#include <stdio.h> // Required for input/output functions
#include <stdlib.h> // Recommended for exit() if you decide to use it for hard exits

// Function prototypes - declare functions before they are used
float addition(float a, float b);
float subtraction(float a, float b);
float multiplication(float a, float b);
float division(float a, float b);
void run_calculator_loop(); // Renamed 'run' to be more descriptive and avoid potential conflicts

// Global variables - generally good practice to minimize global variables,
// but keeping them as per your original structure.
char mode;
float ans; // Stores the result of the previous operation, used as the first number for the next
float num1, num2; // Temporary variables for current operation's numbers
int count = 1; // Keeps track of the input number count

void clear_input_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

// Main function where the program execution begins
int main() {
    printf("Welcome to the calculator.\n");

    // --- First operation setup ---
    printf("Enter number %d --> ", count);
    if (scanf("%f", &num1) != 1) { // Check if scanf successfully read a float
        printf("Invalid number input. Exiting.\n");
        clear_input_buffer(); // Clear buffer in case of invalid input
        return 1; // Indicate an error
    }
    clear_input_buffer(); // Clear the newline character left by scanf("%f", ...)

    printf("\nPlease select an operation:\n");
    printf("    - Addition (type 1)\n");
    printf("    - Subtraction (type 2)\n");
    printf("    - Multiplication (type 3)\n");
    printf("    - Division (type 4)\n");
    printf("    - Exit (type e)\n\n");
    printf("Your response --> ");
    scanf("%c", &mode); // Read the operation character
    clear_input_buffer(); // Clear the newline character left by scanf("%c", ...)

    // --- Handle the first operation or exit condition ---
    if (mode == 'e' || mode == 'E') { // Check for exit immediately
        printf("\nBye bye...\n");
        return 0; // Exit the program directly from main
    } else if (mode < '1' || mode > '4') { // Check for invalid operation
        printf("Invalid input. Exiting.\n\n");
        return 0; // Exit the program directly from main
    }

    // If we reach here, a valid operation (1-4) was selected, so ask for the second number
    count++; // Increment count for the second number input
    printf("Enter number %d --> ", count);
    if (scanf("%f", &num2) != 1) { // Check if scanf successfully read a float
        printf("Invalid number input. Exiting.\n");
        clear_input_buffer();
        return 1; // Indicate an error
    }
    clear_input_buffer(); // Clear the newline character after num2

    // Perform the first calculation
    if (mode == '1') {
        ans = addition(num1, num2); // Store result in global 'ans'
        printf("\nAnswer --> %f\n", ans);
    } else if (mode == '2') {
        ans = subtraction(num1, num2);
        printf("\nAnswer --> %f\n", ans);
    } else if (mode == '3') {
        ans = multiplication(num1, num2);
        printf("\nAnswer --> %f\n", ans);
    } else if (mode == '4') {
        if (num2 == 0) { // Handle division by zero
            printf("Error: Division by zero is not allowed.\n");
            // Optionally, you could exit or restart this operation.
            // For now, we'll just print error and proceed to loop, keeping prev 'ans' or 0
            // If you want to exit on error: return 0;
        } else {
            ans = division(num1, num2);
            printf("\nAnswer --> %f\n", ans);
        }
    }

    // Now, enter the continuous calculator loop for subsequent operations
    run_calculator_loop();

    return 0; // Standard successful exit code for main
}

// Function to handle continuous calculator operations
void run_calculator_loop() {
    int continue_loop = 1; // Flag to control the while loop

    while (continue_loop) {
        printf("\nPlease select an operation:\n");
        printf("    - Addition (type 1)\n");
        printf("    - Subtraction (type 2)\n");
        printf("    - Multiplication (type 3)\n");
        printf("    - Division (type 4)\n");
        printf("    - Exit (type e)\n\n");
        printf("Your response --> ");

        scanf("%c", &mode); // Read the operation character
        clear_input_buffer(); // Clear the newline character

        if (mode == 'e' || mode == 'E') { // Check for exit condition
            printf("\nBye bye...\n");
            continue_loop = 0; // Set flag to exit the loop
        } else if (mode >= '1' && mode <= '4') { // Valid operation selected
            count++; // Increment count for the next number input
            num1 = ans; // The result of the previous operation becomes the first number for this new operation
            printf("Enter number %d --> ", count); // Prompt for the second number of this operation
            if (scanf("%f", &num2) != 1) { // Read the second number
                printf("Invalid number input. Exiting.\n");
                clear_input_buffer();
                continue_loop = 0; // Set flag to exit loop on invalid input
                continue; // Skip to next iteration to check continue_loop flag
            }
            clear_input_buffer(); // Clear the newline character

            // Perform the chosen operation
            if (mode == '1') {
                ans = addition(num1, num2);
                printf("\nAnswer --> %f\n", ans);
            } else if (mode == '2') {
                ans = subtraction(num1, num2);
                printf("\nAnswer --> %f\n", ans);
            } else if (mode == '3') {
                ans = multiplication(num1, num2);
                printf("\nAnswer --> %f\n", ans);
            } else if (mode == '4') {
                if (num2 == 0) { // Handle division by zero
                    printf("Error: Division by zero is not allowed.\n");
                    // 'ans' retains its previous value; loop continues, allowing new operation.
                } else {
                    ans = division(num1, num2);
                    printf("\nAnswer --> %f\n", ans);
                }
            }
        } else { // Invalid input for mode
            printf("Invalid input. Please choose 1, 2, 3, 4, or e.\n\n");
            // The loop will continue, allowing the user to re-enter a valid choice
        }
    } // End of while loop
}

// Function definitions for arithmetic operations
float addition(float a, float b) {
    return a + b;
}
float subtraction(float a, float b) {
    return a - b;
}
float multiplication(float a, float b) {
    return a * b;
}
float division(float a, float b) {
    return a / b;
}
*/