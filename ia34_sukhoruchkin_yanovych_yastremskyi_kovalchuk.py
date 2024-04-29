import heapq
from io import TextIOWrapper
from loguru import logger
import sys

min_level = "INFO"

def min_level_filter(record):
    return record["level"].no >= logger.level(min_level).no

logger.remove()
logger.add(sys.stderr, format="[{time:HH:mm:ss.SSS} | <level>{level: <8}</level>] {message}", filter=min_level_filter)

def median_from_stream(nums):
    low, high = [], []
    medians = []
    
    for num in nums:
        if len(low) == 0 or num <= -low[0]:
            heapq.heappush(low, -num)
        else:
            heapq.heappush(high, num)
        
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
        
        if len(low) > len(high):
            medians.append(-low[0])
        elif len(low) == len(high):
            medians.append(f"{-low[0]} {high[0]}")
        else:
            medians.append(high[0])
    
    return medians

def file_reader(file: TextIOWrapper):
    lines = file.readlines()
    info = int(lines[0])
    arr = []
    if len(lines) != info+1:
        raise Exception("Invalid input was provided. The length of the array is not correct.") 
    for i in range(1,info+1):
        inputting = int(lines[i])
        if (inputting in arr):
            raise Exception("Invalid input was provided. Duplicates were found.") 
        arr.append(inputting)
    return arr

def output_text(o):
    s = ""
    for i in o:
        s += str(i) + "\n"
    return s

if __name__ == "__main__":
    logger.info("Starting to work..")
    inp = file_reader(open("./input.txt"))
    logger.debug("Working with median_from_stream..")
    out = median_from_stream(list(inp))
    logger.info("Finsihed working. Writing to file.")
    f = open("./output.txt", "w")
    f.write(output_text(out))
    f.close()