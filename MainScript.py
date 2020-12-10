import logging
import argparse


def parse_options():
    parser = argparse.ArgumentParser(description='This is a test project with a currently unknown purpose.')

    # parser.add_argument('base', help='folder of output to analyze ex: 2020-02-10.12.48.53')
    # parser.add_argument('--sum', action='store_true', help='flag to print summary')
    # parser.add_argument('--machine', default='mixr', help='configure to desktop, laptop, or mixr')
    parser.add_argument('-vb', '--verbose', action='store_true', default=False,
                        help='turn on verbose logs for debugging')
    ret_args = parser.parse_args()

    log_fmt = '%(asctime)s LINE:%(lineno)d LEVEL:%(levelname)s %(message)s'
    if ret_args.verbose:
        logging.basicConfig(level=logging.DEBUG, format=log_fmt)
    else:
        logging.basicConfig(level=logging.INFO, format=log_fmt)

    return ret_args


def main():
    parse_options()
    logging.info('This is the main function.')


if __name__ == '__main__':
    main()
