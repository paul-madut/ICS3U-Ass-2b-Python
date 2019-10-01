#!/usr/bin//env python3

# Created by: Paul Madut
# Created on: September 2019
# This is the a program used to calculate area of a trapezoid


def main():
    # This functions calculates area
    # Input
    Base = int(input("Enter Base of rectangle (mm):"))
    Width = int(input("Enter Width of rectangle (mm):"))
    Height = int(input("Enter Height of trapezoid(mm)"))
    # Process
    Area = (Base + Width)/2*Height
    # Output
    print("")
    print("Area is {}mm²".format(Area))


if __name__ == "__main__":
    main()
