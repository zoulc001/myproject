# myproject
=======
This is a CI CD project that build docker image and deploy it on aws eks.
index.html will be included in the docker image and replace the original nginx index page.
Folder build_image contains the Dokcerfile that needed to build the nginx docker image.
Folder deploy contains terraform config files, enter the sub-folder and use command "terraform apply", it will aotomatically created the defined aws resource.
If you want to delete the created resources, use command "terraform destroy".
