import hashlib

def calculate_md5(file_path):
    with open(file_path, 'rb') as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()


file_path = 'D:\\学校任务\\学期三\\Anti-Malware Technologies\\test\\test_malware_2.txt'
md5_hash = calculate_md5(file_path)
print("MD5 Hash of test file:", md5_hash)
