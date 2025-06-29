// Libraries
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

/*
    Anmerkung: Die hier verwendeten Variablen sind wie folgt zu verstehen:
    - jede Variable mit _1 am Ende ist die Zentral-Variable: für diese wird gerade die Positionsänderung berechnet
    - jede Variable mit _2 am Ende ist die other - Variable: mit diesem Objekt gibt es Wechselwirkungen
*/

// Struct zum Zurückgeben mehrerer Values
typedef struct Returner {
    double variable_x;
    double variable_y;
} Returner;

typedef struct MovingObject {
    double x, y;
    double v_x, v_y;
    double masse;
    bool is_planet; // bool möglich
} MovingObject;


// Konstanten
const long double GravitationalConstant = 6.6743e-11;


// Python -> C

// globale Variablen für laden der objekte
MovingObject* objects;
int current_object = 0;
int number_objects;
double delta_Time;

void init_objects(int number_objects_from_Python, double delta_Time_from_Python){
    number_objects = number_objects_from_Python;
    delta_Time = delta_Time_from_Python;

    if (objects != NULL){
        free(objects);
    }
    objects = calloc(number_objects, sizeof(MovingObject));
    current_object = 0;
}

void import_objects(
    double x, double y,
    double v_x, double v_y,
    double masse,
    bool is_planet){

    if(current_object < number_objects){
        objects[current_object].x = x;
        objects[current_object].y = y;
        objects[current_object].v_x = v_x;
        objects[current_object].v_y = v_y;
        objects[current_object].masse = masse;
        objects[current_object].is_planet = is_planet;

        current_object++;
    }
}

void position_calculator(double delta_Time); // muss hier sein, damit danach export_objects nicht weinen muss

void export_objects(
        int n,
        double* x, double* y,
        double* v_x, double* v_y){

    *x = objects[n].x;
    *y = objects[n].y;
    *v_x = objects[n].v_x;
    *v_y = objects[n].v_y;
}



// Funktionen
// Deklarationen
/*double distance_calculator(
        double x_1, double x_2,
        double y_1, double y_2);
*/

struct Returner force_calculator(
        double distance_x,  double distance_y,
        double mass_1, double mass_2,
        double distance);

void velocity_calculator(int i, double delta_Time);



// Definitionen
/*double distance_calculator(
        double x_1,  double x_2,
        double y_1,  double y_2){

    double distance_x = x_1 - x_2;
    double distance_y = y_1 - y_2;

    double distance;
    distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));

    return distance;
}*/


struct Returner force_calculator(
        double distance_x, double distance_y,
        double mass_1, double mass_2,
        double distance){

    // Am Anfang werden die Forces auf 0 gesetzt, beim Berechnen dann aber geändert
    struct Returner forces_1 = {0, 0};
    double force = 0;

    // Ab hier sollte der Loop hin
    if (distance <= 0){
        force = 0;
    }

    else{
        force = (GravitationalConstant * mass_1 * mass_2) / pow(distance, 2);
        double force_x, force_y, x_Einheitsvektor, y_Einheitsvektor;

        x_Einheitsvektor  = distance_x/distance;
        y_Einheitsvektor  = distance_y/distance;

        // Berechnen der Kraftwerte
        force_x = force * x_Einheitsvektor;
        force_y = force * y_Einheitsvektor;

        // Speichern der Werte in forces_1, damit sie danach zurückgegeben werden können
        forces_1.variable_x = force_x;
        forces_1.variable_y = force_y;
    }

    return forces_1;

}


void velocity_calculator(
        int i,
        double delta_Time){

    double force_x_total = 0;
    double force_y_total = 0;
    struct Returner forces_1;

    double mass_1;
    double mass_2;

    for(int j = 0; j < number_objects; j++){
            if(i == j){
                continue;
            }

            mass_1 = objects[i].masse;
            mass_2 = objects[j].masse;

            // Es muss hier j - i sein, damit (Einheits-) Vektor in Richtung des j - Objekts zeigt
            // Wenn z.B. j > i, dann muss der Vektor in Richtung j zeigen, also ebenfalls in positive Richtung
            // Sonst einfach umgekehrt, wenn j < i
            // Im Endeffekt fragt man nur, wer von beiden größer ist, es soll schließlich immer in Richtung J sein
            double distance_x = objects[j].x - objects[i].x;
            double distance_y = objects[j].y - objects[i].y;

            double distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));

            forces_1 = force_calculator(distance_x, distance_y, mass_1, mass_2, distance);

            force_x_total =  force_x_total + forces_1.variable_x;
            force_y_total =  force_y_total + forces_1.variable_y;
    }

    // hier soll das Programm erst hin, wenn alle Kräfte für das Objekt berechnet wurden

    double acceleration_1_x, acceleration_1_y;

    acceleration_1_x = force_x_total / mass_1;
    acceleration_1_y = force_y_total / mass_1;

    double v_x_neu = objects[i].v_x + acceleration_1_x * delta_Time;
    double v_y_neu = objects[i].v_y + acceleration_1_y * delta_Time;

    objects[i].v_x = v_x_neu;
    objects[i].v_y = v_y_neu;
}

void position_calculator(double delta_Time){

    for(int i = 0; i < number_objects; i++){
        velocity_calculator(i, delta_Time);

        double x_neu;
        double y_neu;

        x_neu = objects[i].x + objects[i].v_x * delta_Time;
        y_neu = objects[i].y + objects[i].v_y * delta_Time;

        objects[i].x = x_neu;
        objects[i].y = y_neu;
    }

}

int main(){
    return 0;
}




// alte Funktion zum Berechnen von Exponenten, <math.h> hat aber wohl schnellere Lösungen O(log n) statt O(n) von mir
/*double power(double number, int exponent) {
    if (exponent == 0) {
        return 1;
    }

     double result = 1;

    for (int i = 0; i < exponent; i++) {
        result = result * number;
    }
    return result;
}
*/
