#!/usr/bin/env python3
"""
Программа симулирует запросы БД, выводит max, min, и average значения
"""
import datetime
import time
import random


def stress_db():
    const_n = 10
    const_pause = 1
    list_of_result = []
    for i in range(const_n):
        date_now = datetime.date.today()
        time_now = datetime.datetime.today().strftime("%M:%S")
        n = random.randint(1, 100)
        time.sleep(const_pause)
        latency = f'{date_now}  [{time_now}] - latency = {n}'
        list_of_result.append(latency)
        print(latency)
    return list_of_result


def parse_stress_results(arr):
    list_of_result_latency = []
    for i in arr:
        element_of_latency = int(i.rpartition("=")[len(i.rpartition("=")) - 1])
        list_of_result_latency.append(element_of_latency)
    print(list_of_result_latency)
    return list_of_result_latency


def calculate_and_print_statics(arr):
    if len(arr) == 0:
        raise Exception(" Нет ни одного значения Latency ")
    max_value = max(arr)
    min_value = min(arr)
    average_value = 0
    for latency_value in arr:
        average_value = average_value + latency_value
    average_value = average_value / len(arr)
    print(f"Minimum latency: {min_value} ms\nMaximum Latency: {max_value} ms")
    print(f"Average latency: {int(average_value)} ms")


if __name__ == "__main__":
    list_of_results = stress_db()
    latencies = parse_stress_results(arr=list_of_results)
    calculate_and_print_statics(latencies)
