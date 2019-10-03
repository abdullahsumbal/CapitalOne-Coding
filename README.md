# CapitalOne-Coding

This repo contains code to count simple line comments, block comments, lines of block comment and TODOs within comments. Link to the Technical Assessment can be found [here](www.abdullahsumbal.com/doc/capital-one.pdf)..

## Getting started

### Prerequisites

1. Install [anaconda](https://www.anaconda.com/distribution/).
2. step up python environment
    ```buildoutcfg
    conda create --name language-info python=3.6
    ``` 
3. activate environment
    ```buildoutcfg
    conda activate language-info
    or 
    source activate language-info
    ```

### Installation
There are no requirements for this project.

Note: In future, If there are any dependencies, Please them in the `requirements.txt` and use the following command to install.
```buildoutcfg
conda install -c conda-forge --file requirements.txt

or 

pip install -r requirements.txt

```
### Run Application 
The application takes in a configuration json file as argument. In this configuration file, you can define allowed language and their extensions and also a path to 
source code directory. There is a template configuration placed in the root folder called [template-config.json](template-config.json).If you do not provide any arguments, the 
program takes [template-config.json](template-config.json) as default configuration file. Please point the `source_directory` value in the configuration file to the desired source file directory.
Run the following command on terminal.
```buildoutcfg
python main.py
```

The following shows the `-h` output.

```buildoutcfg
$>python main.py -h
usage: main.py [-h] [-c CONFIG_PATH]

Count Comments

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_PATH, --config_path CONFIG_PATH
                        provide an config file (default: template-config.json)

```
### Program Architecture
The project uses the strategy design pattern. 
