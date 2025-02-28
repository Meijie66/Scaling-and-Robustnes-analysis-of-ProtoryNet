#!/bin/bash
#SBATCH --job-name=10_random
#SBATCH --time=20:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf2/Cluster_init/10_class/10_random2.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf2/Cluster_init/10_class/10_random2.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf2/Cluster_init/10_class
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_10_old_random.py 