year = int(input("Please enter the year that you want to calculate the personal interest rate for:"))
CategoriesNum = int(input("Please enter the number of expenditure categories: "))

if CategoriesNum > 0:

    PreYear_list = []
    IntYear_list = []

    i = 0
    for i in range(i, CategoriesNum):
        PreYear = int(input("Please enter expenses for previous year:"))
        IntYear = int(input("Please enter expenses for year of interest:"))
        PreYear_list.append(PreYear)
        IntYear_list.append(IntYear)
        i =+ 1

    PreYear_Total = sum(PreYear_list)
    IntYear_Total = sum(IntYear_list)

    Inflation = ((IntYear_Total - PreYear_Total)/IntYear_Total) * 100

    if Inflation < 3:
        InflationType = "Low"
    elif Inflation < 5:
        InflationType = "Moderate"
    elif Inflation < 10:
        InflationType = "High"
    elif Inflation > 10:
        InflationType = "Hyper"

    print("Personal inflation rate for {} is {}%".format(year, Inflation))
    print("Type of Inflation: {}".format(InflationType))

else:
    print("The number of Expenditure categories has to be greater than 0.")
