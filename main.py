import InputFuncs as infunc
import OutputFuncs as outfunc
import CalculationFuncs as calcfunc

carSelections = infunc.CarSelect()

for car in carSelections:
    rpm, torque, ratio = infunc.ImportData(car)
    torquePoly = calcfunc.fitDyno(rpm, torque)
    outfunc.plotDyno(rpm,torque, torquePoly)