#Temprature Converter
# a program to convert Celsius To Farenhite
#by-Vishal Yadav

def main():
    celsius=eval(input("Enter Celsius Value"))
    faren=(9/5)*celsius+32
    print("The Temprature is",faren,"Degrees Fahrenheit")

    
'''Eval() will alllow float values to be as input,if int() used will show error  when input is in decimals'''
