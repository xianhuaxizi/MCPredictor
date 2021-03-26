"""Arguments."""
import argparse


def parse_args():
    """Parse input arguments."""
    # Load config files
    parser = argparse.ArgumentParser(prog="SentEventPrediction")
    # Set basic arguments
    parser.add_argument("--data_dir", default="/data/users/bl/data/gandc16",
                        type=str, help="MCNC corpus directory")
    parser.add_argument("--work_dir", default="/data/users/bl/work_tmp",
                        type=str, help="Workspace directory")
    parser.add_argument("--device", default="cuda:0",
                        choices=["cpu", "cuda:0", "cuda:1", "cuda:2", "cuda:3"],
                        help="Device used for models.")
    parser.add_argument("--mode", default="preprocess",
                        choices=["preprocess", "train", "dev", "test"],
                        type=str, help="Experiment mode")
    parser.add_argument("--model_config", default="",
                        type=str, help="Model configuration files")
    # Set model arguments
    return parser.parse_args()


CONFIG = parse_args()
