#include <iostream>
#include<chrono>
#include <variant>
#include <vector>
#include <fstream>

using namespace std;

template <typename T>
T generate(int typeOfNumber) {
	if (typeOfNumber == 1) {
		int number = rand() % 100 + 1;
		return number;
	}
	if (typeOfNumber == 2) {
		return ((0 - 1) * ((float)rand() / RAND_MAX)) + 1;
	}
	if (typeOfNumber == 3) {
		char character = char('a' + rand() % ('z' - 'a'));
		return character;
	}

}

int main() {
	setlocale(LC_ALL, "ru");
	srand(time(NULL));

	cout << "Введите пип елемнтов массива: 1) цифры, 2) числа с плавающей точкой, 3) символы" << endl;
	int typeOfNumbers;
	cin >> typeOfNumbers;
	cout << "Введите размерность массива";
	int length;
	cin >> length;
	// strting timer
	auto startTime = chrono::high_resolution_clock::now();
	if (typeOfNumbers == 1) {
		int* myArray = new int[length];
		for (int i = 0; i < length; i++)
		{
			myArray[i] = generate<int>(1);
		}
	}
	if (typeOfNumbers == 2) {
		int* myArray = new int[length];
		for (int i = 0; i < length; i++)
		{
			myArray[i] = generate<float>(2);
		}
	}
	if (typeOfNumbers == 3) {
		int* myArray = new int[length];
		for (int i = 0; i < length; i++)
		{
			myArray[i] = generate<char>(3);
		}
	}

	auto endTime = chrono::high_resolution_clock::now();
	chrono::duration<float> duration = endTime - startTime;
	cout << "Время заполнения массива: " << duration.count() << endl;

	//adding result to the file
	ofstream fout;
	fout.open("E://Python/MetelapLaba/cppResult.txt", ofstream::app);

	fout << "\nВремя заполнения массива: " << duration.count() << "\t тип елементов: " << typeOfNumbers;

	fout.close();
	cout << "\nВремя заполнения массива: " << duration.count() << "\t тип елементов: " << typeOfNumbers;
}