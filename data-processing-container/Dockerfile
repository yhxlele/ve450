# install from dl-docker cpu version
FROM gaole/deeplearning-wrapper

# work dir as app
WORKDIR /app

# copy the app file into the directory
ADD . /app

# install the requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# RUN pip install --upgrade tensorflow 

# expose the 80
EXPOSE 80

# ENV NAME deep-learning-container

CMD ["python", "app.py"]
# CMD ["/bin/bash"]



