# Retrieving Homework from Github to Jupyter

Open a terminal in Jupyter


## Cloning the repository

For first retreival, clone the repository using

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
cp -r PATH/TO/HW
```

For example, for homework 1 you would type

```
cp -r CCM-site/homeworks/homework1-Jupyter:CA .
```

(don't forget trailing `.`)
