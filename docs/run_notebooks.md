# How to run the example notebooks
Here is a step by step guide to running and/or edit and re-running the example [Jupyter](https://jupyter.org/) notebooks.

- Install Docker on your computer. https://docs.docker.com/get-docker/
- Open a terminal window and paste the following
```shell
docker run -p 8888:8888 ghcr.io/davidpratten/jetisu:latest
```
- Click on the link provided which will look like this:
```shell
http://127.0.0.1:8888/lab?token=98c394671e0c8109980ad1467e6ef8a81cb54509d37fe2ab
```
- This will open a Jupyter lab browser window like the one below, double-click on any notebook to edit and/or re-run the examples.

- See here for [Jupyter Notebook Help](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)

![img.png](jetisu_jupyter_lab.png)