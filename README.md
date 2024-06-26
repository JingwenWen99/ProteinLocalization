# Citation
__Jing-Wen Wen__, Han-Lin Zhang, Pu-Feng Du*. Vislocas: Vision transformers for identifying protein subcellular mis-localization signatures of different cancer subtypes from immunohistochemistry images. _Computers in Biology and Medicine_ (2024). (In press)

# ProteinLocalization
In this work, we developed Vislocas, which identifies potential protein mis-localization events from IHC images, to mark different cancer subtypes. Vislocas combines CNN and vision transformer to capture IHC image features at both global and local levels. Vislocas can be trained from scratch to create an end-to-end system that can identify protein subcellular localizations directly from IHC images.
## 1. Platform and Dependency
### 1.1 Platform
* Ubuntu 9.4.0-1ubuntu1~20.04.1
* RTX 2080 Ti(11GB) * 6
### 1.2 Dependency
|Requirements|Release|
|----|----|
|CUDA|11.3|
|Python|3.8.15|
|pytorch|1.11.0|
|torchvision|0.12.0|
|torchaudio|0.11.0|
|cudatoolkit|11.3|
|pandas|1.2.4|
|fvcore|0.1.5|
|opencv-python|4.6.0.66|
|timm|0.6.12|
|scipy|1.9.3|
|einops|0.6.0|
|matplotlib|3.5.1|
|scikit-learn|1.1.2|
|tensorboard|2.11.0|
|adabelief-pytorch|0.2.0|
## 2. Project Catalog Structure
### 2.1 datasets
> This folder stores the code files for data loading.
* ihc.py
    > This file includes ihc data loading code.
* build.py
    > This file includes building dataset code.
* loader.py
    > This file includes constructing loader code.
### 2.2 prepareData
> This folder stores the code files for data preparing.
+ IF
  > This folder stores the code files used to analyse and process the IF labels. 
+ IHC
  > This folder stores the code files used to analyse, process and download the IHC data. 
+ pathology
  > This folder stores the code files used to analyse, process and download the pathology data. 
### 2.3 data
> Download and save the data annotation information to this folder.  
> All benchmark data has been deposited at Zenodo (<https://doi.org/10.5281/zenodo.10632698>) [![DOI](<https://zenodo.org/badge/DOI/10.5281/zenodo.10632698.svg>)](<https://doi.org/10.5281/zenodo.10632698>)

The following files should be placed directly in the `data` directory.  
|File|Descriptrion|
|----|----|
|data1.csv|The whole benchmark dataset|
|data_train.csv|The full training set|
|data_test.csv|The independent set|
|data_train_split<sub>i</sub>_fold<sub>j</sub>.csv|The training set for the jth-fold cross-validation of the i-th division|
|data_val_split<sub>i</sub>_fold<sub>j</sub>.csv|The validation set for the jth-fold cross-validation of the i-th division|
|data_IHC_analysis.csv|Data statistics for the benchmark data set|
|annotations.csv|Location annotation information for IF images|
|tissueUrl.csv|All normal IHC images and their URLs in the HPA database.|
|pathologyUrl.csv|All pathology IHC images and their URLs in the HPA database.|
|normalWithAnnotation.csv|IHC data information with matching IF labels|
|normalLabeled.csv|IHC data with labels|

The following files should be placed directly in the `data/cancer` directory.  
|File|Descriptrion|
|----|----|
|normalGlioma.csv|The normal data for glioma|
|patholotyGlioma.csv|The patholoty data for glioma|
|normalMelanoma.csv|The normal data for melanoma|
|patholotyMelanoma.csv|The patholoty data for melanoma|
|normalSkinCancer.csv|The normal data for skin cancer|
|patholotySkinCancer.csv|The patholoty data for skin cancer|
|screenedNormalData.csv|Normal data filtered to the same image quality as the benchmark dataset|
|screenedPathologyData.csv|Pathology tissue data filtered to the same image quality as the benchmark dataset|
### 2.4 models
> This folder stores model-related code files, including Visloacas model code, loss function code, and model training-related code.
  * cvr_utils
    > This folder stores convolutional tokenizer and transformer encoder module code.
  * cct.py
    > This file includes Visloacas model code.
  * classifier_model.py
    > This file includes load model code.
  * train_classifier.py
    > This file includes model training-related code.
  * loss.py
    > This file includes loss function code.
  * criterion.py
    > This file includes criterion-related code.
### 2.5 tools
> This folder stores code files for model training, prediction, biomarker prediction, etc.
* train.py
    > This file includes model training code.
* test.py
    > This file includes model testing code.
* multi-instance.py
    > This file includes the code that aggregates the image-level results into protein-level results.
* cancerTest.py
    > This file includes the codes for screening biomarkers of cancer subtypes.
* cal_metrics.py
    > This file includes the code that calculates the performance metrics.
### 2.6 utils
> This folder stores the optimiser, scheduler, checkpoint and other utilities code files.
* checkpoint.py
    > This file includes checkpoint code.
* config_defaults.py
    > This file includes the parameter configuration code.
* distributed.py
    > This file includes the code for distributed training.
* eval_metrics.py
    > This file includes the utilities code for calculating the performance metrics.
* optimizer.py
    > This file includes the optimizer code.
* scheduler.py
    > This file includes the scheduler code.
### 2.7 logs
> This folder is used to store the output log messages.
### 2.8 results
> This folder is used to store the output models and prediction results.
### 2.9 dataset
> This folder is used to store the downloaded images.
## 3. How to run
### 1. Download the data files to the data folder.
All benchmark data has been deposited at Zenodo (<https://doi.org/10.5281/zenodo.10632698>) [![DOI](<https://zenodo.org/badge/DOI/10.5281/zenodo.10632698.svg>)](<https://doi.org/10.5281/zenodo.10632698>)
### 2. Download the images from HPA. 
The download address of the images can be obtained from file `tissueUrl.csv` and `pathologyUrl.csv`.
### 3. Install the environment.
The program is written in Python 3.8.15 and to run the code we provide, so you need to install the `environment.yml` through inputting the following command in command line mode:<br>
`conda env create -f environment.yml`
### 4. Follow the steps below to generate the results of our paper.
1. Train the Vislocas model, and save trained model to `./results/IHC`.<br>
`sh train.sh`
3. Predict subcellular location results for each image, and save the results to `./results/IHC`.<br>
`sh test.sh`
3. Aggregates the image-level results into protein-level results and calculate the performance metrics of the model.<br>
`sh cal_metrics.sh`<br>
    > In the result files obtained, `statistic_crossValidation_Vislocas_mlce_lr-000005_bn_drop-01_attn-drop-01_drop-path-01_batch12_seed6293_wd-005_aug_no-normalized_metrics.csv` and `statistic_proteinLevel_crossValidation_Vislocas_mlce_lr-000005_bn_drop-01_attn-drop-01_drop-path-01_batch12_seed6293_wd-005_aug_no-normalized_metrics.csv` are the image level results and protein level results, respectively. 
4. Predict mis-localization-related cancer subtype biomarker, and save the results to `./results/cancer`.<br>
`sh cancerTest.sh `
