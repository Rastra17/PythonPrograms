try:
    print("try will try to run this block if no errors are raised.")
except Exception as e:
    print("except <Exception> will run if the try block fails.")
else:
    print("else will run only when if there is no exception. Use else to run code if there is no exception.")
finally:
    print("finally will run regardless of any error or exception.")