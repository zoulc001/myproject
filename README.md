# myproject
=======
This is a CI CD project that build docker image and deploy it on aws eks.\n
index.html will be included in the docker image and replace the original nginx index page.\n
Folder 'build_image' contains the Dokcerfile that needed to build the nginx docker image.\n
Folder 'deploy' contains terraform config files, enter the sub-folder and use command "terraform apply", it will aotomatically created the defined aws resource.\n
If you want to delete the created resources, use command "terraform destroy".\n
Folder 'functional_test' contains the test that need to be run 

