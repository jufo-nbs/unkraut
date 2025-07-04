import argparse

parser = argparse.ArgumentParser(prog = "main.py", 
                                 usage = "python main.py [-h] [--headless]", 
                                 description = "Intended to run on a Raspberry Pi 5 with AI-HAT and AI-Camera. It detects harmful plants and destroys them.", 
                                 epilog = "Program written for the 'Jugend Forscht'-Competition by Niklas Keim", 
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--headless', action='store_true')

args = parser.parse_args()
headless = args.headless
