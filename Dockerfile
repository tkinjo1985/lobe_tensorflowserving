FROM tensorflow/serving

WORKDIR /work

RUN apt-get update && apt-get install -y \
    sudo \
    git

# CMD [ "/bin/bash" ]
