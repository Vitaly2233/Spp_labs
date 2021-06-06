#include <iostream>
#include<chrono>
#include <variant>
#include <vector>
#include <fstream>

using namespace std;

//void createNumberArray(int length) {
//	auto start = chrono::high_resolution_clock::now();
//	int* p_darr = new int[length];
//
//	for (int i = 0; i < length; i++) {
//		p_darr[i] = rand() % 100 + 1;
//	}
//
//	auto end = chrono::high_resolution_clock::now();
//	chrono::duration<float> duration = end - start;
//	cout << "����� ���������� ������ �����: " << duration.count() << endl;
//
//	delete[] p_darr;
//}
//
//void createFloatArray(int length, float start, float end) {
//	auto startTime = chrono::high_resolution_clock::now();
//	float* p_darr = new float[length];
//
//	for (int i = 0; i < length; i++) {
//		p_darr[i] = ((end - start) * ((float)rand() / RAND_MAX)) + start;
//	}
//
//	auto endTime = chrono::high_resolution_clock::now();
//	chrono::duration<float> duration = endTime - startTime;
//	cout << "����� ��������� ������ ����� � ��������� ������: " << duration.count() << endl;
//
//	delete[] p_darr;
//}
//
//void createSymbolArray(int length) {
//	auto startTime = chrono::high_resolution_clock::now();
//	float* p_darr = new float[length];
//
//	for (int i = 0; i < length; i++) {
//		p_darr[i] = char('a' + rand() % ('z' - 'a'));
//	}
//
//	auto endTime = chrono::high_resolution_clock::now();
//	chrono::duration<float> duration = endTime - startTime;
//	cout << "����� ��������� ������ ��������:" << duration.count() << endl;
//
//	delete[] p_darr;
//}

template <typename T>
T generate(int typeOfNumber) {
	if (typeOfNumber == 1) {
		int number = rand() % 100 + 1;
		cout << number << "\n";
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

	cout << "����� ���� ����� �������� � �������: 1) �����, 2) �������, 3) �������" << endl;
	int typeOfNumbers;
	cin >> typeOfNumbers;
	cout << "������� ���������� ���������";
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
	cout << "����� ��������� ������: " << duration.count() << endl;

	//adding result to the file
	ofstream fout;
	fout.open("E://Python/MetelapLaba/cppResult.txt", ofstream::app);

	fout << "����� ����������: " << duration.count() << "\t ��� ������: " << typeOfNumbers;

	fout.close();
}