from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os

app = Flask(__name__)

# MinIO configuration
minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SECRET_KEY'),
    secure=False
)

bucket_name = "mybucket"

@app.route('/store', methods=['POST'])
def store_image():
   
    file_path = '/api/api/docker-v.jpg'

    try:
        with open(file_path, 'rb') as f:
            # Upload the file to Minio
            minio_client.put_object(bucket_name, os.path.basename(file_path), f, os.stat(file_path).st_size)
        
        return jsonify({"message": "File uploaded successfully"}), 200
    
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)    
    app.run(host='0.0.0.0', port=5000)
