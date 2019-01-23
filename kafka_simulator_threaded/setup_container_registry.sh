

######################################################################
#
# Google Cloud - Container Registry
#
######################################################################


# Authenticate - configure Docker to use the gcloud
gcloud auth configure-docker


# Tag the image with a registry name
project_id=ml-healthcare-poc-201901 
container_name=kafka_simulator
docker tag kafka_simulator gcr.io/$project_id/$container_name


# Push the image to Container Registry
docker push gcr.io/$project_id/$container_name


# Pull the image from Conainer Registry
project_id=ml-healthcare-poc-201901
container_name=kafka_simulator
#docker pull gcr.io/$project_id/$container_name
#docker run gcr.io/$project_id/$container_name


#ZEND
