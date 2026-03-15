import logging
import argparse
from analytics_worker import config
from analytics_worker.worker import AnalyticsWorker

def parse_args():
    parser = argparse.ArgumentParser(description='Analytics Worker')
    parser.add_argument('--config', help='Path to configuration file', default='config.yml')
    return parser.parse_args()

def main():
    args = parse_args()
    logging.basicConfig(level=logging.INFO)
    worker = AnalyticsWorker(config.load_config(args.config))
    worker.start()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f'Error: {str(e)}')
        raise