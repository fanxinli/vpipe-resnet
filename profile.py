import time
import pynvml as nvidia_smi
import sys
nvidia_smi.nvmlInit()

handles = []

deviceCount = nvidia_smi.nvmlDeviceGetCount()
for i in range(deviceCount):
    handle = nvidia_smi.nvmlDeviceGetHandleByIndex(i)
    print("GPU", i, ":", nvidia_smi.nvmlDeviceGetName(handle))

for i in range(deviceCount):
    handles.append(nvidia_smi.nvmlDeviceGetHandleByIndex(i))

with open(sys.argv[1], 'w') as f:
    for c in range(int(sys.argv[2])):
        usage = []
        mem = []
        for handle in handles:
            res = nvidia_smi.nvmlDeviceGetUtilizationRates(handle)
            mem_info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)

            usage.append(res.gpu)
            mem.append(mem_info.used)
        usage_str = ""
        mem_str = ""

        usage_str = ' '.join(["%.3f"%s for s in usage])
        mem_str = ' '.join(["%.3f"%s for s in mem])

        usage_output = "Usage [%.2f]: "%time.time()+usage_str
        mem_output = "Mem   [%.2f]: "%time.time() +mem_str

        print(usage_output)
        f.write(usage_output+"\n")

        print(mem_output)
        f.write(mem_output+"\n")

        time.sleep(float(sys.argv[3]))

nvidia_smi.nvmlShutdown()
