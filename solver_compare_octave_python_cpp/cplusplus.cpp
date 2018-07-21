#include <iostream>
#include <Eigen/Dense>
#include <Eigen/LU>
#include <chrono>

using namespace std;
using namespace Eigen;
using namespace std::chrono;

int main()
{
	unsigned size = 1E+3;

	time_point<system_clock,duration<double>> buildTimeStart = system_clock::now();
	MatrixXd matrix = MatrixXd::Random(size,size);
	MatrixXd independent = VectorXd::Random(size);
	time_point<system_clock,duration<double>> buildTimeEnd = system_clock::now();
	cout << "Build time: " << (buildTimeEnd - buildTimeStart).count() << " s" << endl;

	time_point<system_clock,duration<double>> solveTimeStart = system_clock::now();
	MatrixXd solution = matrix.lu().solve(independent);
	time_point<system_clock,duration<double>> solveTimeEnd = system_clock::now();
	cout << "Solve time: " << (solveTimeEnd - solveTimeStart).count() << " s" << endl;

	double error2 = (matrix*solution-independent).norm();
	double errorInfinity = (matrix*solution-independent).lpNorm<Infinity>();
	cout << "Norm 2: " << error2 << endl;
	cout << "Norm inf: " << errorInfinity << endl;
	return 0;
}
