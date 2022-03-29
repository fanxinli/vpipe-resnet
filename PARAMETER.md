### launch.py parameters

--nnodes, The number of nodes to use for distributed training

--node_rank, The rank of the node for multi-node distributed training

--nproc_per_node,  The number of processes to launch on each node for GPU training, this is recommended to be set to the number of GPUs in your system so that each process can be bound to a single GPU.

### main_with_runtimes.py parameters

#### algorithm parameters
--data_dir,  path to dataset

--distributed_backend, distributed backend to use (gloo|nccl)

--module, name of module that contains model and tensor_shapes definition

-j, number of data loading workers (default: 4)

--epochs, number of total epochs to run

--start-epoch, manual epoch number (useful on restarts)

-b, --batch-size,  mini-batch size (default: 256)

--eval-batch-size, eval mini-batch size (default: 100)

--lr, --learning-rate, initial learning rate

--momentum, momentum

--weight-decay, --wd, weight decay (default: 1e-4)

--no-weight-stash, 

--print-freq, -p, print frequency (default: 10)

--fp16, train model in fp16 precision

--checkpoint_dir, path to directory to save checkpoints

--num_ranks_in_server, number of gpus per machine

#### distirbuted parameters


--master_addr, IP address of master (machine with rank 0)

--config_path, Path of configuration file

--rank RANK, Rank of worker

--local_rank, Local rank of worker

