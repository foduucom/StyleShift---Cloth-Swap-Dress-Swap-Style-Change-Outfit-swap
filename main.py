#This is an example that uses the websockets api to know when a prompt execution is done
#Once the prompt execution is done it downloads the images using the /history endpoint

import websocket #NOTE: websocket-client (https://github.com/websocket-client/websocket-client)
import uuid
import json
import urllib.request
import urllib.parse

server_address = "127.0.0.1:8188"
client_id = str(uuid.uuid4())

def queue_prompt(prompt):
    p = {"prompt": prompt, "client_id": client_id}
    data = json.dumps(p).encode('utf-8')
    req =  urllib.request.Request("http://{}/prompt".format(server_address), data=data)
    return json.loads(urllib.request.urlopen(req).read())

def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    with urllib.request.urlopen("http://{}/view?{}".format(server_address, url_values)) as response:
        return response.read()

def get_history(prompt_id):
    with urllib.request.urlopen("http://{}/history/{}".format(server_address, prompt_id)) as response:
        return json.loads(response.read())

def get_images(ws, prompt):
    prompt_id = queue_prompt(prompt)['prompt_id']
    output_images = {}
    while True:
        out = ws.recv()
        if isinstance(out, str):
            message = json.loads(out)
            if message['type'] == 'executing':
                data = message['data']
                if data['node'] is None and data['prompt_id'] == prompt_id:
                    break #Execution is done
        else:
            continue #previews are binary data

    history = get_history(prompt_id)[prompt_id]
    for node_id in history['outputs']:
        node_output = history['outputs'][node_id]
        images_output = []
        if 'images' in node_output:
            for image in node_output['images']:
                image_data = get_image(image['filename'], image['subfolder'], image['type'])
                images_output.append(image_data)
        output_images[node_id] = images_output

    return output_images

prompt_text = """
{
  "1": {
    "inputs": {
      "sam_model": "sam_vit_h (2.56GB)",
      "grounding_dino_model": "GroundingDINO_SwinT_OGC (694MB)",
      "threshold": 0.3,
      "detail_method": "VITMatte",
      "detail_erode": 6,
      "detail_dilate": 6,
      "black_point": 0.01,
      "white_point": 0.99,
      "process_detail": false,
      "prompt": "shirt",
      "device": "cuda",
      "max_megapixels": 2,
      "cache_model": true,
      "image": [
        "2",
        0
      ]
    },
    "class_type": "LayerMask: SegmentAnythingUltra V2",
    "_meta": {
      "title": "LayerMask: SegmentAnythingUltra V2"
    }
  },
  "2": {
    "inputs": {
      "image": "q.jpg",
      "upload": "image"
    },
    "class_type": "LoadImage",
    "_meta": {
      "title": "Load Image"
    }
  },
  "3": {
    "inputs": {
      "image": "tshirt.jpeg",
      "upload": "image"
    },
    "class_type": "LoadImage",
    "_meta": {
      "title": "Load Image"
    }
  },
  "5": {
    "inputs": {
      "mask_grow": 25,
      "mixed_precision": "fp16",
      "seed": 95593377186337,
      "steps": 40,
      "cfg": 2.5,
      "image": [
        "2",
        0
      ],
      "mask": [
        "1",
        1
      ],
      "refer_image": [
        "3",
        0
      ]
    },
    "class_type": "CatVTONWrapper",
    "_meta": {
      "title": "CatVTON Wrapper"
    }
  },
  "6": {
    "inputs": {
      "images": [
        "5",
        0
      ]
    },
    "class_type": "PreviewImage",
    "_meta": {
      "title": "Preview Image"
    }
  }
}"""

prompt = json.loads(prompt_text)

prompt["2"]["inputs"]["image"] = "\\ put your input person pose image"
prompt["3"]["inputs"]["image"] = "\\ put your input cloth image"

ws = websocket.WebSocket()
ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
images = get_images(ws, prompt)

# Commented out code to display the output images:

for node_id in images:
    for image_data in images[node_id]:
        from PIL import Image
        import io
        image = Image.open(io.BytesIO(image_data))
        image.save("output.jpg")
        # image.show()


