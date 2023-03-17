#!/usr/bin/env python3
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import GoogleImageCrawler
import argparse

VER = "v1.0"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def init_args_parser(description="\nImages Dataset Builder\n"):

    example="""
Example:
  python main.py -s \"Human Faces\", \"Roads\"\n 
"""
    parser = argparse.ArgumentParser(description=description, epilog=example, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-s", "--search", nargs="+", required=True, help='Classes to search (e.g ["Human Faces", "Roads"])')
    parser.add_argument("-n", "--number", required=False, help="Number of element to search per class")
    parser.add_argument("-o", "--output", required=False, help="Output folder path")
    parser.add_argument("-d", "--dispatch", action=argparse.BooleanOptionalAction, required=False, help="For each class, output in a different folder")

    args = parser.parse_args()
    return args




if __name__ == '__main__':

    description=f"""
Images Dataset Builder {VER}
https://github.com/danglock/Images-Dataset-Builder/
By @danglock
"""
    args = init_args_parser(description=description)

    print(description)

    classes=args.search
    number=args.number
    output=args.output

    if number is None:
        print(f"{bcolors.WARNING}No number selected. Default set to 100.{bcolors.ENDC}")
        number = 100
    else:
        number = int(args.number)

    


    # Set output Folder
    if output is None:
        print(f"[*] Output Folder:    {bcolors.WARNING}./Output/{bcolors.ENDC}")
        output = "./Output/"
    else:
        print(f"Output: {output}")



    # Select the navigator !! TO IMPROVE
    t = "Bing" # test var
    if t == "Bing":
        crawler = BingImageCrawler
    elif t == "Google":
        crawler = GoogleImageCrawler

    print(f"[*] Crawler Selected: {bcolors.WARNING}{t}{bcolors.ENDC}")



    # crawl images
    print(f"\nSearching {bcolors.WARNING}{number}{bcolors.ENDC} element(s) for {bcolors.WARNING}{classes}{bcolors.ENDC}...\n")
    if args.dispatch:
        print("Dispatching classes")
        for c in classes:
            selected_crawler=crawler(storage={'root_dir':f'{output}/{c.replace(" ",".")}'})
            selected_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)
    else:
        ####### Can be improved
        selected_crawler=crawler(storage={'root_dir':f'{output}/'})
        for c in classes:
            selected_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)


    print(f"\n{bcolors.WARNING}finished !{bcolors.ENDC}\n")


