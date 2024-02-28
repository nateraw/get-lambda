import argparse
from lambdacloud import create_instance
from lambdacloud import login
import os
import time

def main(instance_type, file_system_names=None):
    sleep_time = 1
    login(token=os.getenv('LAMBDA_CLOUD_TOKEN'))

    while True:
        try:
            instance_id = create_instance(instance_type, ssh_key_names="lambda-new", file_system_names=file_system_names)
            print(f'Instance created with id: {instance_id}')
            break
        except:
            print(f'No {instance_type} found...sleeping for {sleep_time} seconds')
            time.sleep(sleep_time)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance_type", type=str, required=True, help="Instance type to be created.")
    parser.add_argument("--file_system_names", type=str, default=None, required=False, help="File system to attach.")
    args = parser.parse_args()
    main(args.instance_type)
