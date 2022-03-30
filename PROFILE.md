profile.py 

### Install 

```bash
pip install nvidia-ml-py
```

### Usage

```bash
python profile.py [output_file] [number_of_prints] [time_sleep_between_each_print(in seconds)]
```

Example: print usage and memory of all GPUs in one host, by 1000 times and with 0.1s sleep.

```bash
python profile.py profile 1000 0.1
```