// Libraries
#include <math.h>

// Konstanten
const long double GravitationalConstant = 6.6743e-11;

/*
    Anmerkung: Die hier verwendeten Variablen sind wie folgt zu verstehen:
    - jede Variable mit _1 am Ende ist die Zentral-Variable: für diese wird gerade die Positionsänderung berechnet
    - jede Variable mit _2 am Ende ist die other - Variable: mit diesem Objekt gibt es Wechselwirkungen
*/

// Struct zum Zurückgeben mehrerer Values
typedef struct Returner {
    double force_x;
    double force_y;
}
Returner;


// Funktionen
// Deklarationen
double distance_calculator(
        double x_1,  double x_2,
        double y_1,  double y_2);

struct Returner force_calculator(
        double distance_x, double distance_y,
        double mass_1, double mass_2,
        double distance);

// Definitionen
double distance_calculator(
        double x_1,  double x_2,
        double y_1,  double y_2)
{

    double distance_x = x_1 - x_2;
    double distance_y = y_1 - y_2;

    double distance;
    distance = sqrt(pow(distance_x, 2) + pow(distance_y, 2));

    return distance;
}

Returner force_calculator(
        double distance,
        double distance_x, double distance_y,
        double mass_1, double mass_2)
{

    Returner r1 = {0, 0};

    if (distance <= 0) return r1;

    double force = (GravitationalConstant * mass_1 * mass_2) / pow(distance, 2);
    double force_x, force_y, x_Einheitsvektor, y_Einheitsvektor;

    x_Einheitsvektor  = distance_x/distance;
    y_Einheitsvektor  = distance_y/distance;

    force_x = force * x_Einheitsvektor;
    force_y = force * y_Einheitsvektor;

    r1.force_x = force_x;
    r1.force_y = force_y;

    return r1;

}

double position_calculator(){
    return 0;
}

// Hauptlogik
int main()
{
return 0;

}




// alte Funktion zum Berechnen von Exponenten, <math.h> hat aber wohl schnellere Lösungen O(log n) statt O(n)
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
