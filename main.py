import hashlib
def main():
    File_read = open(r"shadowfile.txt","r")
    File_result = open(r"shadowfileans.txt","r")
    
    #hash = hashlib.md5( salt + key_string ).hexdigest()
