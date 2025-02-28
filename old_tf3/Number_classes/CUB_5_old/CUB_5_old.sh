#!/bin/bash
#SBATCH --job-name=5_old_s3
#SBATCH --time=20:00:00
#SBATCH --mem=80GB
#SBATCH --error=/home/limei/ProtoryNet/old_tf3/Number_classes/CUB_5_old/5_s3.err
#SBATCH --output=/home/limei/ProtoryNet/old_tf3/Number_classes/CUB_5_old/5_s3.out
#SBATCH --partition=owner_fb12
#SBATCH --gpus=a100_80gb:1
source ~/.bashrc 
cd /home/limei/ProtoryNet/old_tf3/Number_classes/CUB_5_old
conda activate /home/limei/miniconda3/envs/old-tf
python3 CUB_5_old.py 