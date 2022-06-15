#!/usr/bin/env python

from m3u_parser import M3uParser
import argparse


parser = argparse.ArgumentParser(description='a simple m3u > json parser in python')
parser.add_argument('-f', '--file', help='Description for foo argument', required=True)
args = parser.parse_args()

#  `args` will be a dictionary containing the arguments:

url = args.file 
useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36" 
parser = M3uParser(timeout=5, useragent=useragent)
parser.parse_m3u(url)

print(len(parser.get_list()))
parser.to_file('data.json')
