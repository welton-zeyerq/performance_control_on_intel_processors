#!/usr/bin/env python3.11
import os
import sys

def help_use():
    print("follow the examples: ")
    print("")
    print("%s powersave"%(sys.argv[0]))
    print("%s balanced"%(sys.argv[0]))
    print("%s performance"%(sys.argv[0]))
    print("%s extreme"%(sys.argv[0]))

if len(sys.argv) !=2:
    help_use()
    sys.exit()

#/sys/devices/system/cpu/intel_pstate/status
#active = powersave
#passive = schedutil


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

    elif choice == "balanced":
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

    elif choice == "performance":
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

    elif choice == "extreme":
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

    else:
        print("ERROR, NO OPTION OR DIGITATION ERROR")

except Exception as error:
    print(error)
#    pass
except IOError as e:
    print(e)
#    pass
except KeyboardInterrupt:
    sys.exit()

