import datetime
import csv
import matplotlib.pyplot as plt


def plotter(dobY, dobM, dobD, filename, color, plot="date"):
    dob = datetime.datetime(dobY, dobM, dobD)

    data = {'age':[], 'height':[], 'date':[]}

    with open(filename, 'r') as file:
        csv_read = csv.reader(file)
        for row in csv_read:
            if row[0] != "Date":
                date = [int(f) for f in row[0].split("/")]
                date = datetime.datetime(2000+date[2], date[1], date[0])
                height = float(row[1])
                age = round(((date-dob).total_seconds())/(365*24*60*60), 2)
                data['age'].append(age)
                data['date'].append(date)
                data['height'].append(height)

    if plot=="date":
        plt.plot(data['date'], data['height'], marker='x', color=color)
    elif plot=="age":
        plt.plot(data['age'], data['height'], marker='x')

if __name__ == "__main__":
    plt.figure()
    plotter(1997, 10, 21, "jh_height.csv", 'b')
    plotter(1999, 6, 29, "fr_height.csv", 'g')
    plotter(2004, 8, 31, "jo_height.csv", 'r')
    plt.ylabel("Height (cm)")
    plt.xlabel("Year")
    plt.title("Height of my 2 brothers and I over time")
    plt.show()

    plt.figure()
    plotter(1997, 10, 21, "jh_height.csv", 'b', 'age')
    plotter(1999, 6, 29, "fr_height.csv", 'g', 'age')
    plotter(2004, 8, 31, "jo_height.csv", 'r', 'age')
    plt.ylabel("Height (cm)")
    plt.xlabel("Age")
    plt.title("Height of my 2 brothers and I with age")
    plt.show()

    plt.figure()
    plotter(1997, 10, 21, "jh_height.csv", 'b', 'age')
    plt.ylabel("Height (cm)")
    plt.xlabel("Age")
    plt.title("My height with age")
    plt.show()

    plt.figure()
    plotter(1999, 6, 29, "fr_height.csv", 'g', 'age')
    plotter(2004, 8, 31, "jo_height.csv", 'r', 'age')
    plt.ylabel("Height (cm)")
    plt.xlabel("Age")
    plt.title("The height of my two brothers with age")
    plt.show()
