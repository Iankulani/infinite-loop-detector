# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:39:25 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Infinite Loop Detector")
print(Fore.GREEN+font)

import re

def detect_infinite_loops(java_code):
    # Regular expression patterns for loop constructs
    loop_patterns = [
        r"\bfor\s*\(.*;\s*;\s*\)",       # for loop with no condition
        r"\bwhile\s*\(.*;\s*\)",         # while loop with no condition
        r"\bwhile\s*\(.*\s*==\s*.*\)",   # while loop with constant condition
        r"\bfor\s*\(.*\s*==\s*.*\)",     # for loop with constant condition
        r"\bdo\s*{[^}]*}\s*\bwhile\s*\(.*\s*==\s*.*\);"  # do-while loop with constant condition
    ]
    
    # Check for common infinite loop patterns
    infinite_loops = []
    for pattern in loop_patterns:
        matches = re.findall(pattern, java_code)
        if matches:
            infinite_loops.extend(matches)

    return infinite_loops


def main():
    java_code = input("Enter Java code:")
    
    # Analyze the code
    suspicious_loops = detect_infinite_loops(java_code)
    
    if suspicious_loops:
        print("\nWarning: Possible infinite loops detected!")
        for loop in suspicious_loops:
            print(f"Suspicious loop pattern detected: {loop}")
    else:
        print("\nNo obvious infinite loops detected.")

if __name__ == "__main__":
    main()
