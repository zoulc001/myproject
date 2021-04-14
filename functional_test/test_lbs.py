import requests
import re 
def get_lbs_address():
    try:
        state_file=open("/home/ec2-user/deploy/terraform-deploy-nginx-kubernetes/terraform.tfstate","r")
        content=state_file.read()
        state_file.close()
        lbs_url=re.search("\"value\":.*\"(\S*\.\S*\.\S*\.\S*\.\S*)\"",content).group(1)
        return "http://"+lbs_url
    except:
        return False
def get_lbs_content():
    lbs_address=get_lbs_address()
    if lbs_address:
        res=requests.get(lbs_address)
        return res.text
    return False
if __name__=="__main__":
    print get_lbs_content()
