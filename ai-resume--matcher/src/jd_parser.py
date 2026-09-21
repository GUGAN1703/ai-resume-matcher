with open(r"data\job_descriptions\ml_data_analyst_jd.txt","r") as file:
    content = file.read()
required = ["python","SQL","Statistics"]
def jd_cleaner():
    line = content.splitlines()
    

