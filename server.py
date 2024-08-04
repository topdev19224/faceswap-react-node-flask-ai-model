from flask import Flask, request, jsonify
from roop import core

app = Flask(__name__)

@app.route("/swap-faces", methods=['POST'])
def process_images():
  try:
    data = request.get_json()
    source_path = data.get('sourcePath')
    target_path = data.get('targetPath')
    output_path = data.get('outputPath')
    
    if (not source_path or not target_path or not output_path):
      return jsonify({"code": 400, "message": "Bad request"})
    res = core.run(source_path, target_path, output_path)
    print(res)
    if (res):
      return jsonify({"code": 200, 'message': 'Successfully swapped'})
  except Exception as e:
    print(e)
    return jsonify({"code": 500, "message": "Server error"})
  
if __name__ == '__main__':
  app.run()
  