# ResNet-50

## Setup

1. Preprocess the ImageNet dataset and save it to `data`.

## Train

### Run on a host

On the host, run the following commands in the `resnet` directory.
```bash
python -m launch --nnodes 1 --node_rank 0 --nproc_per_node 8 main_with_runtime.py --data_dir data --master_addr localhost --module gpus=8 --checkpoint_dir output --distributed_backend gloo -b 64 --lr 0.010000 --lr_policy polynomial --weight-decay 0.000500 --epochs 60 --print-freq 100 --verbose 100 --num_ranks_in_server 8 --config_path gpus=8/hybrid_conf.json
```