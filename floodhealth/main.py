"""Main script for running tool using command-line"""


import sys

def main(input_path: str):
    """Main function to run the application when running via command-line

    Args:
        input_path (str): path to the input file
    """

    # Check
    print("Main was accessed succesfully! Nothing to do yet. Closing down.")

if __name__ == "__main__":
    main(sys.argv[0])