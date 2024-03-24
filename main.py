import sys
from test.run_all_tests import run_all_tests
from model.exchange import Exchange
from controller.run_exchange import run_exchange

def main():
    args = sys.argv[1:]
    if len(args) == 1 and (args[0] == "--test" or args[0] == "-t"):  
        run_all_tests()
    
    if len(args) == 1 and (args[0] == "--help" or args[0] == "-h"):
        print("Usage: python main.py [options]")
        print("Options:")
        print("  -t, --test    Run all tests")
        print("  -h, --help    Show this help message and exit")
        return

    # exchange = Exchange()
    # run_exchange(exchange)
    
if __name__ == "__main__":
    main()