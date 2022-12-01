#!/usr/bin/env python3.11
import os
import sys

#author: welton-zeyerq
#https://github.com/welton-zeyerq/

def help_use():
    print("follow the examples: ")
    print("")
    print("%s powersave"%(sys.argv[0]))
    print("%s balanced"%(sys.argv[0]))
    print("%s performance"%(sys.argv[0]))
    print("%s extreme"%(sys.argv[0]))
    print("")
    print("compatible with intel 2, 4, 6, 8, 12 or 16 cores")

if len(sys.argv) !=2:
    help_use()
    sys.exit()

#/sys/devices/system/cpu/intel_pstate/status
#active = powersave
#passive = schedutil
#/sys/devices/system/cpu/online

with open("/sys/devices/system/cpu/online", "r") as file:
    online = file.readlines()
    for o in online:
        o = o.replace('\n', '')
#        print(o)
        if o == '0-1':
            print("dual core detected")
        elif o == '0-3':
            print("quad core detected")
        elif o == '0-5':
            print("six core detected")
        elif o == '0-7':
            print("octa core detected")
        elif o == '0-11':
            print("12 cores detected")
        elif o == '0-15':
            print("16 cores detected")
        else:
            print("not support cpu")

with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq", "r") as file:
    maxfreq = file.readlines()
    for maxf in maxfreq:
        maxf = maxf.replace('\n', '')
#        print(maxf)

with open("/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_min_freq", "r") as file:
    minfreq = file.readlines()
    for minf in minfreq:
        minf = minf.replace('\n', '')
#        print(minf)

b_freq = int(maxf) - int(minf)
#print(b_freq)

try:
    choice = str(sys.argv[1])
    if choice == "powersave":
        print("set powersave mode")
        if o == '0-1':
            perfsave = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 50 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                        """)
            os.system(perfsave)

        elif o == '0-3':
            perfsave = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 50 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                        """)
            os.system(perfsave)

        elif o == '0-5':
            perfsave = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 50 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                        """)
            os.system(perfsave)

        elif o == '0-7':
            perfsave = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 50 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                        """)
            os.system(perfsave)

        elif o == '0-11':
            perfsave = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu10cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu11cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 50 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                        """)
            os.system(perfsave)

        elif o == '0-15':
            perfsave = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu12/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu13/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu14/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu15/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu12/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu13/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu14/cpufreq/scaling_max_freq;
printf {minf} >/sys/devices/system/cpu/cpu15/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 50 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                        """)
            os.system(perfsave)

        else:
            print("not 2, 4, 6, 8, 12 or 16 cores, please contact support")

    elif choice == "balanced":
        print("set balanced mode")
        if o == '0-1':
            perfb = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 60 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                        """)
            os.system(perfsave)

        elif o == '0-3':
            perfb = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 60 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfb)

        elif o == '0-5':
            perfb = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 60 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfb)

        elif o == '0-7':
            perfb = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 60 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfb)

        elif o == '0-11':
            perfb = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 60 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfb)

        elif o == '0-15':
            perfb = (f"""
printf {minf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu12/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu13/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu14/cpufreq/scaling_min_freq;
printf {minf} >/sys/devices/system/cpu/cpu15/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu12/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu13/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu14/cpufreq/scaling_max_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu15/cpufreq/scaling_max_freq;
printf active >/sys/devices/system/cpu/intel_pstate/status;
printf 30 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 60 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfb)

        else:
            print("not 2, 4, 6, 8, 12 or 16 cores, please contact support")

    elif choice == "performance":
        print("set performance mode")
        if o == '0-1':
            perfpf = (f"""
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 50 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                  """)
            os.system(perfpf)

        elif o == '0-3':
            perfpf = (f"""
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 50 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                  """)
            os.system(perfpf)

        elif o == '0-5':
            perfpf = (f"""
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 50 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                  """)
            os.system(perfpf)

        elif o == '0-7':
            perfpf = (f"""
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 50 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                  """)
            os.system(perfpf)

        elif o == '0-11':
            perfpf = (f"""
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 50 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                  """)
            os.system(perfpf)

        elif o == '0-15':
            perfpf = (f"""
printf {b_freq} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu12/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu13/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu14/cpufreq/scaling_min_freq;
printf {b_freq} >/sys/devices/system/cpu/cpu15/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu12/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu13/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu14/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu15/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 50 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                  """)
            os.system(perfpf)

        else:
            print("not 2, 4, 6, 8, 12 or 16 cores, please contact support")

    elif choice == "extreme":
        print("set extreme mode")
        if o == '0-1':
            perfext = (f"""
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 90 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                  """)
            os.system(perfext)

        elif o == '0-3':
            perfext = (f"""
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 90 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfext)

        elif o == '0-5':
            perfext = (f"""
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 90 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfext)

        elif o == '0-7':
            perfext = (f"""
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 90 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfext)

        elif o == '0-11':
            perfext = (f"""
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 90 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfext)

        elif o == '0-15':
            perfext = (f"""
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu12/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu13/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu14/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu15/cpufreq/scaling_min_freq;
printf {maxf} >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu8/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu9/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu10/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu11/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu12/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu13/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu14/cpufreq/scaling_max_freq;
printf {maxf} >/sys/devices/system/cpu/cpu15/cpufreq/scaling_max_freq;
printf passive >/sys/devices/system/cpu/intel_pstate/status;
printf 90 >/sys/devices/system/cpu/intel_pstate/min_perf_pct;
printf 100 >/sys/devices/system/cpu/intel_pstate/max_perf_pct;
                      """)
            os.system(perfext)

        else:
            print("not 2, 4, 6, 8, 12 or 16 cores, please contact support")

    else:
        print("")
        print("ERROR, NO OPTION OR DIGITATION ERROR")

except Exception as error:
    print(error)
#    pass
except IOError as e:
    print(e)
#    pass
except KeyboardInterrupt:
    sys.exit()

