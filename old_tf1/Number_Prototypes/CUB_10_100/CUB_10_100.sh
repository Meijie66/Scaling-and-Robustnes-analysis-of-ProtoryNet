#!/bin/bash
#SBATCH --job-name=10_100
#SBATCH --time=1-20:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf/Number_Prototypes/CUB_10_100/10_100.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf/Number_Prototypes/CUB_10_100/10_100.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf/Number_Prototypes/CUB_10_100
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_10_100.py 