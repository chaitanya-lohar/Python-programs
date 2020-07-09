# example of exception handling
# try:
#     age=int(input("enter you age:"))
#     income=20000
#     risk=20000/age
#     print(age)
# except ZeroDivisionError:
#     print("Age can't be zero")
# except ValueError:
#     print("Age can't be string")
# --------------------------------------------------------------------------------------------------------------------
# a=int(input("enter first value:"))
# b=int(input("enter second value:"))
# try:
#     print(a/b)
#     c=int(input("enter any character:"))
# except Exception as e:
#     print(e)
# --------------------------------------------------------------------------------------------------------------------
# a,b=int(input("enter first value:")),int(input("enter second value:"))
# try:
#     print(a/b)
#     c=int(input("entere your age"))
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# finally:
#     print("inside of finally")

# if __name__ == '__main__':
#     print(__name__)
