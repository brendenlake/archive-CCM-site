# Obtaining the Homework

If you are using the university provided Jupyter instance ([here](https://dsgs-3001005.rcnyu.org/)) 
rather than your own personal computer the homeworks will automatically download into a folder in your account
called `course-materials` each time you login.

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
cp -r CCM-site/homeworks/1-NeuralNet .
```

(don't forget trailing `.`)
