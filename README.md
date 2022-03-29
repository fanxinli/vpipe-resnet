# ResNet-50

## Setup

1. Preprocess the ImageNet dataset and save it to `data`.

## Train



### Run on a host

#### 7-1 Configuration: two stages, first stage replicated with 7 GPU, second stage with 1 GPU

On the host, run the following commands in the `resnet` directory.
```bash
python -m launch --nnodes 1 --node_rank 0 --nproc_per_node 8 main_with_runtime.py --data_dir data --master_addr localhost --module gpus=8 --checkpoint_dir output --distributed_backend gloo -b 64 --lr 0.010000 --lr_policy polynomial --weight-decay 0.000500 --epochs 60 --print-freq 100 --num_ranks_in_server 8 --config_path gpus=8/hybrid_conf.json
```

#### 8 Configuration (DP): 1 stages, first stage replicated with 8 GPU

```bash
python -m launch --nnodes 1 --node_rank 0 --nproc_per_node 8 main_with_runtime.py --data_dir data --master_addr localhost --module gpus=8dp --checkpoint_dir output --distributed_backend gloo -b 64 --lr 0.010000 --lr_policy polynomial --weight-decay 0.000500 --epochs 60 --print-freq 100 --num_ranks_in_server 8 --config_path gpus=8dp/hybrid_conf.json
```

#### 8 Configuration (DP) with recompute: 1 stages, first stage replicated with 8 GPU

```bash
python -m launch --nnodes 1 --node_rank 0 --nproc_per_node 8 main_with_runtime.py --data_dir data --master_addr localhost --module gpus=8dprc --checkpoint_dir output --distributed_backend gloo -b 64 --lr 0.010000 --lr_policy polynomial --weight-decay 0.000500 --epochs 60 --print-freq 100 --num_ranks_in_server 8 --config_path gpus=8dprc/hybrid_conf.json
```