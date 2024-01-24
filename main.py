import concurrent.futures
import argparse

from src import word_frequency, check_pwd, circular_queue

def parse_args():
    parser = argparse.ArgumentParser(
                    prog='multi',
                    description='Call multiple scripts based on arguments',)
    
    parser.add_argument('--filename', dest='filename', type=str)
    args = parser.parse_args()

def cq():
    cq = circular_queue.CircularQueue()
    cq.enqueue('a')
    cq.enqueue('b')
    cq.displayQueue()

def main():
    # run scripts in src in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exec:
        exec.submit(word_frequency.print_words_freq('test is test'))
        exec.submit(check_pwd.print_pwds('asAqwr1234@1,aF145#,2w3E*,@Favb#,9zMX*'))
        exec.submit(cq())

if __name__ == '__main__':
    main()