from behave.__main__ import main as behave_main
def main():
   behave_main('features --no-capture --no-capture-stderr')
if __name__ == "__main__":
   main()