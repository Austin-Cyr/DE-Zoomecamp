# to install terraform navigate to main folder

cd ~
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz
tar -xf google-cloud-cli-linux-x86_64.tar.gz


sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl

wget -O- https://apt.releases.hashicorp.com/gpg | \
  gpg --dearmor | \
  sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
  sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt-get update && sudo apt-get install terraform

# create tf folder strux

cd /workspaces/DE-Zoomecamp
mkdir terraform
touch terraform/main.tf
code terraform/main.tf

# create folder to store keys from gcp
mkdir keys
#create file to store key
nano my-creds.json
# copy keys from json file you downloaded from gc;p

# paste in nano
ctrl+x to leave
hit enter

# install hashicorp terraform extension

# make folder struct
cd /workspaces/DE-Zoomecamp
mkdir terraform
touch terraform/main.tf
code terraform/main.tf

# add to gitignore
echo "terraform/keys/" >> .gitignore
echo "*.json" >> .gitignore
echo ".terraform/" >> .gitignore
echo "*.tfstate*" >> .gitignore

# create folder for keys and json
cd terraform
> pwd
/workspaces/DE-Zoomecamp/terraform
> mkdir keys
> nano my-cred.json

# copy key from GCP in here

# go to web band search terraform google provider

copy provider info

copy gcs project id from gcs web

# ENTER BELOW 
export GOOGLE_CREDENTIALS='home/workspaces/terraform/keys/my-cred.json'

# then test with 
echo $GOOGLE_CREDENTIALS

#will need to run each time i come back to here. 
export GOOGLE_CREDENTIALS='/workspaces/DE-Zoomecamp/terraform/keys/my-cred.json'

# go to terraform folder to initialize
terraform init

jq 'keys' /workspaces/DE-Zoomecamp/terraform/keys/my-cred.json
jq -r '.client_email, .private_key_id' /workspaces/DE-Zoomecamp/terraform/keys/my-cred.json