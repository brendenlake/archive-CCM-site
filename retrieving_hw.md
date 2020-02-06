# Obtaining the Homework

If you are using the university provided Jupyter instance ([here](https://dsgs-3001005.rcnyu.org/)) 
rather than your own personal computer the homeworks and other materials will automatically download into a folder in your account
called `class_materials/from_github` each time you login.

## Working on the files on the JupyterHub

The entire `class_materials` folder is read-only so that your work is not accidently overwritten.  Thus, you need to copy the files out of this folder to work on them.

For example, to work on the first homework you would need to copy the files from `class_materials/from_github/homeworks/homework-NeuralNet`.  To do this selected "New" and then "Terminal" from the file browser interface.  Then type
`cp -r class_materials/from_github/homeworks/homework-NeuralNet ./homework-NeuralNet`.  This will copy all the files into position.  You will need to change the folder name of the homework for other homeworks of course.

Then you can open them from the `homework-NeuralNet` (or whatever the name is) in the top directory of your JupyterHub instance.

**IMPORTANT**: When you use notebooks on the NYU Jupyterhub you need to change the default kernel of the notebook.  First open a notebook.  Then selected "Kernel" from the menu bar.  Then select "Change Kernel" and then select "Python \[conda env:cognition\]" from the list.  Otherwise your python environment may not have the necessary packages to do the homework.  In any case please always verify that the current notebook you are running says "Python \[conda env:cognition\]" in the upper right corner of the interface.

If you are running your own Jupyter instance use the following instructions to download
the homeworks.

# Retrieving Homework from Github to Jupyter

Open a terminal in Jupyter (Go to "new" in the upper right, then choose "terminal").


## Cloning the repository

For first retrieval, clone the repository using

```
git clone https://github.com/brendenlake/CCM-site.git
```

## Updating the repository


To update the repository, enter the repository folder using

```
cd CCM-site
```

and pull new commits using

```
git pull
```

## Creating a copy of a HW

To create a copy of a HW problem set to work on in the home folder (and prevent
possible merge conflicts on future pulls), run

```
cd ~
cp -r PATH/TO/HW .
```

For example, for homework 1 you would type

```
cp -r CCM-site/homeworks/homework-NeuralNet .
```

(don't forget trailing `.`)

## Packages

The following python packages are installed on the NYU Jupyterhub and so if you want to create a similar setup please install the following using your preferred pacakge manager (anaconda, pip, etc..).  The latest versions should be fine:

- pandas 
- wikipedia 
- colorlover 
- jupyter_contrib_nbextensions 
- matplotlib 
- pingouin
- scikit-learn 
- scikit-image
- ptitprince
- pomegranate
- hmmlearn
- nilearn
- gym 
- torch 
- torchvision
