import concurrent.futures
import argparse

from typing import List
from src import word_frequency, check_pwd, circular_queue

def parse_args():
    parser = argparse.ArgumentParser(
                    prog='multi',
                    description='Call multiple scripts based on arguments',)
    
    parser.add_argument('--filename', dest='filename', type=str)
    return parser.parse_args()

def get_file_content(filename: str) -> List[str]:
    """
    Read data from file.
    returns: list of string of each line from file.
    """
    with open(filename, '+r') as fin:
        data = fin.readlines()
    return data

def run_func(filename, apply_func) -> any:
    """
    A helper function to read data from filename and feed to function apply_func
    """
    data = get_file_content(filename)
    for line in data:
        print(f'Running function: {apply_func.__name__}')
        apply_func(line.strip())

def __cq__(value: str) -> None:
    # helper function to enqueue and display queue to use in multi-thread
    cq = circular_queue.CircularQueue()
    cq.enqueue(value)
    cq.enqueue(value)
    cq.displayQueue()

    cq.dequeue()
    cq.displayQueue()

def main() -> None:
    options = parse_args()
    if options.filename: # read input from file
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exec:
            exec.submit(run_func(options.filename, word_frequency.print_words_freq))
            exec.submit(run_func(options.filename, check_pwd.print_pwds))
            exec.submit(run_func(options.filename, __cq__))
    else: # run scripts in src in parallel with some sample inputs
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exec:
            exec.submit(word_frequency.print_words_freq('This is a test test'))
            exec.submit(check_pwd.print_pwds('asAqwr1234@1,aF145#,2w3E*,@Favb#,9zMX*'))
            exec.submit(__cq__('a'))

if __name__ == '__main__':
    main()